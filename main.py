from risk_matrix.data_loader import MarketDataLoader
from risk_matrix.stats_engine import RiskEngine
import numpy as np
def main():
    """portfel inwestycyjny"""
    assets = ['GOOGL', 'MSFT']

    loader = MarketDataLoader(assets)

    df = loader.fetch_data(start_date="2026-01-01", end_date="2026-03-31") #pobieranie danych
    if df.empty:
        print("błąd podczas pobierania danych. Przerywam działanie")
        return
    
    print("\n statystyki portfela")

    stats = loader.get_summary_stats()

    print(stats)

    returns = loader.calculate_log_returns() #logarytmiczne stopy zwrotu

    print("\n ostatnie 5 dni zwrotów logarytmicznych:")
    print(returns.tail())

    engine = RiskEngine(returns) #Inicjalizacja silnika ryzyka

    #Obliczanie VaR dla pojedynczych akcji (przy portfelu 100 000 USD)
    var_95 = engine.calculate_parametric_var(confidence_level=0.95, portfolio_value=100000)

    print("\n 1-dniowy VaR (95% ufnosci) dla 100k USD inwestycji")
    print(var_95)

    #VaR całego portfela (równe wagi: po 25% na każde aktywo)
    weights = np.array([0.25, 0.25, 0.25, 0.25])
    
    port_var = engine.calculate_portfolio_var(weights, confidence_level=0.95, portfolio_value=1000000)

    print(f"\n całkowity Var portfela: {port_var:.2f} USD")
    
if __name__=="__main__":
    main()