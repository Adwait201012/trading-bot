from colorama import Fore, Style, init
from trading.portfolio import get_portfolio, get_total_value
from config import STARTING_CAPITAL

init(autoreset=True)


def print_portfolio(current_prices: dict):
    portfolio = get_portfolio()
    total = get_total_value(portfolio, current_prices)
    total_pnl = total - STARTING_CAPITAL
    pnl_pct = (total_pnl / STARTING_CAPITAL) * 100
    pnl_color = Fore.GREEN if total_pnl >= 0 else Fore.RED

    print(f"\n{Fore.CYAN}{'='*55}")
    print(f"  PAPER TRADING PORTFOLIO SUMMARY")
    print(f"{'='*55}{Style.RESET_ALL}")
    print(f"  Starting Capital : ₹{STARTING_CAPITAL:,.2f}")
    print(f"  Current Value    : ₹{total:,.2f}")
    print(f"  Cash Available   : ₹{portfolio['cash']:,.2f}")
    print(f"  Total P&L        : {pnl_color}₹{total_pnl:+,.2f} ({pnl_pct:+.2f}%){Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*55}{Style.RESET_ALL}")

    if portfolio["positions"]:
        print(f"\n  {Fore.YELLOW}OPEN POSITIONS:{Style.RESET_ALL}")
        print(f"  {'Symbol':<20} {'Qty':>5} {'Avg':>10} {'LTP':>10} {'P&L':>12}")
        print(f"  {'-'*60}")
        for symbol, pos in portfolio["positions"].items():
            ltp = current_prices.get(symbol, pos["avg_price"])
            pnl = (ltp - pos["avg_price"]) * pos["qty"]
            pnl_pct_pos = ((ltp - pos["avg_price"]) / pos["avg_price"]) * 100
            color = Fore.GREEN if pnl >= 0 else Fore.RED
            short = symbol.replace(".NS", "")
            print(f"  {short:<20} {pos['qty']:>5} {pos['avg_price']:>10.2f} {ltp:>10.2f} {color}{pnl:>+10.2f} ({pnl_pct_pos:+.1f}%){Style.RESET_ALL}")
    else:
        print(f"\n  {Fore.YELLOW}No open positions.{Style.RESET_ALL}")


def print_signal(signal: dict):
    action = signal["action"]
    color = Fore.GREEN if action == "BUY" else (Fore.RED if action == "SELL" else Fore.YELLOW)
    short = signal["symbol"].replace(".NS", "")
    print(f"\n  [{color}{action}{Style.RESET_ALL}] {short:<15} ₹{signal['price']:.2f}  score={signal['score']:+d}")
    for r in signal["reasons"]:
        print(f"       • {r}")


def print_news(headlines: list[dict], sentiment: float):
    color = Fore.GREEN if sentiment > 0.1 else (Fore.RED if sentiment < -0.1 else Fore.YELLOW)
    print(f"\n{Fore.CYAN}  MARKET NEWS  (sentiment: {color}{sentiment:+.2f}{Style.RESET_ALL}{Fore.CYAN}){Style.RESET_ALL}")
    for h in headlines[:8]:
        print(f"  [{h['source'][:12]:<12}] {h['title'][:70]}")


def print_trade_result(result: dict):
    if result and result.get("ok"):
        print(f"  {Fore.GREEN}✓ {result['msg']}{Style.RESET_ALL}")
    elif result:
        print(f"  {Fore.YELLOW}⚠ {result['msg']}{Style.RESET_ALL}")
