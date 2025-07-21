## Cross Sectional Factor Backtest

## Overview
My project gathers the 12-month returns of assets using Yahoo Finance tickers and uses the returns to decide which assets to go long or go short on.

## Dependencies 
- Python 3.13+
- pandas
- numpy
- matplotlib
- yfinance
- jupyter

## How to Run
- Activate the virtual environment with the required packages and run the script in the main.py file: 

1. Activate the virtual environment.
```bash
source .venv/bin/activate
```
2. Install dependencies.
```bash
pip install -r requirements.txt
```
3. Run the full backtest.
```bash
python main.py
```


## Output
- Plot of cumulative return at each date, with drawdowns filled in when the highest return seen at the date is higher than the current cumulative return.
- Performance metrics
    - Cumulative return
    - Sharpe ratio
    - Max drawdown
    - t-value
