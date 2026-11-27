# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-11-27 13:08 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹103,194.04 |
| Cash Available | ₹13,315.74 |
| Total P&L | 🟢 ₹+3,194.04 (+3.19%) |
| Drawdown from Peak | 🟢 -3.19% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| AXISBANK | 11 | ₹1388.60 | ₹1375.56 | ₹1558.95 | ₹15,274.60 |
| TCS | 6 | ₹2517.30 | ₹2495.32 | ₹2868.75 | ₹15,103.80 |
| KOTAKBANK | 31 | ₹500.00 | ₹478.16 | ₹554.60 | ₹15,500.00 |
| BAJAJFINSV | 8 | ₹1849.00 | ₹1750.28 | ₹2095.80 | ₹14,792.00 |
| INFY | 13 | ₹1151.30 | ₹1079.13 | ₹1331.71 | ₹14,966.90 |
| HCLTECH | 10 | ₹1424.10 | ₹1341.90 | ₹1629.60 | ₹14,241.00 |

## 📋 Trade History (89 closed | Win rate 35% | Total P&L ₹+3,194.04)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-11-27 13:08 | 🟢 BUY | HCLTECH | 10 | ₹1424.10 | — |  |
| 2026-11-27 13:08 | 🟢 BUY | INFY | 13 | ₹1151.30 | — |  |
| 2026-11-27 13:08 | 🟢 BUY | BAJAJFINSV | 8 | ₹1849.00 | — |  |
| 2026-11-27 13:08 | 🟢 BUY | KOTAKBANK | 31 | ₹500.00 | — |  |
| 2026-11-27 13:08 | 🔴 SELL | BAJFINANCE | 14 | ₹1080.00 | ₹-217.00 | trailing_stop |
| 2026-11-27 13:08 | 🔴 SELL | BAJAJFINSV | 8 | ₹1849.00 | ₹-248.80 | trailing_stop |
| 2026-11-27 13:08 | 🔴 SELL | KOTAKBANK | 31 | ₹500.00 | ₹+354.95 | trailing_stop |
| 2026-11-27 13:08 | 🔴 SELL | SBIN | 14 | ₹1123.90 | ₹+877.80 | trailing_stop |
| 2026-11-26 18:37 | 🟢 BUY | TCS | 6 | ₹2517.30 | — |  |
| 2026-11-26 18:37 | 🔴 SELL | TCS | 6 | ₹2517.30 | ₹+343.80 | trailing_stop |
| 2026-11-25 18:38 | 🟢 BUY | BAJFINANCE | 14 | ₹1095.50 | — |  |
| 2026-11-25 18:38 | 🔴 SELL | BAJFINANCE | 13 | ₹1095.50 | ₹-332.80 | trailing_stop |
| 2026-11-24 14:17 | 🟢 BUY | TCS | 6 | ₹2460.00 | — |  |
| 2026-11-24 14:17 | 🟢 BUY | BAJAJFINSV | 8 | ₹1880.10 | — |  |
| 2026-11-24 14:17 | 🟢 BUY | AXISBANK | 11 | ₹1388.60 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*