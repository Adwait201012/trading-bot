"""
All technical indicators in one place.
Supertrend, ATR, RSI, MACD, DMAs, Bollinger, Support/Resistance.
"""
import numpy as np
import pandas as pd
import ta
from config import (RSI_PERIOD, MACD_FAST, MACD_SLOW, MACD_SIGNAL,
                    DMA_SHORT, DMA_MID, DMA_LONG, ATR_PERIOD,
                    SUPERTREND_PERIOD, SUPERTREND_MULT, SUPPORT_WINDOW)


def add_all(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    c, h, l, v = df["Close"], df["High"], df["Low"], df["Volume"]

    # RSI
    df["RSI"] = ta.momentum.RSIIndicator(c, window=RSI_PERIOD).rsi()

    # MACD
    macd = ta.trend.MACD(c, window_fast=MACD_FAST, window_slow=MACD_SLOW, window_sign=MACD_SIGNAL)
    df["MACD"] = macd.macd()
    df["MACD_signal"] = macd.macd_signal()
    df["MACD_hist"] = macd.macd_diff()

    # Moving averages
    df["DMA21"]  = ta.trend.EMAIndicator(c, window=DMA_SHORT).ema_indicator()
    df["DMA50"]  = ta.trend.SMAIndicator(c, window=DMA_MID).sma_indicator()
    df["DMA200"] = ta.trend.SMAIndicator(c, window=DMA_LONG).sma_indicator()

    # ATR
    df["ATR"] = ta.volatility.AverageTrueRange(h, l, c, window=ATR_PERIOD).average_true_range()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(c, window=20, window_dev=2)
    df["BB_upper"] = bb.bollinger_hband()
    df["BB_lower"] = bb.bollinger_lband()

    # Volume SMA
    df["Vol_SMA"] = v.rolling(20).mean()

    # Supertrend
    df["ST"], df["ST_dir"] = _supertrend(df, SUPERTREND_PERIOD, SUPERTREND_MULT)

    # Support / Resistance
    df["Support"]    = l.rolling(SUPPORT_WINDOW * 2 + 1, center=True).min()
    df["Resistance"] = h.rolling(SUPPORT_WINDOW * 2 + 1, center=True).max()

    # Drop only rows where core signals are missing; DMA200 allowed to be NaN early on
    core = ["RSI", "MACD_hist", "DMA21", "DMA50", "ATR", "ST"]
    df.dropna(subset=core, inplace=True)
    return df


def _supertrend(df: pd.DataFrame, period: int, mult: float):
    hl2  = (df["High"] + df["Low"]) / 2
    atr  = ta.volatility.AverageTrueRange(df["High"], df["Low"], df["Close"], window=period).average_true_range()

    ub_raw = hl2 + mult * atr
    lb_raw = hl2 - mult * atr

    ub = ub_raw.copy()
    lb = lb_raw.copy()
    st = pd.Series(np.nan, index=df.index)
    direction = pd.Series(0, index=df.index)

    for i in range(1, len(df)):
        # Final upper band
        ub.iloc[i] = ub_raw.iloc[i] if (ub_raw.iloc[i] < ub.iloc[i-1] or df["Close"].iloc[i-1] > ub.iloc[i-1]) else ub.iloc[i-1]
        # Final lower band
        lb.iloc[i] = lb_raw.iloc[i] if (lb_raw.iloc[i] > lb.iloc[i-1] or df["Close"].iloc[i-1] < lb.iloc[i-1]) else lb.iloc[i-1]

        if pd.isna(st.iloc[i-1]) or st.iloc[i-1] == ub.iloc[i-1]:
            if df["Close"].iloc[i] <= ub.iloc[i]:
                st.iloc[i] = ub.iloc[i];  direction.iloc[i] = -1
            else:
                st.iloc[i] = lb.iloc[i];  direction.iloc[i] =  1
        else:
            if df["Close"].iloc[i] >= lb.iloc[i]:
                st.iloc[i] = lb.iloc[i];  direction.iloc[i] =  1
            else:
                st.iloc[i] = ub.iloc[i];  direction.iloc[i] = -1

    return st, direction


def get_latest(df: pd.DataFrame) -> dict:
    r, p = df.iloc[-1], df.iloc[-2]
    return {
        "close":        r["Close"],
        "high":         r["High"],
        "low":          r["Low"],
        "rsi":          r["RSI"],
        "macd_hist":    r["MACD_hist"],
        "prev_macd_hist": p["MACD_hist"],
        "dma21":        r["DMA21"],
        "dma50":        r["DMA50"],
        "dma200":       r["DMA200"],
        "atr":          r["ATR"],
        "bb_upper":     r["BB_upper"],
        "bb_lower":     r["BB_lower"],
        "st_dir":       r["ST_dir"],
        "prev_st_dir":  p["ST_dir"],
        "supertrend":   r["ST"],
        "support":      r["Support"],
        "resistance":   r["Resistance"],
        "volume":       r["Volume"],
        "vol_sma":      r["Vol_SMA"],
    }
