"""
Event-driven backtesting engine.
Simulates day-by-day: signals → position sizing → ATR trailing stops → exits.

WARNING: Past performance does NOT guarantee future results.
         Backtests suffer from lookahead bias and survivorship bias.
         Always assume real returns will be WORSE than backtest shows.
"""
import math
import pandas as pd
import numpy as np
from config import (STARTING_CAPITAL, MAX_OPEN_POSITIONS, SCALE_IN_TRANCHES,
                    ATR_STOP_MULTIPLIER, ATR_TRAIL_MULTIPLIER, FIXED_TARGET_RR,
                    SIGNAL_MIN_SCORE, MAX_PORTFOLIO_DRAWDOWN)
from analysis.indicators import add_all
from analysis.signals import generate_signal
from strategy.position_sizer import calculate as size_position
from backtest.metrics import compute as compute_metrics


def run(symbol: str, df_raw: pd.DataFrame) -> dict:
    """Run backtest for a single symbol. Returns metrics + equity curve + trades."""
    if len(df_raw) < 250:
        return {"error": f"Not enough data for {symbol} ({len(df_raw)} bars)"}

    df = add_all(df_raw)
    if df.empty:
        return {"error": f"Indicators failed for {symbol}"}

    capital    = float(STARTING_CAPITAL)
    peak       = capital
    positions  = []   # active positions
    trades     = []   # closed trades
    equity     = []

    for i in range(50, len(df)):
        row  = df.iloc[i]
        prev = df.iloc[i-1]
        date = df.index[i]
        price = float(row["Close"])
        atr   = float(row["ATR"])

        # ── Update trailing stops ────────────────────────────────────────────
        for pos in list(positions):
            new_stop = float(row["High"]) - ATR_TRAIL_MULTIPLIER * atr
            pos["trailing_stop"] = max(pos["trailing_stop"], new_stop)

            # Exit: trailing stop hit
            if price <= pos["trailing_stop"]:
                pnl = (pos["trailing_stop"] - pos["entry"]) * pos["qty"]
                capital += pos["trailing_stop"] * pos["qty"]
                trades.append({"date": date, "symbol": symbol, "action": "SELL",
                               "entry": pos["entry"], "exit": pos["trailing_stop"],
                               "qty": pos["qty"], "pnl": round(pnl, 2), "reason": "trailing_stop"})
                positions.remove(pos)
                continue

            # Exit: target hit
            if price >= pos["target"]:
                pnl = (pos["target"] - pos["entry"]) * pos["qty"]
                capital += pos["target"] * pos["qty"]
                trades.append({"date": date, "symbol": symbol, "action": "SELL",
                               "entry": pos["entry"], "exit": pos["target"],
                               "qty": pos["qty"], "pnl": round(pnl, 2), "reason": "target"})
                positions.remove(pos)

        # ── Circuit breaker ──────────────────────────────────────────────────
        portfolio_val = capital + sum(p["qty"] * price for p in positions)
        peak = max(peak, portfolio_val)
        drawdown = (peak - portfolio_val) / peak
        equity.append({"date": date, "value": portfolio_val})

        if drawdown >= MAX_PORTFOLIO_DRAWDOWN:
            continue  # halted — no new trades

        # ── Generate signal ──────────────────────────────────────────────────
        ind = {
            "close": price, "high": float(row["High"]), "low": float(row["Low"]),
            "rsi": float(row["RSI"]), "macd_hist": float(row["MACD_hist"]),
            "prev_macd_hist": float(prev["MACD_hist"]),
            "dma21": float(row["DMA21"]), "dma50": float(row["DMA50"]),
            "dma200": float(row["DMA200"]), "atr": atr,
            "bb_upper": float(row["BB_upper"]), "bb_lower": float(row["BB_lower"]),
            "st_dir": int(row["ST_dir"]), "prev_st_dir": int(prev["ST_dir"]),
            "supertrend": float(row["ST"]), "support": float(row["Support"]),
            "resistance": float(row["Resistance"]),
            "volume": float(row["Volume"]), "vol_sma": float(row["Vol_SMA"]),
        }
        signal = generate_signal(symbol, ind, sentiment=0.0)

        # ── Entry ────────────────────────────────────────────────────────────
        if signal["action"] == "BUY" and len(positions) < MAX_OPEN_POSITIONS:
            sizing = size_position(portfolio_val, price, atr)
            qty    = sizing["qty"]
            cost   = qty * price
            if cost <= capital and qty > 0:
                stop   = price - ATR_STOP_MULTIPLIER * atr
                target = price + FIXED_TARGET_RR * ATR_STOP_MULTIPLIER * atr
                capital -= cost
                positions.append({
                    "entry": price, "qty": qty,
                    "stop": stop, "target": target,
                    "trailing_stop": stop,
                })

    # Close remaining positions at last price
    last_price = float(df.iloc[-1]["Close"])
    for pos in positions:
        pnl = (last_price - pos["entry"]) * pos["qty"]
        capital += last_price * pos["qty"]
        trades.append({"symbol": symbol, "action": "SELL", "entry": pos["entry"],
                       "exit": last_price, "qty": pos["qty"],
                       "pnl": round(pnl, 2), "reason": "end_of_backtest"})

    eq_series = pd.Series({e["date"]: e["value"] for e in equity})
    metrics   = compute_metrics(eq_series, trades)
    metrics["symbol"] = symbol

    return {"metrics": metrics, "trades": trades, "equity": eq_series}


def run_multi(symbols: list[str], data: dict[str, pd.DataFrame]) -> list[dict]:
    """Run backtest across all symbols, print summary table."""
    results = []
    for symbol in symbols:
        if symbol not in data:
            continue
        result = run(symbol, data[symbol])
        if "error" not in result:
            results.append(result["metrics"])
    return results
