# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-10-08 14:33 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹95,941.17 |
| Cash Available | ₹41,367.17 |
| Total P&L | 🔴 ₹-4,058.83 (-4.06%) |
| Drawdown from Peak | 🟡 4.06% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| ICICIBANK | 10 | ₹1357.50 | ₹1316.78 | ₹1462.34 | ₹13,575.00 |
| KOTAKBANK | 33 | ₹435.00 | ₹421.95 | ₹481.04 | ₹14,355.00 |
| ADANIENT | 5 | ₹2596.00 | ₹2518.12 | ₹3042.31 | ₹12,980.00 |
| ADANIPORTS | 8 | ₹1708.00 | ₹1656.76 | ₹1925.39 | ₹13,664.00 |

## 📋 Trade History (62 closed | Win rate 31% | Total P&L ₹-4,058.83)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-10-08 10:56 | 🟢 BUY | ADANIPORTS | 8 | ₹1708.00 | — |  |
| 2026-10-08 10:56 | 🟢 BUY | ADANIENT | 5 | ₹2596.00 | — |  |
| 2026-10-08 10:56 | 🟢 BUY | KOTAKBANK | 33 | ₹435.00 | — |  |
| 2026-10-08 10:56 | 🔴 SELL | ADANIPORTS | 8 | ₹1708.00 | ₹-528.00 | trailing_stop |
| 2026-10-07 10:35 | 🟢 BUY | ICICIBANK | 10 | ₹1357.50 | — |  |
| 2026-10-07 10:35 | 🔴 SELL | KOTAKBANK | 36 | ₹440.00 | ₹+1296.00 | target |
| 2026-10-05 10:51 | 🟢 BUY | ADANIPORTS | 8 | ₹1774.00 | — |  |
| 2026-10-01 10:28 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹10045.00 | ₹-766.00 | trailing_stop |
| 2026-10-01 10:28 | 🔴 SELL | ADANIPORTS | 8 | ₹1737.80 | ₹-47.20 | trailing_stop |
| 2026-09-29 12:53 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹10811.00 | — |  |
| 2026-09-29 10:08 | 🔴 SELL | GRASIM | 4 | ₹3100.00 | ₹-363.20 | trailing_stop |
| 2026-09-28 10:10 | 🟢 BUY | ADANIPORTS | 8 | ₹1743.70 | — |  |
| 2026-09-28 10:10 | 🔴 SELL | HDFCBANK | 20 | ₹719.05 | ₹-229.00 | trailing_stop |
| 2026-09-28 10:10 | 🔴 SELL | EICHERMOT | 1 | ₹7213.50 | ₹-239.00 | trailing_stop |
| 2026-09-28 10:10 | 🔴 SELL | ADANIPORTS | 8 | ₹1743.70 | ₹+116.80 | trailing_stop |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*