# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-01 12:01 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹102,767.67 |
| Cash Available | ₹15,778.27 |
| Total P&L | 🟢 ₹+2,767.67 (+2.77%) |
| Drawdown from Peak | 🟢 -2.77% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| EICHERMOT | 2 | ₹7638.00 | ₹7885.61 | ₹8406.00 | ₹15,276.00 |
| ICICIBANK | 11 | ₹1421.40 | ₹1410.38 | ₹1544.08 | ₹15,635.40 |
| TECHM | 9 | ₹1585.00 | ₹1588.86 | ₹1763.97 | ₹14,265.00 |
| BAJAJFINSV | 7 | ₹1964.70 | ₹1912.84 | ₹2154.73 | ₹13,752.90 |
| HCLTECH | 11 | ₹1353.50 | ₹1311.25 | ₹1516.53 | ₹14,888.50 |
| GRASIM | 4 | ₹3292.90 | ₹3205.85 | ₹3629.84 | ₹13,171.60 |

## 📋 Trade History (37 closed | Win rate 43% | Total P&L ₹+2,767.67)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
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
| 2026-08-18 04:20 | 🔴 SELL | TECHM | 9 | ₹1588.10 | ₹-334.80 | trailing_stop |
| 2026-08-12 06:39 | 🟢 BUY | TECHM | 9 | ₹1625.30 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*