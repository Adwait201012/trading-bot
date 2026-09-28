# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-28 10:57 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹96,349.57 |
| Cash Available | ₹55,092.77 |
| Total P&L | 🔴 ₹-3,650.43 (-3.65%) |
| Drawdown from Peak | 🟡 3.65% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3190.80 | ₹3112.92 | ₹3523.69 | ₹12,763.20 |
| KOTAKBANK | 36 | ₹404.00 | ₹391.88 | ₹438.69 | ₹14,544.00 |
| ADANIPORTS | 8 | ₹1743.70 | ₹1691.39 | ₹1934.92 | ₹13,949.60 |

## 📋 Trade History (57 closed | Win rate 32% | Total P&L ₹-3,650.43)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
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
| 2026-09-15 10:02 | 🔴 SELL | KOTAKBANK | 36 | ₹409.80 | ₹-522.00 | trailing_stop |
| 2026-09-15 08:58 | 🟢 BUY | ADANIPORTS | 8 | ₹1729.10 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*