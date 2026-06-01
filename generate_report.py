"""Generates REPORT.md — readable on GitHub after each Actions run."""
import json, os
from datetime import datetime

PORTFOLIO_FILE = "logs/portfolio.json"
REPORT_FILE    = "REPORT.md"
STARTING       = 100_000


def load():
    if not os.path.exists(PORTFOLIO_FILE):
        return None
    with open(PORTFOLIO_FILE) as f:
        return json.load(f)


def main():
    p   = load()
    now = datetime.now().strftime("%Y-%m-%d %H:%M IST")
    L   = []

    L.append("# 📈 Trading Bot — Live Portfolio Report")
    L.append(f"\n**Last updated:** {now}\n")
    L.append("> ⚠️ **PAPER TRADING ONLY — No real money at risk**\n")

    if not p:
        L.append("_No portfolio data yet. Bot will populate this after first scan._")
    else:
        cash      = p.get("cash", STARTING)
        positions = p.get("positions", {})
        trades    = p.get("trades", [])
        pos_val   = sum(pos["qty"] * pos["avg_price"] for pos in positions.values())
        total     = cash + pos_val
        pnl       = total - STARTING
        pct       = pnl / STARTING * 100
        peak      = p.get("peak_value", total)
        dd        = (peak - total) / peak * 100 if peak > 0 else 0

        emoji = "🟢" if pnl >= 0 else "🔴"
        dd_emoji = "🔴" if dd > 5 else ("🟡" if dd > 2 else "🟢")

        L.append("## 💰 Portfolio Summary")
        L.append("| Metric | Value |")
        L.append("|---|---|")
        L.append(f"| Starting Capital | ₹{STARTING:,.2f} |")
        L.append(f"| Current Value | ₹{total:,.2f} |")
        L.append(f"| Cash Available | ₹{cash:,.2f} |")
        L.append(f"| Total P&L | {emoji} ₹{pnl:+,.2f} ({pct:+.2f}%) |")
        L.append(f"| Drawdown from Peak | {dd_emoji} {dd:.2f}% |")

        if positions:
            L.append("\n## 📂 Open Positions")
            L.append("| Stock | Qty | Entry | Stop | Target | Est. Value |")
            L.append("|---|---|---|---|---|---|")
            for sym, pos in positions.items():
                s = sym.replace(".NS", "")
                val = pos["qty"] * pos["avg_price"]
                L.append(f"| {s} | {pos['qty']} | ₹{pos['avg_price']:.2f} | "
                         f"₹{pos.get('trailing_stop',0):.2f} | ₹{pos.get('target',0):.2f} | ₹{val:,.2f} |")
        else:
            L.append("\n## 📂 Open Positions\n_No open positions._")

        if trades:
            closed_pnl = sum(t.get("pnl", 0) for t in trades if "pnl" in t)
            wins  = sum(1 for t in trades if t.get("pnl", 0) > 0)
            total_closed = sum(1 for t in trades if "pnl" in t)
            wr = wins / total_closed * 100 if total_closed else 0

            L.append(f"\n## 📋 Trade History ({total_closed} closed | Win rate {wr:.0f}% | Total P&L ₹{closed_pnl:+,.2f})")
            L.append("| Time | Action | Stock | Qty | Price | P&L | Reason |")
            L.append("|---|---|---|---|---|---|---|")
            for t in reversed(trades[-15:]):
                s = t["symbol"].replace(".NS", "")
                a = "🟢 BUY" if t["action"] == "BUY" else "🔴 SELL"
                pnl_str = f"₹{t.get('pnl', 0):+.2f}" if "pnl" in t else "—"
                L.append(f"| {t['time'][:16]} | {a} | {s} | {t['qty']} | "
                         f"₹{t['price']:.2f} | {pnl_str} | {t.get('reason','')} |")

    L.append("\n---")
    L.append("**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance")
    L.append("\n**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade")
    L.append("\n*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*")

    with open(REPORT_FILE, "w") as f:
        f.write("\n".join(L))
    print(f"Report written → {REPORT_FILE}")


if __name__ == "__main__":
    main()
