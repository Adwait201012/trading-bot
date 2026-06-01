"""Data fetching — supports yfinance (default) and future paid APIs."""
import yfinance as yf
import pandas as pd
from config import DATA_INTERVAL, LIVE_PERIOD, BACKTEST_PERIOD


def fetch_ohlcv(symbol: str, period: str = LIVE_PERIOD, interval: str = DATA_INTERVAL) -> pd.DataFrame:
    try:
        df = yf.Ticker(symbol).history(period=period, interval=interval)
        if df.empty:
            return pd.DataFrame()
        df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
        df.dropna(inplace=True)
        return df
    except Exception as e:
        print(f"  [WARN] Failed to fetch {symbol}: {e}")
        return pd.DataFrame()


def fetch_backtest_data(symbol: str) -> pd.DataFrame:
    return fetch_ohlcv(symbol, period=BACKTEST_PERIOD)


def fetch_current_price(symbol: str) -> float | None:
    try:
        return float(yf.Ticker(symbol).fast_info.last_price)
    except Exception:
        return None


def fetch_all(symbols: list[str], period: str = LIVE_PERIOD) -> dict[str, pd.DataFrame]:
    return {s: df for s in symbols if not (df := fetch_ohlcv(s, period=period)).empty}
