import pandas as pd
import numpy as np

from core.risk_profile import Question, RiskProfiler
from core.goals import InvestmentGoal, GoalPlanner
from models.expected_returns import ExpectedReturnsModel
from models.covariance import CovarianceModel
from core.optimizer import MeanVarianceOptimizer
from core.rebalancer import Rebalancer
from reports.client_report import ClientReport

prices = pd.read_csv("data/sample_prices.csv")
returns = prices.pct_change().dropna().values

questions = [
    Question("Horizon", 2),
    Question("Loss tolerance", 3),
    Question("Experience", 2),
    Question("Income stability", 1)
]

responses = [4, 3, 4, 5]
profiler = RiskProfiler(questions)
score = profiler.calculate_score(responses)
risk_category = profiler.risk_category(score)

risk_map = {"Conservative": 5.0, "Moderate": 2.5, "Aggressive": 1.0}

goal = InvestmentGoal("Retirement", 1_000_000, 20, 1)
goal_return = GoalPlanner.required_return(goal, 200_000)

mu = ExpectedReturnsModel.historical_mean(returns)
cov = CovarianceModel.sample_covariance(returns)

prev_weights = np.ones(len(mu)) / len(mu)

optimizer = MeanVarianceOptimizer(mu, cov)
weights = optimizer.optimize(
    risk_map[risk_category],
    max_weight=0.4,
    prev_weights=prev_weights
)

trades = Rebalancer.rebalance(prev_weights, weights)

report = ClientReport.generate(
    weights,
    returns,
    goal_return,
    risk_category
)

print("FINAL CLIENT REPORT")
print(report)
