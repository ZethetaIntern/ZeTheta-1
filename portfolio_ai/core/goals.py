from dataclasses import dataclass


@dataclass
class InvestmentGoal:
    name: str
    target_amount: float
    years: int
    priority: int


class GoalPlanner:
    @staticmethod
    def required_return(goal: InvestmentGoal, current_value: float) -> float:
        if current_value <= 0:
            raise ValueError("Current value must be positive")

        return (goal.target_amount / current_value) ** (1 / goal.years) - 1
