# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-11-26 13:56 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹102,083.29 |
| Cash Available | ₹11,669.04 |
| Total P&L | 🟢 ₹+2,083.29 (+2.08%) |
| Drawdown from Peak | 🟢 -2.08% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| SBIN | 14 | ₹1061.20 | ₹1130.15 | ₹1176.81 | ₹14,856.80 |
| KOTAKBANK | 31 | ₹488.55 | ₹500.33 | ₹539.65 | ₹15,145.05 |
| AXISBANK | 11 | ₹1388.60 | ₹1375.56 | ₹1558.95 | ₹15,274.60 |
| BAJAJFINSV | 8 | ₹1880.10 | ₹1867.25 | ₹2099.18 | ₹15,040.80 |
| TCS | 6 | ₹2460.00 | ₹2561.09 | ₹2810.02 | ₹14,760.00 |
| BAJFINANCE | 14 | ₹1095.50 | ₹1064.91 | ₹1249.43 | ₹15,337.00 |

## 📋 Trade History (84 closed | Win rate 33% | Total P&L ₹+2,083.29)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-11-25 18:38 | 🟢 BUY | BAJFINANCE | 14 | ₹1095.50 | — |  |
| 2026-11-25 18:38 | 🔴 SELL | BAJFINANCE | 13 | ₹1095.50 | ₹-332.80 | trailing_stop |
| 2026-11-24 14:17 | 🟢 BUY | TCS | 6 | ₹2460.00 | — |  |
| 2026-11-24 14:17 | 🟢 BUY | BAJAJFINSV | 8 | ₹1880.10 | — |  |
| 2026-11-24 14:17 | 🟢 BUY | AXISBANK | 11 | ₹1388.60 | — |  |
| 2026-11-24 14:17 | 🔴 SELL | AXISBANK | 11 | ₹1388.60 | ₹+0.00 | trailing_stop |
| 2026-11-24 14:17 | 🔴 SELL | ICICIBANK | 9 | ₹1585.50 | ₹+0.00 | trailing_stop |
| 2026-11-24 14:17 | 🔴 SELL | HDFCBANK | 18 | ₹817.80 | ₹+0.00 | trailing_stop |
| 2026-11-23 13:40 | 🟢 BUY | AXISBANK | 11 | ₹1388.60 | — |  |
| 2026-11-23 13:40 | 🟢 BUY | ICICIBANK | 9 | ₹1585.50 | — |  |
| 2026-11-23 13:40 | 🟢 BUY | HDFCBANK | 18 | ₹817.80 | — |  |
| 2026-11-23 13:40 | 🔴 SELL | AXISBANK | 11 | ₹1388.60 | ₹+574.20 | trailing_stop |
| 2026-11-23 13:40 | 🔴 SELL | HDFCBANK | 19 | ₹817.80 | ₹+561.45 | trailing_stop |
| 2026-11-23 13:40 | 🔴 SELL | ICICIBANK | 10 | ₹1585.50 | ₹+855.00 | trailing_stop |
| 2026-11-17 12:28 | 🟢 BUY | BAJFINANCE | 13 | ₹1121.10 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*