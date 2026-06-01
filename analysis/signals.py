"""
Signal generation — combines RSI, MACD, Supertrend, DMA, S/R, volume, sentiment.
Score-based: BUY >= SIGNAL_MIN_SCORE, SELL <= -SIGNAL_MIN_SCORE.
"""
from config import RSI_OVERSOLD, RSI_OVERBOUGHT, SIGNAL_MIN_SCORE


def generate_signal(symbol: str, ind: dict, sentiment: float = 0.0) -> dict:
    score, reasons = 0, []

    # ── Supertrend (strong weight) ──────────────────────────────────────────
    if ind["st_dir"] == 1:
        score += 2; reasons.append("Supertrend BULLISH")
    elif ind["st_dir"] == -1:
        score -= 2; reasons.append("Supertrend BEARISH")

    # Supertrend crossover (trend flip — high conviction)
    if ind["prev_st_dir"] == -1 and ind["st_dir"] == 1:
        score += 2; reasons.append("Supertrend flipped BULLISH (crossover)")
    elif ind["prev_st_dir"] == 1 and ind["st_dir"] == -1:
        score -= 2; reasons.append("Supertrend flipped BEARISH (crossover)")

    # ── RSI ─────────────────────────────────────────────────────────────────
    if ind["rsi"] < RSI_OVERSOLD:
        score += 2; reasons.append(f"RSI oversold ({ind['rsi']:.1f})")
    elif ind["rsi"] > RSI_OVERBOUGHT:
        score -= 2; reasons.append(f"RSI overbought ({ind['rsi']:.1f})")

    # ── MACD crossover ───────────────────────────────────────────────────────
    if ind["prev_macd_hist"] < 0 and ind["macd_hist"] > 0:
        score += 2; reasons.append("MACD bullish crossover")
    elif ind["prev_macd_hist"] > 0 and ind["macd_hist"] < 0:
        score -= 2; reasons.append("MACD bearish crossover")

    # ── DMA alignment ────────────────────────────────────────────────────────
    c = ind["close"]
    if c > ind["dma21"] > ind["dma50"]:
        score += 1; reasons.append("Price > 21 DMA > 50 DMA (uptrend)")
    elif c < ind["dma21"] < ind["dma50"]:
        score -= 1; reasons.append("Price < 21 DMA < 50 DMA (downtrend)")

    if c > ind["dma200"]:
        score += 1; reasons.append("Above 200 DMA (long-term bull)")
    else:
        score -= 1; reasons.append("Below 200 DMA (long-term bear)")

    # ── Support / Resistance ─────────────────────────────────────────────────
    support    = ind.get("support", 0)
    resistance = ind.get("resistance", float("inf"))
    if support and abs(c - support) / c < 0.02:        # within 2% of support
        score += 1; reasons.append(f"Near support ₹{support:.0f} (dip-buy zone)")
    if resistance and abs(c - resistance) / c < 0.02:  # within 2% of resistance
        score -= 1; reasons.append(f"Near resistance ₹{resistance:.0f} (sell zone)")

    # ── Bollinger Bands ──────────────────────────────────────────────────────
    if c <= ind["bb_lower"]:
        score += 1; reasons.append("At lower Bollinger Band (oversold)")
    elif c >= ind["bb_upper"]:
        score -= 1; reasons.append("At upper Bollinger Band (overbought)")

    # ── Volume confirmation ──────────────────────────────────────────────────
    if ind["volume"] > ind["vol_sma"] * 1.5:
        if score > 0:
            score += 1; reasons.append("High volume confirms bullish move")
        elif score < 0:
            score -= 1; reasons.append("High volume confirms bearish move")

    # ── News sentiment ───────────────────────────────────────────────────────
    if sentiment > 0.2:
        score += 1; reasons.append(f"Positive market sentiment ({sentiment:+.2f})")
    elif sentiment < -0.2:
        score -= 1; reasons.append(f"Negative market sentiment ({sentiment:+.2f})")

    action = "BUY" if score >= SIGNAL_MIN_SCORE else ("SELL" if score <= -SIGNAL_MIN_SCORE else "HOLD")
    return {"symbol": symbol, "action": action, "score": score,
            "reasons": reasons, "price": c, "atr": ind["atr"],
            "support": ind.get("support"), "resistance": ind.get("resistance")}
