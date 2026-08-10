# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-08-10 10:00 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹104,251.17 |
| Cash Available | ₹18,220.37 |
| Total P&L | 🟢 ₹+4,251.17 (+4.25%) |
| Drawdown from Peak | 🟢 -4.25% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| EICHERMOT | 2 | ₹7638.00 | ₹7808.50 | ₹8406.00 | ₹15,276.00 |
| ULTRACEMCO | 1 | ₹11997.00 | ₹11824.30 | ₹13095.66 | ₹11,997.00 |
| TECHM | 9 | ₹1537.70 | ₹1630.76 | ₹1763.00 | ₹13,839.30 |
| BAJFINANCE | 14 | ₹1095.80 | ₹1071.85 | ₹1247.64 | ₹15,341.20 |
| BAJAJFINSV | 7 | ₹1991.70 | ₹1971.72 | ₹2239.91 | ₹13,941.90 |
| ICICIBANK | 11 | ₹1421.40 | ₹1385.35 | ₹1544.08 | ₹15,635.40 |

## 📋 Trade History (28 closed | Win rate 54% | Total P&L ₹+4,251.17)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-08-07 09:14 | 🟢 BUY | ICICIBANK | 11 | ₹1421.40 | — |  |
| 2026-08-07 09:14 | 🔴 SELL | ICICIBANK | 10 | ₹1421.40 | ₹+411.00 | trailing_stop |
| 2026-08-07 08:20 | 🟢 BUY | BAJAJFINSV | 7 | ₹1991.70 | — |  |
| 2026-08-07 08:20 | 🔴 SELL | SBIN | 15 | ₹1114.90 | ₹+1507.50 | target |
| 2026-08-07 05:23 | 🟢 BUY | BAJFINANCE | 14 | ₹1095.80 | — |  |
| 2026-08-07 05:23 | 🔴 SELL | BAJFINANCE | 13 | ₹1095.80 | ₹-465.40 | trailing_stop |
| 2026-07-31 06:32 | 🟢 BUY | BAJFINANCE | 13 | ₹1131.60 | — |  |
| 2026-07-31 06:32 | 🔴 SELL | BAJFINANCE | 15 | ₹1131.60 | ₹+1866.00 | target |
| 2026-07-29 06:18 | 🟢 BUY | SBIN | 15 | ₹1014.40 | — |  |
| 2026-07-29 06:18 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹11453.50 | ₹+1098.50 | target |
| 2026-07-24 06:40 | 🟢 BUY | TECHM | 9 | ₹1537.70 | — |  |
| 2026-07-24 06:40 | 🔴 SELL | TECHM | 10 | ₹1537.70 | ₹+410.00 | trailing_stop |
| 2026-07-24 06:13 | 🟢 BUY | BAJFINANCE | 15 | ₹1007.20 | — |  |
| 2026-07-24 06:13 | 🔴 SELL | BAJFINANCE | 14 | ₹1007.20 | ₹-25.20 | trailing_stop |
| 2026-07-22 06:14 | 🟢 BUY | ULTRACEMCO | 1 | ₹11997.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*