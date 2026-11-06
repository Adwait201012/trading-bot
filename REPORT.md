# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-11-06 14:36 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹99,036.02 |
| Cash Available | ₹14,667.27 |
| Total P&L | 🔴 ₹-963.98 (-0.96%) |
| Drawdown from Peak | 🟢 0.96% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| HCLTECH | 10 | ₹1326.00 | ₹1396.80 | ₹1528.29 | ₹13,260.00 |
| TECHM | 8 | ₹1789.00 | ₹1776.07 | ₹2054.83 | ₹14,312.00 |
| KOTAKBANK | 33 | ₹440.00 | ₹465.60 | ₹486.82 | ₹14,520.00 |
| TCS | 5 | ₹2460.00 | ₹2427.52 | ₹2837.23 | ₹12,300.00 |
| ICICIBANK | 10 | ₹1500.00 | ₹1524.06 | ₹1650.32 | ₹15,000.00 |
| HDFCBANK | 19 | ₹788.25 | ₹764.60 | ₹875.81 | ₹14,976.75 |

## 📋 Trade History (72 closed | Win rate 32% | Total P&L ₹-963.98)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-11-06 11:30 | 🟢 BUY | HDFCBANK | 19 | ₹788.25 | — |  |
| 2026-11-06 11:30 | 🔴 SELL | ADANIPORTS | 8 | ₹1936.60 | ₹+1844.00 | target |
| 2026-11-05 11:30 | 🟢 BUY | ICICIBANK | 10 | ₹1500.00 | — |  |
| 2026-11-05 11:30 | 🔴 SELL | ICICIBANK | 10 | ₹1500.00 | ₹+1425.00 | target |
| 2026-10-28 10:01 | 🟢 BUY | TCS | 5 | ₹2460.00 | — |  |
| 2026-10-28 10:01 | 🟢 BUY | KOTAKBANK | 33 | ₹440.00 | — |  |
| 2026-10-28 10:01 | 🔴 SELL | INFY | 12 | ₹1123.15 | ₹-448.20 | trailing_stop |
| 2026-10-28 10:01 | 🔴 SELL | TCS | 5 | ₹2460.00 | ₹-234.50 | trailing_stop |
| 2026-10-23 09:36 | 🟢 BUY | TECHM | 8 | ₹1789.00 | — |  |
| 2026-10-23 08:50 | 🟢 BUY | ADANIPORTS | 8 | ₹1706.10 | — |  |
| 2026-10-23 08:50 | 🟢 BUY | INFY | 12 | ₹1160.50 | — |  |
| 2026-10-23 08:50 | 🔴 SELL | ADANIPORTS | 8 | ₹1706.10 | ₹-15.20 | trailing_stop |
| 2026-10-23 08:50 | 🔴 SELL | KOTAKBANK | 33 | ₹430.70 | ₹-141.90 | trailing_stop |
| 2026-10-22 10:39 | 🟢 BUY | TCS | 5 | ₹2506.90 | — |  |
| 2026-10-21 08:53 | 🔴 SELL | EICHERMOT | 2 | ₹7101.00 | ₹-367.00 | trailing_stop |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*