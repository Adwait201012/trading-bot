# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-08 09:37 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹101,541.57 |
| Cash Available | ₹19,376.87 |
| Total P&L | 🟢 ₹+1,541.57 (+1.54%) |
| Drawdown from Peak | 🟢 -1.54% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| BAJAJFINSV | 7 | ₹1964.70 | ₹1932.34 | ₹2154.73 | ₹13,752.90 |
| GRASIM | 4 | ₹3292.90 | ₹3224.86 | ₹3629.84 | ₹13,171.60 |
| BAJAJ-AUTO | 1 | ₹12051.00 | ₹11766.10 | ₹13224.17 | ₹12,051.00 |
| KOTAKBANK | 36 | ₹424.30 | ₹412.01 | ₹460.58 | ₹15,274.80 |
| ICICIBANK | 10 | ₹1400.40 | ₹1359.45 | ₹1510.21 | ₹14,004.00 |
| TECHM | 9 | ₹1545.60 | ₹1471.98 | ₹1729.66 | ₹13,910.40 |

## 📋 Trade History (42 closed | Win rate 40% | Total P&L ₹+1,541.57)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-09-08 09:37 | 🟢 BUY | TECHM | 9 | ₹1545.60 | — |  |
| 2026-09-08 09:37 | 🔴 SELL | TECHM | 9 | ₹1545.60 | ₹-387.90 | trailing_stop |
| 2026-09-08 08:20 | 🟢 BUY | ICICIBANK | 10 | ₹1400.40 | — |  |
| 2026-09-08 08:20 | 🔴 SELL | ICICIBANK | 11 | ₹1400.40 | ₹-231.00 | trailing_stop |
| 2026-09-04 09:04 | 🟢 BUY | TECHM | 9 | ₹1588.70 | — |  |
| 2026-09-04 09:04 | 🔴 SELL | TECHM | 9 | ₹1588.70 | ₹+33.30 | trailing_stop |
| 2026-09-04 08:14 | 🟢 BUY | KOTAKBANK | 36 | ₹424.30 | — |  |
| 2026-09-04 08:14 | 🔴 SELL | HCLTECH | 11 | ₹1300.00 | ₹-588.50 | trailing_stop |
| 2026-09-02 08:48 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹12051.00 | — |  |
| 2026-09-02 08:08 | 🔴 SELL | EICHERMOT | 2 | ₹7612.00 | ₹-52.00 | trailing_stop |
| 2026-09-01 08:55 | 🟢 BUY | GRASIM | 4 | ₹3292.90 | — |  |
| 2026-09-01 08:55 | 🟢 BUY | HCLTECH | 11 | ₹1353.50 | — |  |
| 2026-09-01 08:55 | 🟢 BUY | BAJAJFINSV | 7 | ₹1964.70 | — |  |
| 2026-09-01 08:55 | 🔴 SELL | SBIN | 14 | ₹1031.00 | ₹-252.00 | signal |
| 2026-09-01 08:55 | 🔴 SELL | AXISBANK | 12 | ₹1261.40 | ₹-463.20 | signal |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*