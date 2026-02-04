import cvxpy as cp
import numpy as np


class MeanVarianceOptimizer:
    def __init__(self, expected_returns, covariance):
        self.mu = expected_returns
        self.cov = covariance

    def optimize(self, risk_aversion, max_weight=0.4, prev_weights=None, max_turnover=0.3):
        n = len(self.mu)
        w = cp.Variable(n)

        risk = cp.quad_form(w, self.cov)
        ret = self.mu @ w

        constraints = [
            cp.sum(w) == 1,
            w >= 0,
            w <= max_weight
        ]

        if prev_weights is not None:
            turnover = cp.norm1(w - prev_weights)
            constraints.append(turnover <= max_turnover)

        problem = cp.Problem(
            cp.Maximize(ret - risk_aversion * risk),
            constraints
        )

        problem.solve(solver=cp.SCS)

        if problem.status != cp.OPTIMAL:
            raise RuntimeError("Optimization failed")

        return np.clip(w.value, 0, None)
