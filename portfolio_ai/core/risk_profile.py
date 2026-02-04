from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    text: str
    weight: int


class RiskProfiler:
    def __init__(self, questions: List[Question]):
        self.questions = questions

    def calculate_score(self, responses: List[int]) -> int:
        if len(responses) != len(self.questions):
            raise ValueError("Responses must match number of questions")

        score = 0
        for r, q in zip(responses, self.questions):
            if r not in [1, 2, 3, 4, 5]:
                raise ValueError("Responses must be between 1 and 5")
            score += r * q.weight
        return score

    @staticmethod
    def risk_category(score: int) -> str:
        if score <= 40:
            return "Conservative"
        elif score <= 70:
            return "Moderate"
        return "Aggressive"
