from config import RSI_OVERSOLD, RSI_OVERBOUGHT
from data.news import score_sentiment, get_stock_news


def generate_signal(symbol: str, indicators: dict, sentiment: float) -> dict:
    """
    Returns signal dict: action (BUY/SELL/HOLD), score, reasons
    Score > 0 = bullish, < 0 = bearish
    """
    score = 0
    reasons = []

    rsi = indicators["rsi"]
    macd_hist = indicators["macd_hist"]
    prev_macd_hist = indicators["prev_macd_hist"]
    close = indicators["close"]
    sma_short = indicators["sma_short"]
    sma_long = indicators["sma_long"]
    bb_lower = indicators["bb_lower"]
    bb_upper = indicators["bb_upper"]
    volume = indicators["volume"]
    volume_sma = indicators["volume_sma"]

    # RSI
    if rsi < RSI_OVERSOLD:
        score += 2
        reasons.append(f"RSI oversold ({rsi:.1f})")
    elif rsi > RSI_OVERBOUGHT:
        score -= 2
        reasons.append(f"RSI overbought ({rsi:.1f})")

    # MACD crossover
    if prev_macd_hist < 0 and macd_hist > 0:
        score += 2
        reasons.append("MACD bullish crossover")
    elif prev_macd_hist > 0 and macd_hist < 0:
        score -= 2
        reasons.append("MACD bearish crossover")

    # SMA trend
    if sma_short > sma_long:
        score += 1
        reasons.append("SMA short > long (uptrend)")
    else:
        score -= 1
        reasons.append("SMA short < long (downtrend)")

    # Bollinger Band squeeze
    if close <= bb_lower:
        score += 1
        reasons.append("Price at lower Bollinger Band")
    elif close >= bb_upper:
        score -= 1
        reasons.append("Price at upper Bollinger Band")

    # Volume confirmation
    if volume > volume_sma * 1.5:
        if score > 0:
            score += 1
            reasons.append("High volume confirms bullish move")
        elif score < 0:
            score -= 1
            reasons.append("High volume confirms bearish move")

    # News sentiment
    if sentiment > 0.2:
        score += 1
        reasons.append(f"Positive market sentiment ({sentiment:+.2f})")
    elif sentiment < -0.2:
        score -= 1
        reasons.append(f"Negative market sentiment ({sentiment:+.2f})")

    # Decision
    if score >= 3:
        action = "BUY"
    elif score <= -3:
        action = "SELL"
    else:
        action = "HOLD"

    return {"symbol": symbol, "action": action, "score": score, "reasons": reasons, "price": close}
