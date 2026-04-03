import pandas as pd
import numpy as np
from scipy.stats import norm

class RiskEngine:
    """Silnik do obliczeń statystycznych i miar ryzyka."""

    def __init__(self, returns: pd.DataFrame):
        self.returns = returns

    def get_covariance_matrix(self) -> pd.DataFrame:
        """Oblicza macierz kowariancji zwrotów"""
        return self.returns.cov() * 252 #liczba dni handlowych w roku
    