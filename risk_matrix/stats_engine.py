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
    
    def get_correlation_matrix(self) -> pd.DataFrame:
        """Oblicza macierz korelacji między aktywami"""
        return self.returns.corr()
    
    def calculate_parametric_var(self, confidence_level: float= 0.95, portfolio_value: float = 1000000) -> pd.Series:
        """
        Oblicza parametryczny value at risk dla każdego aktywa
        zwraca wartosc w walucie (ile pln mozna stracic)
        """
        #srednia i odchylenie standardowe
        mu = self.returns.mean()
        sigma = self.returns.std()

        #kwantyl rozkładu normalnego (z-score)
        z_score = norm.ppf(1 - confidence_level)

        var = abs(mu + z_score * sigma) * portfolio_value
        return var