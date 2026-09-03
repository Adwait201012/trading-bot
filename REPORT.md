# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-03 12:15 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹102,715.67 |
| Cash Available | ₹18,951.27 |
| Total P&L | 🟢 ₹+2,715.67 (+2.72%) |
| Drawdown from Peak | 🟢 -2.72% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| ICICIBANK | 11 | ₹1421.40 | ₹1410.38 | ₹1544.08 | ₹15,635.40 |
| TECHM | 9 | ₹1585.00 | ₹1588.86 | ₹1763.97 | ₹14,265.00 |
| BAJAJFINSV | 7 | ₹1964.70 | ₹1932.34 | ₹2154.73 | ₹13,752.90 |
| HCLTECH | 11 | ₹1353.50 | ₹1311.25 | ₹1516.53 | ₹14,888.50 |
| GRASIM | 4 | ₹3292.90 | ₹3221.37 | ₹3629.84 | ₹13,171.60 |
| BAJAJ-AUTO | 1 | ₹12051.00 | ₹11766.10 | ₹13224.17 | ₹12,051.00 |

## 📋 Trade History (38 closed | Win rate 42% | Total P&L ₹+2,715.67)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-09-02 08:48 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹12051.00 | — |  |
| 2026-09-02 08:08 | 🔴 SELL | EICHERMOT | 2 | ₹7612.00 | ₹-52.00 | trailing_stop |
| 2026-09-01 08:55 | 🟢 BUY | GRASIM | 4 | ₹3292.90 | — |  |
| 2026-09-01 08:55 | 🟢 BUY | HCLTECH | 11 | ₹1353.50 | — |  |
| 2026-09-01 08:55 | 🟢 BUY | BAJAJFINSV | 7 | ₹1964.70 | — |  |
| 2026-09-01 08:55 | 🔴 SELL | SBIN | 14 | ₹1031.00 | ₹-252.00 | signal |
| 2026-09-01 08:55 | 🔴 SELL | AXISBANK | 12 | ₹1261.40 | ₹-463.20 | signal |
| 2026-09-01 08:55 | 🔴 SELL | BAJAJFINSV | 7 | ₹1964.70 | ₹-189.00 | trailing_stop |
| 2026-08-31 10:06 | 🟢 BUY | AXISBANK | 12 | ₹1300.00 | — |  |
| 2026-08-31 10:06 | 🔴 SELL | BAJFINANCE | 14 | ₹1057.00 | ₹-543.20 | trailing_stop |
| 2026-08-28 18:42 | 🟢 BUY | TECHM | 9 | ₹1585.00 | — |  |
| 2026-08-28 18:42 | 🔴 SELL | TECHM | 9 | ₹1585.00 | ₹-27.90 | trailing_stop |
| 2026-08-19 04:53 | 🟢 BUY | SBIN | 14 | ₹1049.00 | — |  |
| 2026-08-19 04:53 | 🔴 SELL | SBIN | 14 | ₹1049.00 | ₹-261.80 | trailing_stop |
| 2026-08-18 04:20 | 🟢 BUY | TECHM | 9 | ₹1588.10 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*