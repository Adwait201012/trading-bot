import yfinance as yf
import pandas as pd
from config import DATA_INTERVAL, DATA_PERIOD


def fetch_ohlcv(symbol: str, period: str = DATA_PERIOD, interval: str = DATA_INTERVAL) -> pd.DataFrame:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval)
    if df.empty:
        return df
    df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
    df.dropna(inplace=True)
    return df


def fetch_current_price(symbol: str) -> float | None:
    ticker = yf.Ticker(symbol)
    info = ticker.fast_info
    try:
        return float(info.last_price)
    except Exception:
        return None


def fetch_all_watchlist(watchlist: list[str]) -> dict[str, pd.DataFrame]:
    data = {}
    for symbol in watchlist:
        df = fetch_ohlcv(symbol)
        if not df.empty:
            data[symbol] = df
    return data
