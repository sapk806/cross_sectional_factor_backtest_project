import yfinance as yf
import pandas as pd

def gather_data(universe: list[str], start_date: str, end_date: str):
    """
    Downloads the adjusted close prices of a group of Yahoo Finance tickers and finds the closest date before the first of every month.
    Saves close prices to 'results/close_prices.csv'
    
    Args:
        universe (list[str]): List of Yahoo Finance tickers to download data for.
        start_date (str): Start date in 'YYYY-MM-DD' format. 
        end_date (str): End date 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: DataFrame containing the adjusted close prices of all the assets between the start and end date. Indexed by date with assets as columns.
    list[pd.Timestamp]: List containing either the first of every month between the start and end date, or the closest date before the first of the month. Used as the rebalane dates.
    """

    close_prices = yf.download(universe, start = start_date, end = end_date)['Close'].dropna()

    target_date = pd.date_range(start = start_date, end = end_date, freq = 'MS')
    
    rebalance_trading_dates = []
    for date in target_date:
        if date in close_prices.index:
            rebalance_trading_dates.append(date)
        elif date not in close_prices.index:
            adjusted_trading_date = close_prices.index[close_prices.index < date].max()
            rebalance_trading_dates.append(adjusted_trading_date)            

    close_prices.to_csv('results/close_prices.csv')
    return close_prices, rebalance_trading_dates