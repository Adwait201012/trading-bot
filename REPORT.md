# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-07-08 08:44 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹99,375.47 |
| Cash Available | ₹14,200.17 |
| Total P&L | 🔴 ₹-624.53 (-0.62%) |
| Drawdown from Peak | 🟢 0.62% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3122.40 | ₹3116.61 | ₹3468.30 | ₹12,489.60 |
| ICICIBANK | 11 | ₹1322.90 | ₹1384.48 | ₹1455.98 | ₹14,551.90 |
| HCLTECH | 13 | ₹1170.00 | ₹1133.15 | ₹1343.17 | ₹15,210.00 |
| AXISBANK | 11 | ₹1324.00 | ₹1296.21 | ₹1455.20 | ₹14,564.00 |
| SBIN | 14 | ₹1016.70 | ₹980.17 | ₹1108.02 | ₹14,233.80 |
| BAJFINANCE | 14 | ₹1009.00 | ₹961.19 | ₹1128.51 | ₹14,126.00 |

## 📋 Trade History (14 closed | Win rate 43% | Total P&L ₹-624.53)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
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
| 2026-06-29 08:35 | 🔴 SELL | KOTAKBANK | 39 | ₹395.75 | ₹+450.45 | trailing_stop |
| 2026-06-23 07:05 | 🟢 BUY | BAJFINANCE | 15 | ₹969.30 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*