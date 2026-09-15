# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-15 09:36 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹98,278.07 |
| Cash Available | ₹56,407.27 |
| Total P&L | 🔴 ₹-1,721.93 (-1.72%) |
| Drawdown from Peak | 🟢 1.72% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| KOTAKBANK | 36 | ₹424.30 | ₹412.01 | ₹460.58 | ₹15,274.80 |
| GRASIM | 4 | ₹3190.80 | ₹3087.03 | ₹3523.69 | ₹12,763.20 |
| ADANIPORTS | 8 | ₹1729.10 | ₹1676.84 | ₹1928.19 | ₹13,832.80 |

## 📋 Trade History (50 closed | Win rate 34% | Total P&L ₹-1,721.93)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
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
| 2026-09-09 09:12 | 🔴 SELL | BAJAJFINSV | 7 | ₹1932.30 | ₹-226.80 | trailing_stop |
| 2026-09-09 08:23 | 🟢 BUY | ADANIENT | 4 | ₹3101.00 | — |  |
| 2026-09-09 08:23 | 🔴 SELL | TECHM | 9 | ₹1503.00 | ₹-383.40 | trailing_stop |
| 2026-09-08 09:37 | 🟢 BUY | TECHM | 9 | ₹1545.60 | — |  |
| 2026-09-08 09:37 | 🔴 SELL | TECHM | 9 | ₹1545.60 | ₹-387.90 | trailing_stop |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*