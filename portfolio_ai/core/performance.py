import numpy as np


class PerformanceMetrics:
    @staticmethod
    def sharpe(returns, risk_free=0.02):
        excess = returns - risk_free / 252
        return np.mean(excess) / np.std(excess)

    @staticmethod
    def max_drawdown(cumulative):
        peak = np.maximum.accumulate(cumulative)
        return np.min((cumulative - peak) / peak)

    @staticmethod
    def var(returns, alpha=0.05):
        return np.percentile(returns, alpha * 100)
