import numpy as np
import pandas as pd

TRADING_DAYS = 252

def annualized_return(returns: pd.Series) -> float:
    return returns.mean() * TRADING_DAYS

def annualized_volatility(returns: pd.Series) -> float:
    return returns.std() * np.sqrt(TRADING_DAYS)

def sharpe_ratio(returns: pd.Series, rf: float = 0.0) -> float:
    excess = returns - rf / TRADING_DAYS
    vol = annualized_volatility(returns)
    if vol == 0:
        return 0.0
    return annualized_return(excess) / vol