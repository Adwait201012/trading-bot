# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-11-12 13:43 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹101,180.12 |
| Cash Available | ₹14,042.57 |
| Total P&L | 🟢 ₹+1,180.12 (+1.18%) |
| Drawdown from Peak | 🟢 -1.18% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| TCS | 5 | ₹2460.00 | ₹2427.52 | ₹2837.23 | ₹12,300.00 |
| ICICIBANK | 10 | ₹1500.00 | ₹1542.30 | ₹1650.32 | ₹15,000.00 |
| HDFCBANK | 19 | ₹788.25 | ₹787.93 | ₹875.81 | ₹14,976.75 |
| AXISBANK | 11 | ₹1336.40 | ₹1302.61 | ₹1489.09 | ₹14,700.40 |
| SBIN | 14 | ₹1061.20 | ₹1053.90 | ₹1176.81 | ₹14,856.80 |
| WIPRO | 78 | ₹196.20 | ₹190.31 | ₹220.91 | ₹15,303.60 |

## 📋 Trade History (75 closed | Win rate 33% | Total P&L ₹+1,180.12)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-11-12 11:51 | 🟢 BUY | WIPRO | 78 | ₹196.20 | — |  |
| 2026-11-12 11:51 | 🔴 SELL | TECHM | 8 | ₹1774.00 | ₹-120.00 | trailing_stop |
| 2026-11-11 11:27 | 🟢 BUY | SBIN | 14 | ₹1061.20 | — |  |
| 2026-11-11 11:27 | 🟢 BUY | AXISBANK | 11 | ₹1336.40 | — |  |
| 2026-11-11 11:27 | 🔴 SELL | KOTAKBANK | 33 | ₹487.70 | ₹+1574.10 | target |
| 2026-11-11 11:27 | 🔴 SELL | HCLTECH | 10 | ₹1395.00 | ₹+690.00 | trailing_stop |
| 2026-11-06 11:30 | 🟢 BUY | HDFCBANK | 19 | ₹788.25 | — |  |
| 2026-11-06 11:30 | 🔴 SELL | ADANIPORTS | 8 | ₹1936.60 | ₹+1844.00 | target |
| 2026-11-05 11:30 | 🟢 BUY | ICICIBANK | 10 | ₹1500.00 | — |  |
| 2026-11-05 11:30 | 🔴 SELL | ICICIBANK | 10 | ₹1500.00 | ₹+1425.00 | target |
| 2026-10-28 10:01 | 🟢 BUY | TCS | 5 | ₹2460.00 | — |  |
| 2026-10-28 10:01 | 🟢 BUY | KOTAKBANK | 33 | ₹440.00 | — |  |
| 2026-10-28 10:01 | 🔴 SELL | INFY | 12 | ₹1123.15 | ₹-448.20 | trailing_stop |
| 2026-10-28 10:01 | 🔴 SELL | TCS | 5 | ₹2460.00 | ₹-234.50 | trailing_stop |
| 2026-10-23 09:36 | 🟢 BUY | TECHM | 8 | ₹1789.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*