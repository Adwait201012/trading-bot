# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-11-26 18:37 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹102,427.09 |
| Cash Available | ₹11,669.04 |
| Total P&L | 🟢 ₹+2,427.09 (+2.43%) |
| Drawdown from Peak | 🟢 -2.43% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| SBIN | 14 | ₹1061.20 | ₹1130.15 | ₹1176.81 | ₹14,856.80 |
| KOTAKBANK | 31 | ₹488.55 | ₹500.33 | ₹539.65 | ₹15,145.05 |
| AXISBANK | 11 | ₹1388.60 | ₹1375.56 | ₹1558.95 | ₹15,274.60 |
| BAJAJFINSV | 8 | ₹1880.10 | ₹1867.25 | ₹2099.18 | ₹15,040.80 |
| BAJFINANCE | 14 | ₹1095.50 | ₹1097.41 | ₹1249.43 | ₹15,337.00 |
| TCS | 6 | ₹2517.30 | ₹2376.72 | ₹2868.75 | ₹15,103.80 |

## 📋 Trade History (85 closed | Win rate 34% | Total P&L ₹+2,427.09)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-11-26 18:37 | 🟢 BUY | TCS | 6 | ₹2517.30 | — |  |
| 2026-11-26 18:37 | 🔴 SELL | TCS | 6 | ₹2517.30 | ₹+343.80 | trailing_stop |
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

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*