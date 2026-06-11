# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-06-11 11:59 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹98,366.12 |
| Cash Available | ₹17,349.42 |
| Total P&L | 🔴 ₹-1,633.88 (-1.63%) |
| Drawdown from Peak | 🟢 1.63% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| KOTAKBANK | 39 | ₹384.20 | ₹384.65 | ₹426.92 | ₹14,983.80 |
| EICHERMOT | 2 | ₹7177.00 | ₹7048.99 | ₹8129.42 | ₹14,354.00 |
| GRASIM | 4 | ₹3122.40 | ₹3041.63 | ₹3468.30 | ₹12,489.60 |
| BAJAJ-AUTO | 1 | ₹10267.00 | ₹10095.76 | ₹11466.61 | ₹10,267.00 |
| ADANIPORTS | 8 | ₹1796.30 | ₹1785.58 | ₹2010.79 | ₹14,370.40 |
| ICICIBANK | 11 | ₹1322.90 | ₹1280.98 | ₹1455.98 | ₹14,551.90 |

## 📋 Trade History (5 closed | Win rate 20% | Total P&L ₹-1,633.88)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-06-11 08:24 | 🟢 BUY | ICICIBANK | 11 | ₹1322.90 | — |  |
| 2026-06-11 08:24 | 🔴 SELL | TECHM | 9 | ₹1455.10 | ₹-449.10 | trailing_stop |
| 2026-06-08 09:04 | 🟢 BUY | TECHM | 9 | ₹1505.00 | — |  |
| 2026-06-08 08:31 | 🔴 SELL | SHREECEM | 0 | ₹23675.00 | ₹-0.00 | signal |
| 2026-06-05 07:55 | 🟢 BUY | SHREECEM | 0 | ₹24125.00 | — |  |
| 2026-06-05 07:55 | 🔴 SELL | WIPRO | 73 | ₹195.59 | ₹-632.18 | trailing_stop |
| 2026-06-04 08:34 | 🟢 BUY | ADANIPORTS | 8 | ₹1796.30 | — |  |
| 2026-06-04 08:34 | 🔴 SELL | BAJAJFINSV | 8 | ₹1710.90 | ₹-581.60 | trailing_stop |
| 2026-06-03 08:36 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10267.00 | — |  |
| 2026-06-03 08:36 | 🔴 SELL | TECHM | 10 | ₹1486.80 | ₹+29.00 | trailing_stop |
| 2026-06-01 21:37 | 🟢 BUY | GRASIM | 4 | ₹3122.40 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | EICHERMOT | 2 | ₹7177.00 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | TECHM | 10 | ₹1483.90 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | WIPRO | 73 | ₹204.25 | — |  |
| 2026-06-01 21:37 | 🟢 BUY | BAJAJFINSV | 8 | ₹1783.60 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*