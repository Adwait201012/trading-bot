"""Performance metrics: CAGR, Sharpe, max drawdown, win rate, worst-case loss."""
import numpy as np
import pandas as pd


def compute(equity_curve: pd.Series, trades: list[dict], risk_free_rate: float = 0.065) -> dict:
    """
    equity_curve : pd.Series indexed by date, values = portfolio value
    trades       : list of closed trade dicts with 'pnl' key
    risk_free_rate: Indian 10Y GSec ~6.5%
    """
    if len(equity_curve) < 2:
        return {}

    start_val = equity_curve.iloc[0]
    end_val   = equity_curve.iloc[-1]
    years     = (equity_curve.index[-1] - equity_curve.index[0]).days / 365.25

    # CAGR
    cagr = ((end_val / start_val) ** (1 / years) - 1) if years > 0 else 0

    # Daily returns
    daily_returns = equity_curve.pct_change().dropna()
    ann_factor    = np.sqrt(252)

    # Sharpe
    excess = daily_returns - (risk_free_rate / 252)
    sharpe = (excess.mean() / excess.std() * ann_factor) if excess.std() > 0 else 0

    # Max drawdown
    rolling_peak = equity_curve.cummax()
    drawdown     = (equity_curve - rolling_peak) / rolling_peak
    max_dd       = drawdown.min()
    max_dd_date  = drawdown.idxmin()

    # Worst single-day loss
    worst_day = daily_returns.min()

    # Trade stats
    closed = [t for t in trades if "pnl" in t]
    wins   = [t for t in closed if t["pnl"] > 0]
    losses = [t for t in closed if t["pnl"] <= 0]

    win_rate    = len(wins) / len(closed) if closed else 0
    avg_win     = np.mean([t["pnl"] for t in wins])   if wins   else 0
    avg_loss    = np.mean([t["pnl"] for t in losses]) if losses else 0
    profit_factor = (sum(t["pnl"] for t in wins) / abs(sum(t["pnl"] for t in losses))
                     if losses and sum(t["pnl"] for t in losses) != 0 else float("inf"))

    return {
        "cagr":          round(cagr * 100, 2),
        "sharpe":        round(sharpe, 2),
        "max_drawdown":  round(max_dd * 100, 2),
        "max_dd_date":   str(max_dd_date.date()) if hasattr(max_dd_date, "date") else str(max_dd_date),
        "worst_day":     round(worst_day * 100, 2),
        "total_trades":  len(closed),
        "win_rate":      round(win_rate * 100, 2),
        "avg_win_inr":   round(avg_win, 2),
        "avg_loss_inr":  round(avg_loss, 2),
        "profit_factor": round(profit_factor, 2),
        "final_value":   round(end_val, 2),
        "total_return":  round((end_val / start_val - 1) * 100, 2),
        "years":         round(years, 1),
    }
