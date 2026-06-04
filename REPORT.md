# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-06-04 08:34 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹99,447.40 |
| Cash Available | ₹18,072.35 |
| Total P&L | 🔴 ₹-552.60 (-0.55%) |
| Drawdown from Peak | 🟢 0.55% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| KOTAKBANK | 39 | ₹384.20 | ₹371.07 | ₹426.92 | ₹14,983.80 |
| WIPRO | 73 | ₹204.25 | ₹203.56 | ₹227.14 | ₹14,910.25 |
| EICHERMOT | 2 | ₹7177.00 | ₹6944.23 | ₹8129.42 | ₹14,354.00 |
| GRASIM | 4 | ₹3122.40 | ₹3035.81 | ₹3468.30 | ₹12,489.60 |
| BAJAJ-AUTO | 1 | ₹10267.00 | ₹10067.63 | ₹11466.61 | ₹10,267.00 |
| ADANIPORTS | 8 | ₹1796.30 | ₹1710.51 | ₹2010.79 | ₹14,370.40 |

## 📋 Trade History (2 closed | Win rate 50% | Total P&L ₹-552.60)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-06-04 08:34 | 🟢 BUY | ADANIPORTS | 8 | ₹1796.30 | — |  |
| 2026-06-04 08:34 | 🔴 SELL | BAJAJFINSV | 8 | ₹1710.90 | ₹-581.60 | trailing_stop |
| 2026-06-03 08:36 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10267.00 | — |  |
| 2026-06-03 08:36 | 🔴 SELL | TECHM | 10 | ₹1486.80 | ₹+29.00 | trailing_stop |
| 2026-06-01 21:37 | 🟢 BUY | GRASIM | 4 | ₹3122.40 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | EICHERMOT | 2 | ₹7177.00 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | TECHM | 10 | ₹1483.90 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | WIPRO | 73 | ₹204.25 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | BAJAJFINSV | 8 | ₹1783.60 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | KOTAKBANK | 39 | ₹384.20 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*