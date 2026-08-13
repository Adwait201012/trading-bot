# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-08-13 06:06 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹104,839.57 |
| Cash Available | ₹15,069.57 |
| Total P&L | 🟢 ₹+4,839.57 (+4.84%) |
| Drawdown from Peak | 🟢 -4.84% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| EICHERMOT | 2 | ₹7638.00 | ₹7832.27 | ₹8406.00 | ₹15,276.00 |
| BAJFINANCE | 14 | ₹1095.80 | ₹1071.85 | ₹1247.64 | ₹15,341.20 |
| BAJAJFINSV | 7 | ₹1991.70 | ₹1976.38 | ₹2239.91 | ₹13,941.90 |
| ICICIBANK | 11 | ₹1421.40 | ₹1388.85 | ₹1544.08 | ₹15,635.40 |
| SBIN | 14 | ₹1067.70 | ₹1050.99 | ₹1177.43 | ₹14,947.80 |
| TECHM | 9 | ₹1625.30 | ₹1590.80 | ₹1824.68 | ₹14,627.70 |

## 📋 Trade History (30 closed | Win rate 53% | Total P&L ₹+4,839.57)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-08-12 06:39 | 🟢 BUY | TECHM | 9 | ₹1625.30 | — |  |
| 2026-08-12 06:39 | 🔴 SELL | TECHM | 9 | ₹1625.30 | ₹+788.40 | trailing_stop |
| 2026-08-11 06:01 | 🟢 BUY | SBIN | 14 | ₹1067.70 | — |  |
| 2026-08-11 06:01 | 🔴 SELL | ULTRACEMCO | 1 | ₹11797.00 | ₹-200.00 | trailing_stop |
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

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*