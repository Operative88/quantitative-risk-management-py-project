from risk_matrix.data_loader import MarketDataLoader

def main():
    """portfel inwestycyjny"""
    assets = ['GOOGL', 'MSFT']

    loader = MarketDataLoader(assets)

    loader.fetch_data(start_date="2026-01-01", end_date="2026-03-31") #pobieranie danych

    print("\n statystyki portfela")

    stats = loader.get_summary_stats()

    print(stats)

    returns = loader.calculate_log_returns() #logarytmiczne stopy zwrotu

    print("\n ostatnie 5 dni zwrotów logarytmicznych:")
    print(returns.tail())

if __name__=="__main__":
    main()