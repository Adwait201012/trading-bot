# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-10-14 12:51 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹96,164.97 |
| Cash Available | ₹14,112.22 |
| Total P&L | 🔴 ₹-3,835.03 (-3.84%) |
| Drawdown from Peak | 🟡 3.84% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| ICICIBANK | 10 | ₹1357.50 | ₹1319.39 | ₹1462.34 | ₹13,575.00 |
| KOTAKBANK | 33 | ₹435.00 | ₹430.10 | ₹481.04 | ₹14,355.00 |
| ADANIENT | 5 | ₹2596.00 | ₹2642.86 | ₹3042.31 | ₹12,980.00 |
| ADANIPORTS | 8 | ₹1708.00 | ₹1710.11 | ₹1925.39 | ₹13,664.00 |
| HCLTECH | 10 | ₹1326.00 | ₹1292.82 | ₹1528.29 | ₹13,260.00 |
| INFY | 13 | ₹1093.75 | ₹1058.27 | ₹1238.77 | ₹14,218.75 |

## 📋 Trade History (63 closed | Win rate 32% | Total P&L ₹-3,835.03)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-10-14 09:01 | 🟢 BUY | INFY | 13 | ₹1093.75 | — |  |
| 2026-10-14 09:01 | 🔴 SELL | TCS | 6 | ₹2306.60 | ₹+223.80 | signal |
| 2026-10-13 11:07 | 🟢 BUY | HCLTECH | 10 | ₹1326.00 | — |  |
| 2026-10-13 11:07 | 🟢 BUY | TCS | 6 | ₹2269.30 | — |  |
| 2026-10-08 10:56 | 🟢 BUY | ADANIPORTS | 8 | ₹1708.00 | — |  |
| 2026-10-08 10:56 | 🟢 BUY | ADANIENT | 5 | ₹2596.00 | — |  |
| 2026-10-08 10:56 | 🟢 BUY | KOTAKBANK | 33 | ₹435.00 | — |  |
| 2026-10-08 10:56 | 🔴 SELL | ADANIPORTS | 8 | ₹1708.00 | ₹-528.00 | trailing_stop |
| 2026-10-07 10:35 | 🟢 BUY | ICICIBANK | 10 | ₹1357.50 | — |  |
| 2026-10-07 10:35 | 🔴 SELL | KOTAKBANK | 36 | ₹440.00 | ₹+1296.00 | target |
| 2026-10-05 10:51 | 🟢 BUY | ADANIPORTS | 8 | ₹1774.00 | — |  |
| 2026-10-01 10:28 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹10045.00 | ₹-766.00 | trailing_stop |
| 2026-10-01 10:28 | 🔴 SELL | ADANIPORTS | 8 | ₹1737.80 | ₹-47.20 | trailing_stop |
| 2026-09-29 12:53 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10811.00 | — |  |
| 2026-09-29 10:08 | 🔴 SELL | GRASIM | 4 | ₹3100.00 | ₹-363.20 | trailing_stop |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*