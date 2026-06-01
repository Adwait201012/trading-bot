import json
import os
from datetime import datetime
from config import STARTING_CAPITAL

PORTFOLIO_FILE = os.path.join(os.path.dirname(__file__), "..", "logs", "portfolio.json")


def _load() -> dict:
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE) as f:
            return json.load(f)
    return {
        "cash": STARTING_CAPITAL,
        "positions": {},
        "trades": [],
        "created_at": str(datetime.now()),
    }


def _save(portfolio: dict):
    os.makedirs(os.path.dirname(PORTFOLIO_FILE), exist_ok=True)
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(portfolio, f, indent=2, default=str)


def get_portfolio() -> dict:
    return _load()


def get_total_value(portfolio: dict, current_prices: dict) -> float:
    total = portfolio["cash"]
    for symbol, pos in portfolio["positions"].items():
        price = current_prices.get(symbol, pos["avg_price"])
        total += pos["qty"] * price
    return total


def buy(symbol: str, qty: int, price: float) -> dict:
    portfolio = _load()
    cost = qty * price
    if portfolio["cash"] < cost:
        return {"ok": False, "msg": f"Insufficient cash. Need ₹{cost:.0f}, have ₹{portfolio['cash']:.0f}"}

    portfolio["cash"] -= cost
    if symbol in portfolio["positions"]:
        pos = portfolio["positions"][symbol]
        total_qty = pos["qty"] + qty
        pos["avg_price"] = (pos["avg_price"] * pos["qty"] + price * qty) / total_qty
        pos["qty"] = total_qty
    else:
        portfolio["positions"][symbol] = {
            "qty": qty,
            "avg_price": price,
            "buy_time": str(datetime.now()),
        }

    portfolio["trades"].append({
        "action": "BUY", "symbol": symbol, "qty": qty,
        "price": price, "total": cost, "time": str(datetime.now()),
    })
    _save(portfolio)
    return {"ok": True, "msg": f"Bought {qty} shares of {symbol} @ ₹{price:.2f} (Total: ₹{cost:.2f})"}


def sell(symbol: str, qty: int, price: float) -> dict:
    portfolio = _load()
    if symbol not in portfolio["positions"]:
        return {"ok": False, "msg": f"No position in {symbol}"}

    pos = portfolio["positions"][symbol]
    if pos["qty"] < qty:
        return {"ok": False, "msg": f"Only have {pos['qty']} shares, tried to sell {qty}"}

    proceeds = qty * price
    pnl = (price - pos["avg_price"]) * qty
    portfolio["cash"] += proceeds
    pos["qty"] -= qty

    if pos["qty"] == 0:
        del portfolio["positions"][symbol]

    portfolio["trades"].append({
        "action": "SELL", "symbol": symbol, "qty": qty,
        "price": price, "total": proceeds, "pnl": pnl, "time": str(datetime.now()),
    })
    _save(portfolio)
    return {"ok": True, "msg": f"Sold {qty} shares of {symbol} @ ₹{price:.2f} | P&L: ₹{pnl:+.2f}"}


def reset():
    if os.path.exists(PORTFOLIO_FILE):
        os.remove(PORTFOLIO_FILE)
    return _load()
