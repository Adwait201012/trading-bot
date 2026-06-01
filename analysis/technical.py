import pandas as pd
import ta
from config import RSI_PERIOD, MACD_FAST, MACD_SLOW, MACD_SIGNAL, SMA_SHORT, SMA_LONG


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    close = df["Close"]

    df["RSI"] = ta.momentum.RSIIndicator(close, window=RSI_PERIOD).rsi()

    macd = ta.trend.MACD(close, window_fast=MACD_FAST, window_slow=MACD_SLOW, window_sign=MACD_SIGNAL)
    df["MACD"] = macd.macd()
    df["MACD_signal"] = macd.macd_signal()
    df["MACD_hist"] = macd.macd_diff()

    df["SMA_short"] = ta.trend.SMAIndicator(close, window=SMA_SHORT).sma_indicator()
    df["SMA_long"] = ta.trend.SMAIndicator(close, window=SMA_LONG).sma_indicator()
    df["EMA_short"] = ta.trend.EMAIndicator(close, window=SMA_SHORT).ema_indicator()

    bb = ta.volatility.BollingerBands(close, window=20, window_dev=2)
    df["BB_upper"] = bb.bollinger_hband()
    df["BB_lower"] = bb.bollinger_lband()
    df["BB_mid"] = bb.bollinger_mavg()

    df["Volume_SMA"] = df["Volume"].rolling(window=20).mean()

    df.dropna(inplace=True)
    return df


def get_latest(df: pd.DataFrame) -> dict:
    row = df.iloc[-1]
    prev = df.iloc[-2]
    return {
        "close": row["Close"],
        "rsi": row["RSI"],
        "macd": row["MACD"],
        "macd_signal": row["MACD_signal"],
        "macd_hist": row["MACD_hist"],
        "prev_macd_hist": prev["MACD_hist"],
        "sma_short": row["SMA_short"],
        "sma_long": row["SMA_long"],
        "ema_short": row["EMA_short"],
        "bb_upper": row["BB_upper"],
        "bb_lower": row["BB_lower"],
        "volume": row["Volume"],
        "volume_sma": row["Volume_SMA"],
    }
