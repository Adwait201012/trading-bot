# 📈 Trading Bot — Live Portfolio Report

**Last updated:** 2026-09-10 10:03 IST

> ⚠️ **PAPER TRADING ONLY — No real money at risk**

## 💰 Portfolio Summary
| Metric | Value |
|---|---|
| Starting Capital | ₹100,000.00 |
| Current Value | ₹100,644.37 |
| Cash Available | ₹20,499.87 |
| Total P&L | 🟢 ₹+644.37 (+0.64%) |
| Drawdown from Peak | 🟢 -0.64% |

## 📂 Open Positions
| Stock | Qty | Entry | Stop | Target | Est. Value |
|---|---|---|---|---|---|
| GRASIM | 4 | ₹3292.90 | ₹3224.86 | ₹3629.84 | ₹13,171.60 |
| KOTAKBANK | 36 | ₹424.30 | ₹412.01 | ₹460.58 | ₹15,274.80 |
| ICICIBANK | 10 | ₹1400.40 | ₹1359.45 | ₹1510.21 | ₹14,004.00 |
| ADANIENT | 4 | ₹3101.00 | ₹3011.56 | ₹3528.90 | ₹12,404.00 |
| BAJAJFINSV | 7 | ₹1932.30 | ₹1882.29 | ₹2106.97 | ₹13,526.10 |
| BAJAJ-AUTO | 1 | ₹11764.00 | ₹11436.30 | ₹12853.48 | ₹11,764.00 |

## 📋 Trade History (45 closed | Win rate 38% | Total P&L ₹+644.37)
| Time | Action | Stock | Qty | Price | P&L | Reason |
|---|---|---|---|---|---|---|
| 2026-09-09 09:12 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹11764.00 | — |  |
| 2026-09-09 09:12 | 🟢 BUY | BAJAJFINSV | 7 | ₹1932.30 | — |  |
| 2026-09-09 09:12 | 🔴 SELL | BAJAJ-AUTO | 1 | ₹11764.00 | ₹-287.00 | trailing_stop |
| 2026-09-09 09:12 | 🔴 SELL | BAJAJFINSV | 7 | ₹1932.30 | ₹-226.80 | trailing_stop |
| 2026-09-09 08:23 | 🟢 BUY | ADANIENT | 4 | ₹3101.00 | — |  |
| 2026-09-09 08:23 | 🔴 SELL | TECHM | 9 | ₹1503.00 | ₹-383.40 | trailing_stop |
| 2026-09-08 09:37 | 🟢 BUY | TECHM | 9 | ₹1545.60 | — |  |
| 2026-09-08 09:37 | 🔴 SELL | TECHM | 9 | ₹1545.60 | ₹-387.90 | trailing_stop |
| 2026-09-08 08:20 | 🟢 BUY | ICICIBANK | 10 | ₹1400.40 | — |  |
| 2026-09-08 08:20 | 🔴 SELL | ICICIBANK | 11 | ₹1400.40 | ₹-231.00 | trailing_stop |
| 2026-09-04 09:04 | 🟢 BUY | TECHM | 9 | ₹1588.70 | — |  |
| 2026-09-04 09:04 | 🔴 SELL | TECHM | 9 | ₹1588.70 | ₹+33.30 | trailing_stop |
| 2026-09-04 08:14 | 🟢 BUY | KOTAKBANK | 36 | ₹424.30 | — |  |
| 2026-09-04 08:14 | 🔴 SELL | HCLTECH | 11 | ₹1300.00 | ₹-588.50 | trailing_stop |
| 2026-09-02 08:48 | 🟢 BUY | BAJAJ-AUTO | 1 | ₹12051.00 | — |  |

---
**Strategy:** Supertrend + RSI + MACD + ATR trailing stops + Support/Resistance

**Risk controls:** ATR stop loss | Trailing stops | 12% drawdown circuit breaker | 2% risk per trade

*Runs every 30 min on weekdays 9:15 AM – 3:30 PM IST via GitHub Actions*