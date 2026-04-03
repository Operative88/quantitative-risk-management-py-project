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
        
    def calculate_log_returns(self) -> pd.DataFrame:
        """
        oblicza logarytmiczne stopy zwrotu wedlug
        r_t = ln(P_t / P_{t-1})
        """
        if self.data is None or self.data.empty:
            raise ValueError("Brak danych. Najpierw wywołaj fetch_data().")
            
        #wektorowe obliczanie zwrotów
        log_returns = np.log(self.data / self.data.shift(1)).dropna()
        return log_returns
        
    def get_summary_stats(self) -> pd.DataFrame:
        """Zwraca podstawowe statystyki opisowe dla pobranych aktywow"""
        returns = self.calculate_log_returns()
        summary = returns.aggregate(['mean', 'std', 'skew', 'kurtosis']).T
        summary['annual_mean'] = summary['mean'] * 252
        summary['annual_std'] = summary['std'] * np.sqrt(252)
        return summary
        
            
