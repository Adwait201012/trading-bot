"""
Indian Stock Market Paper Trading Bot
--------------------------------------
Fetches NSE stock data + market news, applies technical analysis,
generates BUY/SELL/HOLD signals, and executes simulated trades.

Run: python main.py
     python main.py --once       (single scan, no loop)
     python main.py --reset      (reset portfolio)
     python main.py --portfolio  (show portfolio only)
"""

import sys
import time
import argparse
from datetime import datetime

from colorama import Fore, Style, init

from config import WATCHLIST
from data.market_data import fetch_all_watchlist, fetch_current_price
from data.news import fetch_news, score_sentiment
from analysis.technical import add_indicators, get_latest
from analysis.signals import generate_signal
from trading.paper_trader import execute_signal, check_stop_loss_targets
from trading.portfolio import reset, get_portfolio
from reports.reporter import print_portfolio, print_signal, print_news, print_trade_result

init(autoreset=True)

SCAN_INTERVAL_SECONDS = 300  # scan every 5 minutes


def run_scan(sentiment: float):
    print(f"\n{Fore.CYAN}[{datetime.now().strftime('%H:%M:%S')}] Scanning {len(WATCHLIST)} stocks...{Style.RESET_ALL}")

    data = fetch_all_watchlist(WATCHLIST)
    current_prices = {}

    signals = []
    for symbol, df in data.items():
        try:
            df_ind = add_indicators(df)
            if df_ind.empty:
                continue
            indicators = get_latest(df_ind)
            current_prices[symbol] = indicators["close"]
            signal = generate_signal(symbol, indicators, sentiment)
            signals.append(signal)
        except Exception as e:
            print(f"  {Fore.YELLOW}⚠ Error processing {symbol}: {e}{Style.RESET_ALL}")

    # Check stop loss / targets first
    sl_results = check_stop_loss_targets(current_prices)
    for r in sl_results:
        print(f"  {Fore.MAGENTA}[AUTO EXIT] {r.get('reason', '')} — {r['msg']}{Style.RESET_ALL}")

    # Print all signals
    print(f"\n  {Fore.YELLOW}SIGNALS:{Style.RESET_ALL}")
    for signal in sorted(signals, key=lambda x: abs(x["score"]), reverse=True):
        print_signal(signal)

    # Execute actionable signals
    print(f"\n  {Fore.YELLOW}TRADE EXECUTION:{Style.RESET_ALL}")
    acted = False
    for signal in signals:
        if signal["action"] in ("BUY", "SELL"):
            result = execute_signal(signal)
            if result:
                print_trade_result(result)
                acted = True
    if not acted:
        print(f"  {Fore.YELLOW}No trades executed (all HOLD or conditions not met){Style.RESET_ALL}")

    # Refresh prices and show portfolio
    for symbol in get_portfolio()["positions"]:
        if symbol not in current_prices:
            p = fetch_current_price(symbol)
            if p:
                current_prices[symbol] = p

    print_portfolio(current_prices)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run one scan and exit")
    parser.add_argument("--reset", action="store_true", help="Reset portfolio to starting capital")
    parser.add_argument("--portfolio", action="store_true", help="Show portfolio and exit")
    args = parser.parse_args()

    print(f"{Fore.CYAN}")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║    INDIAN STOCK MARKET PAPER TRADING BOT ║")
    print("  ║    Powered by yfinance + Technical AI    ║")
    print("  ╚══════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")

    if args.reset:
        reset()
        print(f"  {Fore.GREEN}Portfolio reset to ₹{100000:,.0f}{Style.RESET_ALL}")
        return

    if args.portfolio:
        prices = {s: fetch_current_price(s) for s in WATCHLIST}
        print_portfolio({k: v for k, v in prices.items() if v})
        return

    print(f"  {Fore.YELLOW}Fetching market news...{Style.RESET_ALL}")
    headlines = fetch_news()
    sentiment = score_sentiment(headlines)
    print_news(headlines, sentiment)

    if args.once:
        run_scan(sentiment)
        return

    print(f"\n  {Fore.CYAN}Running continuously every {SCAN_INTERVAL_SECONDS//60} minutes. Press Ctrl+C to stop.{Style.RESET_ALL}")
    while True:
        try:
            run_scan(sentiment)
            print(f"\n  {Fore.CYAN}Next scan in {SCAN_INTERVAL_SECONDS//60} min... (Ctrl+C to stop){Style.RESET_ALL}")
            time.sleep(SCAN_INTERVAL_SECONDS)
            # Refresh news every cycle
            headlines = fetch_news()
            sentiment = score_sentiment(headlines)
        except KeyboardInterrupt:
            print(f"\n\n  {Fore.YELLOW}Bot stopped by user.{Style.RESET_ALL}")
            sys.exit(0)


if __name__ == "__main__":
    main()
