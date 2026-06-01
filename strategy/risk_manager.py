"""
Portfolio-level risk management.
Circuit breakers: max drawdown halt, daily loss limit, trailing stop updates.
"""
from config import (MAX_PORTFOLIO_DRAWDOWN, DAILY_LOSS_LIMIT,
                    ATR_TRAIL_MULTIPLIER, STARTING_CAPITAL)


def check_circuit_breaker(portfolio_value: float, peak_value: float,
                           day_start_value: float) -> dict:
    drawdown   = (peak_value - portfolio_value) / peak_value if peak_value > 0 else 0
    daily_loss = (day_start_value - portfolio_value) / day_start_value if day_start_value > 0 else 0

    halted  = drawdown >= MAX_PORTFOLIO_DRAWDOWN or daily_loss >= DAILY_LOSS_LIMIT
    reasons = []
    if drawdown >= MAX_PORTFOLIO_DRAWDOWN:
        reasons.append(f"Portfolio drawdown {drawdown*100:.1f}% >= {MAX_PORTFOLIO_DRAWDOWN*100:.0f}% limit")
    if daily_loss >= DAILY_LOSS_LIMIT:
        reasons.append(f"Daily loss {daily_loss*100:.1f}% >= {DAILY_LOSS_LIMIT*100:.0f}% limit")

    return {"halted": halted, "drawdown": drawdown,
            "daily_loss": daily_loss, "reasons": reasons}


def update_trailing_stop(position: dict, current_high: float, atr: float) -> float:
    """Returns updated (higher) trailing stop. Never moves the stop down."""
    new_stop = current_high - ATR_TRAIL_MULTIPLIER * atr
    return max(position.get("trailing_stop", 0), new_stop)


def should_exit_trailing(position: dict, current_price: float) -> bool:
    return current_price <= position.get("trailing_stop", 0)
