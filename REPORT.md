# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-10-23 13:47 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹96,449.72 |
| Cash Available | ₹15,193.42 |
| Total P&L | 🔴 ₹-3,550.28 (-3.55%) |
| Drawdown from Peak | 🟡 3.55% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| ICICIBANK | 10 | ₹1357.50 | ₹1356.55 | ₹1462.34 | ₹13,575.00 |
| HCLTECH | 10 | ₹1326.00 | ₹1382.83 | ₹1528.29 | ₹13,260.00 |
| TCS | 5 | ₹2506.90 | ₹2460.41 | ₹2871.15 | ₹12,534.50 |
| INFY | 12 | ₹1160.50 | ₹1125.54 | ₹1368.51 | ₹13,926.00 |
| ADANIPORTS | 8 | ₹1706.10 | ₹1653.27 | ₹1934.69 | ₹13,648.80 |
| TECHM | 8 | ₹1789.00 | ₹1736.30 | ₹2054.83 | ₹14,312.00 |

## 📋 Trade History (68 closed | Win rate 31% | Total P&L ₹-3,550.28)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-10-23 09:36 | 🟢 BUY | TECHM | 8 | ₹1789.00 | — |  |
| 2026-10-23 08:50 | 🟢 BUY | ADANIPORTS | 8 | ₹1706.10 | — |  |
| 2026-10-23 08:50 | 🟢 BUY | INFY | 12 | ₹1160.50 | — |  |
| 2026-10-23 08:50 | 🔴 SELL | ADANIPORTS | 8 | ₹1706.10 | ₹-15.20 | trailing_stop |
| 2026-10-23 08:50 | 🔴 SELL | KOTAKBANK | 33 | ₹430.70 | ₹-141.90 | trailing_stop |
| 2026-10-22 10:39 | 🟢 BUY | TCS | 5 | ₹2506.90 | — |  |
| 2026-10-21 08:53 | 🔴 SELL | EICHERMOT | 2 | ₹7101.00 | ₹-367.00 | trailing_stop |
| 2026-10-21 08:53 | 🔴 SELL | ADANIENT | 5 | ₹2582.40 | ₹-68.00 | trailing_stop |
| 2026-10-16 11:54 | 🟢 BUY | EICHERMOT | 2 | ₹7284.50 | — |  |
| 2026-10-16 11:54 | 🔴 SELL | INFY | 13 | ₹1161.20 | ₹+876.85 | signal |
| 2026-10-14 09:01 | 🟢 BUY | INFY | 13 | ₹1093.75 | — |  |
| 2026-10-14 09:01 | 🔴 SELL | TCS | 6 | ₹2306.60 | ₹+223.80 | signal |
| 2026-10-13 11:07 | 🟢 BUY | HCLTECH | 10 | ₹1326.00 | — |  |
| 2026-10-13 11:07 | 🟢 BUY | TCS | 6 | ₹2269.30 | — |  |
| 2026-10-08 10:56 | 🟢 BUY | ADANIPORTS | 8 | ₹1708.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*