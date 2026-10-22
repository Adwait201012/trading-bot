# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-10-22 08:55 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹96,606.82 |
| Cash Available | ₹41,752.82 |
| Total P&L | 🔴 ₹-3,393.18 (-3.39%) |
| Drawdown from Peak | 🟡 3.39% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| ICICIBANK | 10 | ₹1357.50 | ₹1355.09 | ₹1462.34 | ₹13,575.00 |
| KOTAKBANK | 33 | ₹435.00 | ₹434.71 | ₹481.04 | ₹14,355.00 |
| ADANIPORTS | 8 | ₹1708.00 | ₹1713.02 | ₹1925.39 | ₹13,664.00 |
| HCLTECH | 10 | ₹1326.00 | ₹1381.47 | ₹1528.29 | ₹13,260.00 |

## 📋 Trade History (66 closed | Win rate 32% | Total P&L ₹-3,393.18)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-10-21 08:53 | 🔴 SELL | EICHERMOT | 2 | ₹7101.00 | ₹-367.00 | trailing_stop |
| 2026-10-21 08:53 | 🔴 SELL | ADANIENT | 5 | ₹2582.40 | ₹-68.00 | trailing_stop |
| 2026-10-16 11:54 | 🟢 BUY | EICHERMOT | 2 | ₹7284.50 | — |  |
| 2026-10-16 11:54 | 🔴 SELL | INFY | 13 | ₹1161.20 | ₹+876.85 | signal |
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

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*