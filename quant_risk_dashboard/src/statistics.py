import numpy as np
from scipy.stats import norm

def sharpe_significance_test(sharpe: float, n: int):
    """
    Jobson-Korkie style Sharpe significance test (approximation)
    """
    if n <= 1:
        return 0.0, 1.0
    
    se = np.sqrt((1 + 0.5 * sharpe**2) / n)
    z_stat = sharpe / se
    p_value = 2 * (1 - norm.cdf(abs(z_stat)))
    
    return z_stat, p_value