"""
Central configuration — change parameters here, nowhere else.
All risk parameters are clearly marked. Read the WARNING comments.
"""
from dotenv import load_dotenv
import os

load_dotenv()

# ─── Broker API (fill in when ready for live trading) ───────────────────────
DHAN_CLIENT_ID    = os.getenv("DHAN_CLIENT_ID", "")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN", "")
DATA_API          = "yfinance"   # Options: "yfinance" | "dhan" | "upstox"

# ─── Universe ────────────────────────────────────────────────────────────────
INDICES = ["^NSEI", "^NSEBANK"]   # Nifty 50, Bank Nifty (for context only)

WATCHLIST = {
    "financials": ["HDFCBANK.NS", "ICICIBANK.NS", "AXISBANK.NS", "KOTAKBANK.NS",
                   "SBIN.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS"],
    "it":         ["TCS.NS", "INFY.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS"],
    "auto":       ["MARUTI.NS", "MAHINDRA.NS", "EICHERMOT.NS", "BAJAJ-AUTO.NS"],
    "cement":     ["ULTRACEMCO.NS", "GRASIM.NS", "SHREECEM.NS"],
    "midcap":     ["ADANIENT.NS", "ADANIPORTS.NS", "POLYCAB.NS", "CUMMINSIND.NS"],
}
ALL_STOCKS = [s for sector in WATCHLIST.values() for s in sector]

# ─── Capital & Position Sizing ───────────────────────────────────────────────
STARTING_CAPITAL     = 100_000   # INR — paper trading only

# WARNING: These control how much of your capital is at risk per trade.
# Higher = more aggressive = bigger losses possible.
RISK_PER_TRADE_PCT   = 0.02      # Risk 2% of portfolio per trade (via stop loss)
MAX_POSITION_PCT     = 0.15      # No single stock > 15% of portfolio
MAX_OPEN_POSITIONS   = 6         # Max concurrent positions
SCALE_IN_TRANCHES    = 2         # Buy in 2 tranches (50% each near support)

# ─── Risk Circuit Breakers ───────────────────────────────────────────────────
# WARNING: If portfolio drops this much from peak, ALL new trades are blocked.
MAX_PORTFOLIO_DRAWDOWN = 0.12    # 12% drawdown = halt new trades
DAILY_LOSS_LIMIT       = 0.03    # Stop trading if down 3% on the day

# ─── Stop Loss & Targets (ATR-based) ─────────────────────────────────────────
ATR_PERIOD           = 14
ATR_STOP_MULTIPLIER  = 2.0       # Stop = entry - 2 * ATR
ATR_TRAIL_MULTIPLIER = 1.5       # Trailing stop = high - 1.5 * ATR
FIXED_TARGET_RR      = 2.5       # Target = risk * 2.5 (risk:reward)

# ─── Technical Indicators ────────────────────────────────────────────────────
RSI_PERIOD           = 14
RSI_OVERSOLD         = 40        # Aggressive: buy above 40 (not just 30)
RSI_OVERBOUGHT       = 65
MACD_FAST            = 12
MACD_SLOW            = 26
MACD_SIGNAL          = 9
DMA_SHORT            = 21        # 21-day moving average
DMA_MID              = 50
DMA_LONG             = 200
SUPERTREND_PERIOD    = 10
SUPERTREND_MULT      = 3.0
SUPPORT_WINDOW       = 10        # Swing high/low window for S/R levels
SIGNAL_MIN_SCORE     = 3         # Minimum score to trigger BUY/SELL

# ─── Data ────────────────────────────────────────────────────────────────────
BACKTEST_PERIOD      = "5y"      # 5 years for backtesting
LIVE_PERIOD          = "1y"      # 1 year — needed for 200 DMA
DATA_INTERVAL        = "1d"      # Daily candles

# ─── Market Hours (IST) ──────────────────────────────────────────────────────
MARKET_OPEN_HOUR     = 9
MARKET_OPEN_MIN      = 15
MARKET_CLOSE_HOUR    = 15
MARKET_CLOSE_MIN     = 30
