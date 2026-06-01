"""
Indian Stock Market — Aggressive Paper Trading Bot
===================================================
Commands:
  python main.py              — live scan loop (every 5 min)
  python main.py --once       — single scan
  python main.py --backtest   — run 5-year backtest on all stocks
  python main.py --portfolio  — show portfolio only
  python main.py --reset      — reset portfolio to ₹1,00,000

WARNING: No real money order execution in this version.
         Live trading hooks will be added after broker API is confirmed.
"""
import sys, time, argparse
from datetime import datetime
from colorama import Fore, Style, init

from config import ALL_STOCKS, STARTING_CAPITAL
from data.fetcher import fetch_all, fetch_current_price, fetch_backtest_data
from data.news import fetch_news, score_sentiment
from analysis.indicators import add_all, get_latest
from analysis.signals import generate_signal
from trading.paper_trader import execute_signal, check_exits
from trading.portfolio import get_portfolio, reset
from reports.reporter import (print_risk_banner, print_portfolio,
                               print_signal, print_trade, print_backtest_results)

init(autoreset=True)
SCAN_INTERVAL = 300


def _banner():
    print(f"{Fore.CYAN}")
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║  INDIAN STOCK MARKET — AGGRESSIVE TRADING BOT   ║")
    print("  ║  Supertrend + ATR Stops + Momentum + Dip-Buy    ║")
    print("  ║  ⚠  PAPER TRADING ONLY — NO REAL ORDERS ⚠       ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")


def run_backtest():
    from backtest.engine import run_multi
    print(f"\n  {Fore.YELLOW}Running 5-year backtest on {len(ALL_STOCKS)} stocks...{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}This may take 2–3 minutes. Fetching data...{Style.RESET_ALL}\n")
    data = fetch_all(ALL_STOCKS, period="5y")
    results = run_multi(ALL_STOCKS, data)
    print_backtest_results(results)


def run_scan(sentiment: float):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"\n{Fore.CYAN}[{now}] Scanning {len(ALL_STOCKS)} stocks...{Style.RESET_ALL}")

    data   = fetch_all(ALL_STOCKS)
    prices = {}
    sigs   = []

    for symbol, df in data.items():
        try:
            df_ind = add_all(df)
            if df_ind.empty:
                continue
            ind = get_latest(df_ind)
            prices[symbol] = ind["close"]
            sigs.append(generate_signal(symbol, ind, sentiment))
        except Exception as e:
            print(f"  {Fore.YELLOW}⚠ {symbol}: {e}{Style.RESET_ALL}")

    # Check trailing stop / target exits first
    exits = check_exits(prices)
    if exits:
        print(f"\n  {Fore.MAGENTA}AUTO EXITS:{Style.RESET_ALL}")
        for r in exits:
            print(f"  {Fore.MAGENTA}[{r.get('exit_type','EXIT')}] {r['msg']}{Style.RESET_ALL}")

    # Print signals sorted by absolute score
    print(f"\n  {Fore.YELLOW}SIGNALS:{Style.RESET_ALL}")
    for sig in sorted(sigs, key=lambda x: abs(x["score"]), reverse=True):
        print_signal(sig)

    # Execute trades
    print(f"\n  {Fore.YELLOW}TRADE EXECUTION:{Style.RESET_ALL}")
    acted = False
    for sig in sigs:
        if sig["action"] in ("BUY", "SELL"):
            result = execute_signal(sig)
            if result:
                print_trade(result)
                acted = True
    if not acted:
        print(f"  No trades — all HOLD or circuit breaker active.")

    # Refresh prices for open positions
    for sym in get_portfolio()["positions"]:
        if sym not in prices:
            p = fetch_current_price(sym)
            if p:
                prices[sym] = p

    print_portfolio(prices)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--once",      action="store_true")
    parser.add_argument("--backtest",  action="store_true")
    parser.add_argument("--portfolio", action="store_true")
    parser.add_argument("--reset",     action="store_true")
    args = parser.parse_args()

    _banner()
    print_risk_banner()

    if args.reset:
        reset()
        print(f"  {Fore.GREEN}Portfolio reset to ₹{STARTING_CAPITAL:,.0f}{Style.RESET_ALL}")
        return

    if args.portfolio:
        prices = {s: fetch_current_price(s) for s in ALL_STOCKS}
        print_portfolio({k: v for k, v in prices.items() if v})
        return

    if args.backtest:
        run_backtest()
        return

    print(f"  {Fore.YELLOW}Fetching market news & sentiment...{Style.RESET_ALL}")
    headlines = fetch_news()
    sentiment = score_sentiment(headlines)
    print(f"  Market sentiment: {'+' if sentiment >= 0 else ''}{sentiment:.2f}  ({len(headlines)} headlines)\n")

    if args.once:
        run_scan(sentiment)
        return

    print(f"  {Fore.CYAN}Running every {SCAN_INTERVAL//60} min. Press Ctrl+C to stop.{Style.RESET_ALL}")
    while True:
        try:
            run_scan(sentiment)
            print(f"\n  Next scan in {SCAN_INTERVAL//60} min...")
            time.sleep(SCAN_INTERVAL)
            headlines = fetch_news()
            sentiment = score_sentiment(headlines)
        except KeyboardInterrupt:
            print(f"\n  {Fore.YELLOW}Bot stopped.{Style.RESET_ALL}")
            sys.exit(0)


if __name__ == "__main__":
    main()
