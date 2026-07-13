# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-07-13 09:47 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹100,006.87 |
| Cash Available | ₹15,580.47 |
| Total P&L | 🟢 ₹+6.87 (+0.01%) |
| Drawdown from Peak | 🟢 -0.01% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3122.40 | ₹3138.73 | ₹3468.30 | ₹12,489.60 |
| HCLTECH | 13 | ₹1170.00 | ₹1195.53 | ₹1343.17 | ₹15,210.00 |
| AXISBANK | 11 | ₹1324.00 | ₹1296.21 | ₹1455.20 | ₹14,564.00 |
| SBIN | 14 | ₹1016.70 | ₹1007.73 | ₹1108.02 | ₹14,233.80 |
| BAJFINANCE | 14 | ₹1009.00 | ₹992.21 | ₹1128.51 | ₹14,126.00 |
| ICICIBANK | 10 | ₹1380.30 | ₹1367.02 | ₹1504.73 | ₹13,803.00 |

## 📋 Trade History (15 closed | Win rate 47% | Total P&L ₹+6.87)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-07-08 09:13 | 🟢 BUY | ICICIBANK | 10 | ₹1380.30 | — |  |
| 2026-07-08 09:13 | 🔴 SELL | ICICIBANK | 11 | ₹1380.30 | ₹+631.40 | trailing_stop |
| 2026-07-08 08:44 | 🟢 BUY | BAJFINANCE | 14 | ₹1009.00 | — |  |
| 2026-07-08 08:44 | 🟢 BUY | SBIN | 14 | ₹1016.70 | — |  |
| 2026-07-08 08:44 | 🔴 SELL | BAJFINANCE | 15 | ₹1009.00 | ₹+595.50 | trailing_stop |
| 2026-07-08 08:44 | 🔴 SELL | SBIN | 14 | ₹1016.70 | ₹+83.30 | trailing_stop |
| 2026-07-08 07:16 | 🟢 BUY | AXISBANK | 11 | ₹1324.00 | — |  |
| 2026-07-08 07:16 | 🔴 SELL | AXISBANK | 11 | ₹1324.00 | ₹-388.30 | trailing_stop |
| 2026-07-07 10:00 | 🟢 BUY | HCLTECH | 13 | ₹1170.00 | — |  |
| 2026-07-07 10:00 | 🔴 SELL | ADANIENT | 5 | ₹3109.90 | ₹+613.00 | trailing_stop |
| 2026-06-30 07:38 | 🟢 BUY | AXISBANK | 11 | ₹1359.30 | — |  |
| 2026-06-30 07:38 | 🔴 SELL | EICHERMOT | 2 | ₹7133.00 | ₹-567.00 | trailing_stop |
| 2026-06-29 08:35 | 🟢 BUY | ADANIENT | 5 | ₹2987.30 | — |  |
| 2026-06-29 08:35 | 🟢 BUY | EICHERMOT | 2 | ₹7416.50 | — |  |
| 2026-06-29 08:35 | 🔴 SELL | EICHERMOT | 2 | ₹7416.50 | ₹+479.00 | trailing_stop |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*