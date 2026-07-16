# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-07-16 11:21 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹99,893.27 |
| Cash Available | ₹18,083.77 |
| Total P&L | 🔴 ₹-106.73 (-0.11%) |
| Drawdown from Peak | 🟢 0.11% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| SBIN | 14 | ₹1016.70 | ₹1007.73 | ₹1108.02 | ₹14,233.80 |
| BAJFINANCE | 14 | ₹1009.00 | ₹1007.44 | ₹1128.51 | ₹14,126.00 |
| ICICIBANK | 10 | ₹1380.30 | ₹1380.02 | ₹1504.73 | ₹13,803.00 |
| INFY | 13 | ₹1101.90 | ₹1069.52 | ₹1273.51 | ₹14,324.70 |
| TECHM | 10 | ₹1496.70 | ₹1481.29 | ₹1719.06 | ₹14,967.00 |
| BAJAJ-AUTO | 1 | ₹10355.00 | ₹10045.32 | ₹11420.52 | ₹10,355.00 |

## 📋 Trade History (19 closed | Win rate 47% | Total P&L ₹-106.73)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-07-16 06:04 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10355.00 | — |  |
| 2026-07-16 06:04 | 🔴 SELL | AXISBANK | 11 | ₹1302.30 | ₹-238.70 | trailing_stop |
| 2026-07-14 06:57 | 🟢 BUY | TECHM | 10 | ₹1496.70 | — |  |
| 2026-07-14 06:57 | 🔴 SELL | TCS | 6 | ₹2186.00 | ₹-78.60 | signal |
| 2026-07-14 05:56 | 🟢 BUY | TCS | 6 | ₹2199.10 | — |  |
| 2026-07-14 05:56 | 🔴 SELL | HCLTECH | 13 | ₹1183.70 | ₹+178.10 | trailing_stop |
| 2026-07-13 09:57 | 🟢 BUY | INFY | 13 | ₹1101.90 | — |  |
| 2026-07-13 09:57 | 🔴 SELL | GRASIM | 4 | ₹3128.80 | ₹+25.60 | trailing_stop |
| 2026-07-08 09:13 | 🟢 BUY | ICICIBANK | 10 | ₹1380.30 | — |  |
| 2026-07-08 09:13 | 🔴 SELL | ICICIBANK | 11 | ₹1380.30 | ₹+631.40 | trailing_stop |
| 2026-07-08 08:44 | 🟢 BUY | BAJFINANCE | 14 | ₹1009.00 | — |  |
| 2026-07-08 08:44 | 🟢 BUY | SBIN | 14 | ₹1016.70 | — |  |
| 2026-07-08 08:44 | 🔴 SELL | BAJFINANCE | 15 | ₹1009.00 | ₹+595.50 | trailing_stop |
| 2026-07-08 08:44 | 🔴 SELL | SBIN | 14 | ₹1016.70 | ₹+83.30 | trailing_stop |
| 2026-07-08 07:16 | 🟢 BUY | AXISBANK | 11 | ₹1324.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*