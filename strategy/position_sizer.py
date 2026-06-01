"""
ATR-based position sizing.
Sizes position so that a stop-loss hit = exactly RISK_PER_TRADE_PCT of portfolio.
"""
import math
from config import RISK_PER_TRADE_PCT, MAX_POSITION_PCT, ATR_STOP_MULTIPLIER


def calculate(portfolio_value: float, entry_price: float, atr: float) -> dict:
    stop_distance = ATR_STOP_MULTIPLIER * atr          # distance to stop in ₹
    stop_price    = entry_price - stop_distance

    risk_amount   = portfolio_value * RISK_PER_TRADE_PCT
    qty           = math.floor(risk_amount / stop_distance) if stop_distance > 0 else 1
    qty           = max(qty, 1)

    # Cap at MAX_POSITION_PCT of portfolio
    max_qty  = math.floor((portfolio_value * MAX_POSITION_PCT) / entry_price)
    qty      = min(qty, max_qty)

    cost     = qty * entry_price
    risk_pct = (stop_distance * qty) / portfolio_value * 100

    return {
        "qty":        qty,
        "stop_price": round(stop_price, 2),
        "cost":       round(cost, 2),
        "risk_pct":   round(risk_pct, 2),
        "atr":        round(atr, 2),
    }
