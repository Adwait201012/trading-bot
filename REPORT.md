# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-08-28 18:42 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹104,215.07 |
| Cash Available | ₹15,069.57 |
| Total P&L | 🟢 ₹+4,215.07 (+4.22%) |
| Drawdown from Peak | 🟢 -4.22% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| EICHERMOT | 2 | ₹7638.00 | ₹7885.61 | ₹8406.00 | ₹15,276.00 |
| BAJFINANCE | 14 | ₹1095.80 | ₹1071.85 | ₹1247.64 | ₹15,341.20 |
| BAJAJFINSV | 7 | ₹1991.70 | ₹1976.38 | ₹2239.91 | ₹13,941.90 |
| ICICIBANK | 11 | ₹1421.40 | ₹1399.71 | ₹1544.08 | ₹15,635.40 |
| SBIN | 14 | ₹1049.00 | ₹1027.42 | ₹1145.39 | ₹14,686.00 |
| TECHM | 9 | ₹1585.00 | ₹1513.41 | ₹1763.97 | ₹14,265.00 |

## 📋 Trade History (33 closed | Win rate 48% | Total P&L ₹+4,215.07)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-08-28 18:42 | 🟢 BUY | TECHM | 9 | ₹1585.00 | — |  |
| 2026-08-28 18:42 | 🔴 SELL | TECHM | 9 | ₹1585.00 | ₹-27.90 | trailing_stop |
| 2026-08-19 04:53 | 🟢 BUY | SBIN | 14 | ₹1049.00 | — |  |
| 2026-08-19 04:53 | 🔴 SELL | SBIN | 14 | ₹1049.00 | ₹-261.80 | trailing_stop |
| 2026-08-18 04:20 | 🟢 BUY | TECHM | 9 | ₹1588.10 | — |  |
| 2026-08-18 04:20 | 🔴 SELL | TECHM | 9 | ₹1588.10 | ₹-334.80 | trailing_stop |
| 2026-08-12 06:39 | 🟢 BUY | TECHM | 9 | ₹1625.30 | — |  |
| 2026-08-12 06:39 | 🔴 SELL | TECHM | 9 | ₹1625.30 | ₹+788.40 | trailing_stop |
| 2026-08-11 06:01 | 🟢 BUY | SBIN | 14 | ₹1067.70 | — |  |
| 2026-08-11 06:01 | 🔴 SELL | ULTRACEMCO | 1 | ₹11797.00 | ₹-200.00 | trailing_stop |
| 2026-08-07 09:14 | 🟢 BUY | ICICIBANK | 11 | ₹1421.40 | — |  |
| 2026-08-07 09:14 | 🔴 SELL | ICICIBANK | 10 | ₹1421.40 | ₹+411.00 | trailing_stop |
| 2026-08-07 08:20 | 🟢 BUY | BAJAJFINSV | 7 | ₹1991.70 | — |  |
| 2026-08-07 08:20 | 🔴 SELL | SBIN | 15 | ₹1114.90 | ₹+1507.50 | target |
| 2026-08-07 05:23 | 🟢 BUY | BAJFINANCE | 14 | ₹1095.80 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*