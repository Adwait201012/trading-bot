"""
Paper trading execution with ATR-based stop losses, trailing stops,
scale-in near support, and circuit-breaker integration.
NO real money order execution.
"""
from config import (MAX_OPEN_POSITIONS, ATR_STOP_MULTIPLIER,
                    ATR_TRAIL_MULTIPLIER, FIXED_TARGET_RR)
from trading.portfolio import get_portfolio, buy, sell, update_trailing_stop, get_total_value
from strategy.position_sizer import calculate as size_position
from strategy.risk_manager import check_circuit_breaker, should_exit_trailing
from data.fetcher import fetch_current_price


def execute_signal(signal: dict) -> dict | None:
    portfolio = get_portfolio()
    symbol    = signal["symbol"]
    price     = signal["price"]
    atr       = signal["atr"]
    action    = signal["action"]

    prices = {s: fetch_current_price(s) or p["avg_price"]
              for s, p in portfolio["positions"].items()}
    port_val = get_total_value(portfolio, prices)

    # Circuit breaker check
    cb = check_circuit_breaker(port_val, portfolio.get("peak_value", port_val), port_val)
    if cb["halted"]:
        return {"ok": False, "msg": f"CIRCUIT BREAKER: {' | '.join(cb['reasons'])}"}

    if action == "BUY":
        if len(portfolio["positions"]) >= MAX_OPEN_POSITIONS:
            return {"ok": False, "msg": f"Max {MAX_OPEN_POSITIONS} positions reached"}
        if symbol in portfolio["positions"]:
            return {"ok": False, "msg": f"Already holding {symbol}"}

        sizing = size_position(port_val, price, atr)
        stop   = price - ATR_STOP_MULTIPLIER * atr
        target = price + FIXED_TARGET_RR * ATR_STOP_MULTIPLIER * atr
        return buy(symbol, sizing["qty"], price, stop, target)

    elif action == "SELL":
        if symbol not in portfolio["positions"]:
            return {"ok": False, "msg": f"No position in {symbol}"}
        qty = portfolio["positions"][symbol]["qty"]
        return sell(symbol, qty, price, reason="signal")

    return None


def check_exits(current_prices: dict) -> list[dict]:
    """Check trailing stops and targets for all open positions."""
    portfolio = get_portfolio()
    results   = []

    for symbol, pos in list(portfolio["positions"].items()):
        price = current_prices.get(symbol)
        if not price:
            continue

        atr = pos.get("atr", price * 0.02)   # fallback: 2% ATR estimate

        # Update trailing stop
        new_stop = price - ATR_TRAIL_MULTIPLIER * atr
        update_trailing_stop(symbol, new_stop)

        # Re-read updated portfolio
        portfolio = get_portfolio()
        pos = portfolio["positions"].get(symbol, {})
        if not pos:
            continue

        # Trailing stop exit
        if price <= pos.get("trailing_stop", 0):
            r = sell(symbol, pos["qty"], price, reason="trailing_stop")
            r["exit_type"] = "TRAILING STOP"
            results.append(r)

        # Target exit
        elif price >= pos.get("target", float("inf")):
            r = sell(symbol, pos["qty"], price, reason="target")
            r["exit_type"] = "TARGET HIT"
            results.append(r)

    return results
