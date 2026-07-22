# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-07-22 09:14 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹99,448.77 |
| Cash Available | ₹18,924.77 |
| Total P&L | 🔴 ₹-551.23 (-0.55%) |
| Drawdown from Peak | 🟢 0.55% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| BAJFINANCE | 14 | ₹1009.00 | ₹1037.12 | ₹1128.51 | ₹14,126.00 |
| ICICIBANK | 10 | ₹1380.30 | ₹1421.63 | ₹1504.73 | ₹13,803.00 |
| TECHM | 10 | ₹1496.70 | ₹1539.58 | ₹1719.06 | ₹14,967.00 |
| BAJAJ-AUTO | 1 | ₹10355.00 | ₹10628.29 | ₹11420.52 | ₹10,355.00 |
| EICHERMOT | 2 | ₹7638.00 | ₹7397.22 | ₹8406.00 | ₹15,276.00 |
| ULTRACEMCO | 1 | ₹11997.00 | ₹11631.27 | ₹13095.66 | ₹11,997.00 |

## 📋 Trade History (21 closed | Win rate 48% | Total P&L ₹-551.23)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-07-22 06:14 | 🟢 BUY | ULTRACEMCO | 1 | ₹11997.00 | — |  |
| 2026-07-22 06:14 | 🟢 BUY | EICHERMOT | 2 | ₹7638.00 | — |  |
| 2026-07-22 06:14 | 🔴 SELL | INFY | 13 | ₹1059.20 | ₹-555.10 | trailing_stop |
| 2026-07-22 06:14 | 🔴 SELL | SBIN | 14 | ₹1024.60 | ₹+110.60 | trailing_stop |
| 2026-07-16 06:04 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10355.00 | — |  |
| 2026-07-16 06:04 | 🔴 SELL | AXISBANK | 11 | ₹1302.30 | ₹-238.70 | trailing_stop |
| 2026-07-14 06:57 | 🟢 BUY | TECHM | 10 | ₹1496.70 | — |  |
| 2026-07-14 06:57 | 🔴 SELL | TCS | 6 | ₹2186.00 | ₹-78.60 | signal |
| 2026-07-14 05:56 | 🟢 BUY | TCS | 6 | ₹2199.10 | — |  |
| 2026-07-14 05:56 | 🔴 SELL | HCLTECH | 13 | ₹1183.70 | ₹+178.10 | trailing_stop |
| 2026-07-13 09:57 | 🟢 BUY | INFY | 13 | ₹1101.90 | — |  |
| 2026-07-13 09:57 | 🔴 SELL | GRASIM | 4 | ₹3128.80 | ₹+25.60 | trailing_stop |
| 2026-07-08 09:13 | 🟢 BUY | ICICIBANK | 10 | ₹1380.30 | — |  |
| 2026-07-08 09:13 | 🔴 SELL | ICICIBANK | 11 | ₹1380.30 | ₹+631.40 | trailing_stop |
| 2026-07-08 08:44 | 🟢 BUY | BAJFINANCE | 14 | ₹1009.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*