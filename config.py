from dotenv import load_dotenv
import os

load_dotenv()

# --- Dhan API (for future real trading) ---
DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID", "")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN", "")

# --- Watchlist: NSE stocks to monitor ---
WATCHLIST = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "HINDUNILVR.NS",
    "SBIN.NS",
    "BAJFINANCE.NS",
    "WIPRO.NS",
    "AXISBANK.NS",
]

# --- Paper trading settings ---
STARTING_CAPITAL = 100000       # INR
MAX_POSITION_SIZE = 0.10        # Max 10% of capital per stock
STOP_LOSS_PCT = 0.03            # 3% stop loss
TARGET_PCT = 0.06               # 6% target
MAX_OPEN_POSITIONS = 5

# --- Strategy thresholds ---
RSI_OVERSOLD = 45
RSI_OVERBOUGHT = 60
RSI_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
SMA_SHORT = 20
SMA_LONG = 50

# --- Data ---
DATA_INTERVAL = "1d"            # Daily candles
DATA_PERIOD = "6mo"             # 6 months of history
