import math
from config import MAX_POSITION_SIZE, STOP_LOSS_PCT, TARGET_PCT, MAX_OPEN_POSITIONS
from trading.portfolio import get_portfolio, buy, sell, get_total_value
from data.market_data import fetch_current_price


def calc_qty(symbol: str, price: float, portfolio_value: float) -> int:
    max_spend = portfolio_value * MAX_POSITION_SIZE
    qty = math.floor(max_spend / price)
    return max(1, qty)


def execute_signal(signal: dict) -> dict | None:
    portfolio = get_portfolio()
    symbol = signal["symbol"]
    action = signal["action"]
    price = signal["price"]

    current_prices = {s: fetch_current_price(s) or p["avg_price"]
                      for s, p in portfolio["positions"].items()}
    portfolio_value = get_total_value(portfolio, current_prices)

    if action == "BUY":
        if len(portfolio["positions"]) >= MAX_OPEN_POSITIONS:
            return {"ok": False, "msg": f"Max positions ({MAX_OPEN_POSITIONS}) reached"}
        if symbol in portfolio["positions"]:
            return {"ok": False, "msg": f"Already holding {symbol}"}
        qty = calc_qty(symbol, price, portfolio_value)
        return buy(symbol, qty, price)

    elif action == "SELL":
        if symbol not in portfolio["positions"]:
            return {"ok": False, "msg": f"No position in {symbol} to sell"}
        qty = portfolio["positions"][symbol]["qty"]
        return sell(symbol, qty, price)

    return None


def check_stop_loss_targets(current_prices: dict) -> list[dict]:
    portfolio = get_portfolio()
    results = []
    for symbol, pos in list(portfolio["positions"].items()):
        current = current_prices.get(symbol)
        if not current:
            continue
        avg = pos["avg_price"]
        change_pct = (current - avg) / avg

        if change_pct <= -STOP_LOSS_PCT:
            result = sell(symbol, pos["qty"], current)
            result["reason"] = f"STOP LOSS hit ({change_pct*100:.1f}%)"
            results.append(result)
        elif change_pct >= TARGET_PCT:
            result = sell(symbol, pos["qty"], current)
            result["reason"] = f"TARGET hit ({change_pct*100:.1f}%)"
            results.append(result)

    return results
