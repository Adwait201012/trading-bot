# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-21 13:21 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹97,756.07 |
| Cash Available | ₹21,004.57 |
| Total P&L | 🔴 ₹-2,243.93 (-2.24%) |
| Drawdown from Peak | 🟡 2.24% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3190.80 | ₹3112.92 | ₹3523.69 | ₹12,763.20 |
| ADANIPORTS | 8 | ₹1729.10 | ₹1769.28 | ₹1928.19 | ₹13,832.80 |
| KOTAKBANK | 35 | ₹409.80 | ₹405.99 | ₹445.96 | ₹14,343.00 |
| EICHERMOT | 1 | ₹7452.50 | ₹7323.02 | ₹8167.19 | ₹7,452.50 |
| HDFCBANK | 20 | ₹730.50 | ₹719.74 | ₹794.97 | ₹14,610.00 |
| AXISBANK | 11 | ₹1250.00 | ₹1212.50 | ₹1357.14 | ₹13,750.00 |

## 📋 Trade History (51 closed | Win rate 33% | Total P&L ₹-2,243.93)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-09-21 12:48 | 🟢 BUY | AXISBANK | 11 | ₹1250.00 | — |  |
| 2026-09-18 08:30 | 🟢 BUY | HDFCBANK | 20 | ₹730.50 | — |  |
| 2026-09-15 13:33 | 🟢 BUY | EICHERMOT | 1 | ₹7452.50 | — |  |
| 2026-09-15 10:02 | 🟢 BUY | KOTAKBANK | 35 | ₹409.80 | — |  |
| 2026-09-15 10:02 | 🔴 SELL | KOTAKBANK | 36 | ₹409.80 | ₹-522.00 | trailing_stop |
| 2026-09-15 08:58 | 🟢 BUY | ADANIPORTS | 8 | ₹1729.10 | — |  |
| 2026-09-15 08:58 | 🟢 BUY | GRASIM | 4 | ₹3190.80 | — |  |
| 2026-09-15 08:58 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹11425.00 | ₹-339.00 | trailing_stop |
| 2026-09-15 08:58 | 🔴 SELL | BAJAJFINSV | 7 | ₹1862.00 | ₹-492.10 | trailing_stop |
| 2026-09-15 08:58 | 🔴 SELL | ADANIENT | 4 | ₹2937.30 | ₹-654.80 | trailing_stop |
| 2026-09-15 08:58 | 🔴 SELL | ICICIBANK | 10 | ₹1353.20 | ₹-472.00 | trailing_stop |
| 2026-09-15 08:58 | 🔴 SELL | GRASIM | 4 | ₹3190.80 | ₹-408.40 | trailing_stop |
| 2026-09-09 09:12 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹11764.00 | — |  |
| 2026-09-09 09:12 | 🟢 BUY | BAJAJFINSV | 7 | ₹1932.30 | — |  |
| 2026-09-09 09:12 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹11764.00 | ₹-287.00 | trailing_stop |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*