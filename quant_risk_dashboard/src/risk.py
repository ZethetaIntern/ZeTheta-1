import pandas as pd

def compute_drawdown(returns: pd.Series) -> pd.Series:
    equity_curve = (1 + returns).cumprod()
    peak = equity_curve.cummax()
    drawdown = (equity_curve - peak) / peak
    return drawdown

def max_drawdown(returns: pd.Series) -> float:
    dd = compute_drawdown(returns)
    return dd.min()