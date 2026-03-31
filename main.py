from risk_matrix.data_loader import MarketDataLoader

def main():
    """portfel inwestycyjny"""
    assets = ['GOOGL', 'MSFT']

    loader = MarketDataLoader(assets)

    loader.fetch_data(start_date="2026-01-01", end_date="2026-03-31") #pobieranie danych

    