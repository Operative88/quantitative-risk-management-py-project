import pandas as pd
import numpy as np
import yfinance as yf




class MarketDataLoader:
    """Klasa do pobierania i wstępnego pobierania danych giełdowych"""
   

    def __init__(self, tickers: list[str]):
        self.tickers = tickers
        self.data: pd.DataFrame | None = None
    
    def fetch_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Pobiera ceny zamknięcia z yahoo finance"""
        print(f"Pobieranie danych dla: {', '.join(self.tickers)}")

        try:
            df = yf.download(self.tickers, start=start_date, end=end_date)
            
            #tylko ceny zamknięcia
            if not df.empty:
                self.data = df['Close']
            else:
                self.data = pd.DataFrame()
            
            return self.data
        
        except Exception as e:
            print(f"błąd podczas pobierania danych: {e}")
            return pd.DataFrame()
        
        