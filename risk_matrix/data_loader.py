import pandas as pd
import numpy as pd
import requests

ALPHA_VANTAGE_API_KEY = ""

class MarketDataLoader:
    """Klasa do pobierania i wstępnego pobierania danych giełdowych"""
    BASE_URL = "https://www.alphavantage.co/query"