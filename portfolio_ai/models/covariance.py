import numpy as np


class CovarianceModel:
    @staticmethod
    def sample_covariance(returns: np.ndarray) -> np.ndarray:
        if returns.ndim != 2:
            raise ValueError("Returns must be 2D array")
        return np.cov(returns, rowvar=False)
