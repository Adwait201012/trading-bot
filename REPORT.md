# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-07-08 07:40 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹98,696.67 |
| Cash Available | ₹13,191.17 |
| Total P&L | 🔴 ₹-1,303.33 (-1.30%) |
| Drawdown from Peak | 🟢 1.30% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3122.40 | ₹3116.61 | ₹3468.30 | ₹12,489.60 |
| ICICIBANK | 11 | ₹1322.90 | ₹1384.48 | ₹1455.98 | ₹14,551.90 |
| SBIN | 14 | ₹1010.75 | ₹1021.22 | ₹1116.17 | ₹14,150.50 |
| BAJFINANCE | 15 | ₹969.30 | ₹1011.32 | ₹1076.94 | ₹14,539.50 |
| HCLTECH | 13 | ₹1170.00 | ₹1133.15 | ₹1343.17 | ₹15,210.00 |
| AXISBANK | 11 | ₹1324.00 | ₹1296.21 | ₹1455.20 | ₹14,564.00 |

## 📋 Trade History (12 closed | Win rate 33% | Total P&L ₹-1,303.33)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-07-08 07:16 | 🟢 BUY | AXISBANK | 11 | ₹1324.00 | — |  |
| 2026-07-08 07:16 | 🔴 SELL | AXISBANK | 11 | ₹1324.00 | ₹-388.30 | trailing_stop |
| 2026-07-07 10:00 | 🟢 BUY | HCLTECH | 13 | ₹1170.00 | — |  |
| 2026-07-07 10:00 | 🔴 SELL | ADANIENT | 5 | ₹3109.90 | ₹+613.00 | trailing_stop |
| 2026-06-30 07:38 | 🟢 BUY | AXISBANK | 11 | ₹1359.30 | — |  |
| 2026-06-30 07:38 | 🔴 SELL | EICHERMOT | 2 | ₹7133.00 | ₹-567.00 | trailing_stop |
| 2026-06-29 08:35 | 🟢 BUY | ADANIENT | 5 | ₹2987.30 | — |  |
| 2026-06-29 08:35 | 🟢 BUY | EICHERMOT | 2 | ₹7416.50 | — |  |
| 2026-06-29 08:35 | 🔴 SELL | EICHERMOT | 2 | ₹7416.50 | ₹+479.00 | trailing_stop |
| 2026-06-29 08:35 | 🔴 SELL | KOTAKBANK | 39 | ₹395.75 | ₹+450.45 | trailing_stop |
| 2026-06-23 07:05 | 🟢 BUY | BAJFINANCE | 15 | ₹969.30 | — |  |
| 2026-06-23 07:05 | 🔴 SELL | ADANIPORTS | 8 | ₹1788.10 | ₹-65.60 | trailing_stop |
| 2026-06-12 08:12 | 🟢 BUY | SBIN | 14 | ₹1010.75 | — |  |
| 2026-06-12 08:12 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹10076.00 | ₹-191.00 | trailing_stop |
| 2026-06-11 08:24 | 🟢 BUY | ICICIBANK | 11 | ₹1322.90 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*