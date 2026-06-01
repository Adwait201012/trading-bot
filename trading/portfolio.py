import json, os, math
from datetime import datetime
from config import STARTING_CAPITAL

PORTFOLIO_FILE = os.path.join(os.path.dirname(__file__), "..", "logs", "portfolio.json")


def _load() -> dict:
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE) as f:
            return json.load(f)
    return {"cash": STARTING_CAPITAL, "peak_value": STARTING_CAPITAL,
            "positions": {}, "trades": [], "created_at": str(datetime.now())}


def _save(p: dict):
    os.makedirs(os.path.dirname(PORTFOLIO_FILE), exist_ok=True)
    with open(PORTFOLIO_FILE, "w") as f:
        json.dump(p, f, indent=2, default=str)


def get_portfolio() -> dict:
    p = _load(); _save(p); return p


def get_total_value(p: dict, prices: dict) -> float:
    return p["cash"] + sum(pos["qty"] * prices.get(s, pos["avg_price"])
                           for s, pos in p["positions"].items())


def buy(symbol: str, qty: int, price: float, stop: float, target: float) -> dict:
    p = _load()
    cost = qty * price
    if p["cash"] < cost:
        return {"ok": False, "msg": f"Insufficient cash ₹{cost:.0f} > ₹{p['cash']:.0f}"}
    p["cash"] -= cost
    if symbol in p["positions"]:
        pos = p["positions"][symbol]
        total = pos["qty"] + qty
        pos["avg_price"] = (pos["avg_price"] * pos["qty"] + price * qty) / total
        pos["qty"] = total
    else:
        p["positions"][symbol] = {"qty": qty, "avg_price": price,
                                   "stop": stop, "target": target,
                                   "trailing_stop": stop, "time": str(datetime.now())}
    p["trades"].append({"action": "BUY", "symbol": symbol, "qty": qty,
                         "price": price, "total": cost, "time": str(datetime.now())})
    _save(p)
    return {"ok": True, "msg": f"Bought {qty} × {symbol} @ ₹{price:.2f} | Stop ₹{stop:.2f} | Target ₹{target:.2f}"}


def sell(symbol: str, qty: int, price: float, reason: str = "") -> dict:
    p = _load()
    if symbol not in p["positions"]:
        return {"ok": False, "msg": f"No position in {symbol}"}
    pos = p["positions"][symbol]
    qty = min(qty, pos["qty"])
    proceeds = qty * price
    pnl = (price - pos["avg_price"]) * qty
    p["cash"] += proceeds
    pos["qty"] -= qty
    if pos["qty"] == 0:
        del p["positions"][symbol]
    p["trades"].append({"action": "SELL", "symbol": symbol, "qty": qty,
                         "price": price, "total": proceeds, "pnl": round(pnl, 2),
                         "reason": reason, "time": str(datetime.now())})
    _save(p)
    return {"ok": True, "msg": f"Sold {qty} × {symbol} @ ₹{price:.2f} | P&L ₹{pnl:+.2f} [{reason}]"}


def update_trailing_stop(symbol: str, new_stop: float):
    p = _load()
    if symbol in p["positions"]:
        old = p["positions"][symbol].get("trailing_stop", 0)
        p["positions"][symbol]["trailing_stop"] = max(old, new_stop)
        _save(p)


def reset():
    if os.path.exists(PORTFOLIO_FILE):
        os.remove(PORTFOLIO_FILE)
    p = _load(); _save(p); return p
