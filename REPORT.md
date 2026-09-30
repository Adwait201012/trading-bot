# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-30 13:00 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹95,986.37 |
| Cash Available | ₹56,681.77 |
| Total P&L | 🔴 ₹-4,013.63 (-4.01%) |
| Drawdown from Peak | 🟡 4.01% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| KOTAKBANK | 36 | ₹404.00 | ₹404.49 | ₹438.69 | ₹14,544.00 |
| ADANIPORTS | 8 | ₹1743.70 | ₹1767.34 | ₹1934.92 | ₹13,949.60 |
| BAJAJ-AUTO | 1 | ₹10811.00 | ₹10572.03 | ₹11805.70 | ₹10,811.00 |

## 📋 Trade History (58 closed | Win rate 31% | Total P&L ₹-4,013.63)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-09-29 12:53 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10811.00 | — |  |
| 2026-09-29 10:08 | 🔴 SELL | GRASIM | 4 | ₹3100.00 | ₹-363.20 | trailing_stop |
| 2026-09-28 10:10 | 🟢 BUY | ADANIPORTS | 8 | ₹1743.70 | — |  |
| 2026-09-28 10:10 | 🔴 SELL | HDFCBANK | 20 | ₹719.05 | ₹-229.00 | trailing_stop |
| 2026-09-28 10:10 | 🔴 SELL | EICHERMOT | 1 | ₹7213.50 | ₹-239.00 | trailing_stop |
| 2026-09-28 10:10 | 🔴 SELL | ADANIPORTS | 8 | ₹1743.70 | ₹+116.80 | trailing_stop |
| 2026-09-25 10:09 | 🟢 BUY | KOTAKBANK | 36 | ₹404.00 | — |  |
| 2026-09-25 09:38 | 🔴 SELL | KOTAKBANK | 35 | ₹401.90 | ₹-117.25 | signal |
| 2026-09-24 09:57 | 🟢 BUY | KOTAKBANK | 35 | ₹405.25 | — |  |
| 2026-09-24 09:57 | 🔴 SELL | KOTAKBANK | 35 | ₹405.25 | ₹-159.25 | trailing_stop |
| 2026-09-24 08:45 | 🔴 SELL | AXISBANK | 11 | ₹1179.20 | ₹-778.80 | trailing_stop |
| 2026-09-21 12:48 | 🟢 BUY | AXISBANK | 11 | ₹1250.00 | — |  |
| 2026-09-18 08:30 | 🟢 BUY | HDFCBANK | 20 | ₹730.50 | — |  |
| 2026-09-15 13:33 | 🟢 BUY | EICHERMOT | 1 | ₹7452.50 | — |  |
| 2026-09-15 10:02 | 🟢 BUY | KOTAKBANK | 35 | ₹409.80 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*