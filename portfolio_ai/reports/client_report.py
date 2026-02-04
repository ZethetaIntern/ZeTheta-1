from core.advisor import RoboAdvisor
from core.performance import PerformanceMetrics
import numpy as np


class ClientReport:
    @staticmethod
    def generate(weights, returns, goal_return, risk_category):
        portfolio_returns = returns @ weights
        cumulative = (1 + portfolio_returns).cumprod()

        report = {
    "expected_return": round(float(portfolio_returns.mean()), 4),
    "volatility": round(float(np.std(portfolio_returns)), 4),
    "sharpe": round(float(PerformanceMetrics.sharpe(portfolio_returns)), 2),
    "max_drawdown": round(float(PerformanceMetrics.max_drawdown(cumulative)), 4),
    "VaR_95": round(float(PerformanceMetrics.var(portfolio_returns)), 4),
    "weights": [round(float(w), 4) for w in weights],
    "advisor_note": RoboAdvisor.recommendation(
        goal_return,
        float(portfolio_returns.mean()),
        risk_category
    )
}


        return report
