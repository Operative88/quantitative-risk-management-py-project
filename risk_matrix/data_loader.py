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