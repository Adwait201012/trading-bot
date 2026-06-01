from colorama import Fore, Style, init
from trading.portfolio import get_portfolio, get_total_value
from config import STARTING_CAPITAL

init(autoreset=True)

W = f"{Fore.RED}⚠  WARNING:{Style.RESET_ALL}"


def print_risk_banner():
    print(f"\n{Fore.RED}{'!'*60}")
    print("  RISK DISCLOSURE — READ BEFORE TRADING WITH REAL MONEY")
    print(f"{'!'*60}{Style.RESET_ALL}")
    print("  • This is a paper trading system. Past signals ≠ future profit.")
    print("  • Aggressive strategies can lose 30–50%+ in bear markets.")
    print("  • ATR stops DO NOT guarantee fills at stop price (gap risk).")
    print("  • NSE circuit limits can trap you in losing positions.")
    print(f"{Fore.RED}{'!'*60}{Style.RESET_ALL}\n")


def print_backtest_results(results: list[dict]):
    if not results:
        print("  No backtest results.")
        return
    print(f"\n{Fore.CYAN}{'='*70}")
    print("  BACKTEST RESULTS  (5 years | ⚠ past performance ≠ future returns)")
    print(f"{'='*70}{Style.RESET_ALL}")
    print(f"  {'Symbol':<15} {'CAGR':>7} {'Sharpe':>7} {'MaxDD':>8} {'WinRate':>8} {'Trades':>7} {'PF':>6}")
    print(f"  {'-'*65}")
    for r in sorted(results, key=lambda x: x.get("cagr", 0), reverse=True):
        sym    = r.get("symbol", "").replace(".NS", "")
        cagr   = r.get("cagr", 0)
        sharpe = r.get("sharpe", 0)
        mdd    = r.get("max_drawdown", 0)
        wr     = r.get("win_rate", 0)
        tr     = r.get("total_trades", 0)
        pf     = r.get("profit_factor", 0)
        dd_color = Fore.RED if mdd < -20 else (Fore.YELLOW if mdd < -10 else Fore.GREEN)
        print(f"  {sym:<15} {cagr:>6.1f}% {sharpe:>7.2f} {dd_color}{mdd:>7.1f}%{Style.RESET_ALL} {wr:>7.1f}% {tr:>7} {pf:>6.2f}")
    print(f"\n  {W} Worst drawdown above means you'd have seen that loss from peak.")
    print(f"  {W} Sharpe < 1.0 = strategy barely compensates for risk taken.\n")


def print_portfolio(prices: dict):
    p     = get_portfolio()
    total = get_total_value(p, prices)
    pnl   = total - STARTING_CAPITAL
    pct   = pnl / STARTING_CAPITAL * 100
    dd    = (p.get("peak_value", total) - total) / p.get("peak_value", total) * 100

    color = Fore.GREEN if pnl >= 0 else Fore.RED
    print(f"\n{Fore.CYAN}{'='*55}")
    print("  PAPER PORTFOLIO")
    print(f"{'='*55}{Style.RESET_ALL}")
    print(f"  Starting Capital : ₹{STARTING_CAPITAL:>12,.2f}")
    print(f"  Current Value    : ₹{total:>12,.2f}")
    print(f"  Cash Available   : ₹{p['cash']:>12,.2f}")
    print(f"  Total P&L        : {color}₹{pnl:>+12,.2f}  ({pct:+.2f}%){Style.RESET_ALL}")
    if dd > 1:
        print(f"  Drawdown from peak: {Fore.RED}{dd:.2f}%{Style.RESET_ALL}")

    if p["positions"]:
        print(f"\n  {Fore.YELLOW}OPEN POSITIONS:{Style.RESET_ALL}")
        print(f"  {'Stock':<14} {'Qty':>5} {'Entry':>9} {'LTP':>9} {'Stop':>9} {'Target':>9} {'P&L':>10}")
        print(f"  {'-'*70}")
        for sym, pos in p["positions"].items():
            ltp  = prices.get(sym, pos["avg_price"])
            pnl_pos = (ltp - pos["avg_price"]) * pos["qty"]
            col  = Fore.GREEN if pnl_pos >= 0 else Fore.RED
            s    = sym.replace(".NS", "")
            print(f"  {s:<14} {pos['qty']:>5} {pos['avg_price']:>9.2f} {ltp:>9.2f} "
                  f"{pos.get('trailing_stop',0):>9.2f} {pos.get('target',0):>9.2f} "
                  f"{col}{pnl_pos:>+10.2f}{Style.RESET_ALL}")
    else:
        print(f"\n  {Fore.YELLOW}No open positions.{Style.RESET_ALL}")


def print_signal(sig: dict):
    a = sig["action"]
    c = Fore.GREEN if a == "BUY" else (Fore.RED if a == "SELL" else Fore.YELLOW)
    s = sig["symbol"].replace(".NS", "")
    print(f"\n  [{c}{a:4}{Style.RESET_ALL}] {s:<14} ₹{sig['price']:>9.2f}  ATR={sig['atr']:.2f}  score={sig['score']:+d}")
    for r in sig["reasons"]:
        print(f"         • {r}")


def print_trade(result: dict):
    if result and result.get("ok"):
        print(f"  {Fore.GREEN}✓ {result['msg']}{Style.RESET_ALL}")
    elif result:
        print(f"  {Fore.YELLOW}⚠ {result['msg']}{Style.RESET_ALL}")
