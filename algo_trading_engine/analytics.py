import numpy as np

def sharpe(equity):
    returns = np.diff(equity) / equity[:-1]
    if returns.std() == 0:
        return 0.0
    return np.sqrt(252) * returns.mean() / returns.std()

def max_drawdown(equity):
    peak = equity[0]
    dd = 0
    for x in equity:
        peak = max(peak, x)
        dd = min(dd, (x - peak) / peak)
    return dd
