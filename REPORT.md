# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-08-05 10:45 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹102,798.07 |
| Cash Available | ₹17,955.97 |
| Total P&L | 🟢 ₹+2,798.07 (+2.80%) |
| Drawdown from Peak | 🟢 -2.80% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| ICICIBANK | 10 | ₹1380.30 | ₹1421.63 | ₹1504.73 | ₹13,803.00 |
| EICHERMOT | 2 | ₹7638.00 | ₹7808.50 | ₹8406.00 | ₹15,276.00 |
| ULTRACEMCO | 1 | ₹11997.00 | ₹11824.30 | ₹13095.66 | ₹11,997.00 |
| TECHM | 9 | ₹1537.70 | ₹1630.76 | ₹1763.00 | ₹13,839.30 |
| SBIN | 15 | ₹1014.40 | ₹1023.35 | ₹1103.71 | ₹15,216.00 |
| BAJFINANCE | 13 | ₹1131.60 | ₹1124.13 | ₹1273.82 | ₹14,710.80 |

## 📋 Trade History (25 closed | Win rate 52% | Total P&L ₹+2,798.07)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-07-31 06:32 | 🟢 BUY | BAJFINANCE | 13 | ₹1131.60 | — |  |
| 2026-07-31 06:32 | 🔴 SELL | BAJFINANCE | 15 | ₹1131.60 | ₹+1866.00 | target |
| 2026-07-29 06:18 | 🟢 BUY | SBIN | 15 | ₹1014.40 | — |  |
| 2026-07-29 06:18 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹11453.50 | ₹+1098.50 | target |
| 2026-07-24 06:40 | 🟢 BUY | TECHM | 9 | ₹1537.70 | — |  |
| 2026-07-24 06:40 | 🔴 SELL | TECHM | 10 | ₹1537.70 | ₹+410.00 | trailing_stop |
| 2026-07-24 06:13 | 🟢 BUY | BAJFINANCE | 15 | ₹1007.20 | — |  |
| 2026-07-24 06:13 | 🔴 SELL | BAJFINANCE | 14 | ₹1007.20 | ₹-25.20 | trailing_stop |
| 2026-07-22 06:14 | 🟢 BUY | ULTRACEMCO | 1 | ₹11997.00 | — |  |
| 2026-07-22 06:14 | 🟢 BUY | EICHERMOT | 2 | ₹7638.00 | — |  |
| 2026-07-22 06:14 | 🔴 SELL | INFY | 13 | ₹1059.20 | ₹-555.10 | trailing_stop |
| 2026-07-22 06:14 | 🔴 SELL | SBIN | 14 | ₹1024.60 | ₹+110.60 | trailing_stop |
| 2026-07-16 06:04 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10355.00 | — |  |
| 2026-07-16 06:04 | 🔴 SELL | AXISBANK | 11 | ₹1302.30 | ₹-238.70 | trailing_stop |
| 2026-07-14 06:57 | 🟢 BUY | TECHM | 10 | ₹1496.70 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*