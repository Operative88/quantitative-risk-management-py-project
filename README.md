# Quantitative risk management project in python

![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/Operative88/quantitative-risk-management-py-project/tests.yml?style=for-the-badge)
![Poetry](https://img.shields.io/badge/poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/scipy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![Statsmodels](https://img.shields.io/badge/statsmodels-003366?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/matplotlib-11557C?style=for-the-badge)


## Engine that analyzes investment portfolio in terms of various risk measures
### • Value at Risk (VaR) & Expected Shortfall (ES): Implementation of three VaR computational methods:
    1. Historical (based on past data)
    2. Parametric (assuming a normal distribution)
    3. Monte carlo (generating thousands of simulated price paths)

### • Volatility analysis
    EWMA model implementation (Exponentially Weighted Moving Average)

### Project architecture
| Module | Functionality |
|---|---|
| `data_loader/` | Downloading data from API (`Alpha Vantage`). |
| `stats_engine/` | Calculation of covariance and correlation matrices and normality tests. |
| `risk_models/` | Classes for Monte Carlo simulation and VaR estimation. |
| `visualizer/` | Generating interactive charts with `Plotly` or `Seaborn`. |
| `reports/` | Automatic generation PDF reports with portfolio risk summary |

aktualizacja