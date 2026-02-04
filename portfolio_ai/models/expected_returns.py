import numpy as np


class ExpectedReturnsModel:
    @staticmethod
    def historical_mean(returns: np.ndarray) -> np.ndarray:
        if returns.ndim != 2:
            raise ValueError("Returns must be 2D array")
        return returns.mean(axis=0)
