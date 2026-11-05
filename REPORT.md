# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-11-05 12:46 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹97,192.02 |
| Cash Available | ₹14,151.22 |
| Total P&L | 🔴 ₹-2,807.98 (-2.81%) |
| Drawdown from Peak | 🟡 2.81% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| HCLTECH | 10 | ₹1326.00 | ₹1395.93 | ₹1528.29 | ₹13,260.00 |
| ADANIPORTS | 8 | ₹1706.10 | ₹1852.70 | ₹1934.69 | ₹13,648.80 |
| TECHM | 8 | ₹1789.00 | ₹1768.02 | ₹2054.83 | ₹14,312.00 |
| KOTAKBANK | 33 | ₹440.00 | ₹452.99 | ₹486.82 | ₹14,520.00 |
| TCS | 5 | ₹2460.00 | ₹2427.52 | ₹2837.23 | ₹12,300.00 |
| ICICIBANK | 10 | ₹1500.00 | ₹1455.00 | ₹1650.32 | ₹15,000.00 |

## 📋 Trade History (71 closed | Win rate 31% | Total P&L ₹-2,807.98)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
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
| 2026-10-21 08:53 | 🔴 SELL | ADANIENT | 5 | ₹2582.40 | ₹-68.00 | trailing_stop |
| 2026-10-16 11:54 | 🟢 BUY | EICHERMOT | 2 | ₹7284.50 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*