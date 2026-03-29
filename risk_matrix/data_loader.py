import pandas as pd
import numpy as pd
import requests

ALPHA_VANTAGE_API_KEY = ""

class MarketDataLoader:
    """Klasa do pobierania i wstępnego pobierania danych giełdowych"""
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, tickers: list[str], api_key: str = ALPHA_VANTAGE_API_KEY):
        self.tickers = tickers
        self.api_key = api_key
        self.data: pd.DataFrame | None = None
    
    def fetch_single(self, ticker: str, start_date: str, end_date: str) -> pd.Series:
        """Pobiera dane dla jednego tickera z Alpha Vantage"""
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": ticker,
            "outputsize": "full",
            "apikey": self.api_key,
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        json_data = response.json()
        if "Time series (daily)" not in json_data:
            error_msg = json_data.get("Note") or json_data.get("Information") or "Nieznany blad API"
            raise ValueError(f"blad dla {ticker}: {error_msg}")
