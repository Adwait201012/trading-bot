# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-07-03 08:40 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹98,471.97 |
| Cash Available | ₹12,851.67 |
| Total P&L | 🔴 ₹-1,528.03 (-1.53%) |
| Drawdown from Peak | 🟢 1.53% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3122.40 | ₹3107.88 | ₹3468.30 | ₹12,489.60 |
| ICICIBANK | 11 | ₹1322.90 | ₹1371.48 | ₹1455.98 | ₹14,551.90 |
| SBIN | 14 | ₹1010.75 | ₹1021.22 | ₹1116.17 | ₹14,150.50 |
| BAJFINANCE | 15 | ₹969.30 | ₹1006.08 | ₹1076.94 | ₹14,539.50 |
| ADANIENT | 5 | ₹2987.30 | ₹3102.45 | ₹3405.18 | ₹14,936.50 |
| AXISBANK | 11 | ₹1359.30 | ₹1335.30 | ₹1478.56 | ₹14,952.30 |

## 📋 Trade History (10 closed | Win rate 30% | Total P&L ₹-1,528.03)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-06-30 07:38 | 🟢 BUY | AXISBANK | 11 | ₹1359.30 | — |  |
| 2026-06-30 07:38 | 🔴 SELL | EICHERMOT | 2 | ₹7133.00 | ₹-567.00 | trailing_stop |
| 2026-06-29 08:35 | 🟢 BUY | ADANIENT | 5 | ₹2987.30 | — |  |
| 2026-06-29 08:35 | 🟢 BUY | EICHERMOT | 2 | ₹7416.50 | — |  |
| 2026-06-29 08:35 | 🔴 SELL | EICHERMOT | 2 | ₹7416.50 | ₹+479.00 | trailing_stop |
| 2026-06-29 08:35 | 🔴 SELL | KOTAKBANK | 39 | ₹395.75 | ₹+450.45 | trailing_stop |
| 2026-06-23 07:05 | 🟢 BUY | BAJFINANCE | 15 | ₹969.30 | — |  |
| 2026-06-23 07:05 | 🔴 SELL | ADANIPORTS | 8 | ₹1788.10 | ₹-65.60 | trailing_stop |
| 2026-06-12 08:12 | 🟢 BUY | SBIN | 14 | ₹1010.75 | — |  |
| 2026-06-12 08:12 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹10076.00 | ₹-191.00 | trailing_stop |
| 2026-06-11 08:24 | 🟢 BUY | ICICIBANK | 11 | ₹1322.90 | — |  |
| 2026-06-11 08:24 | 🔴 SELL | TECHM | 9 | ₹1455.10 | ₹-449.10 | trailing_stop |
| 2026-06-08 09:04 | 🟢 BUY | TECHM | 9 | ₹1505.00 | — |  |
| 2026-06-08 08:31 | 🔴 SELL | SHREECEM | 0 | ₹23675.00 | ₹-0.00 | signal |
| 2026-06-05 07:55 | 🟢 BUY | SHREECEM | 0 | ₹24125.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*