import pandas as pd 

def find_factor(close_prices: pd.DataFrame, rebalance_trading_dates: list[pd.Timestamp]):
    """
    Calculates the 12-month returns at each rebalance date to use as the factor for ranking.
    Saves 12-month returns to 'results/12_month_returns.csv'
    
    Args:
        close_prices (pd.DataFrame): DataFrame containing the adjusted close prices of each asset at every date between the start and end date. Indexed by date with assets as columns.
        rebalance_trading_dates (list[pd.Timestamp]): List of rebalance dates.
    
    Returns:
        pd.DataFrame: DataFrame containing the adjusted close prices of each asset at each rebalance date in the rebalance tradiong dates list.
        pd.DataFrame: DataFrame containing the percent change of the shifted DataFrame containing the adjusted close prices, removing future bias and finding the return of each asset between rebalance dates. 
    """

    rebalance_date_close_prices = close_prices.loc[rebalance_trading_dates[1:]]
    shifted_close_prices = rebalance_date_close_prices.shift(1)
    
    twelve_month_returns = shifted_close_prices.pct_change(periods = 12).dropna()

    twelve_month_returns.to_csv('results/12_month_returns.csv')
    return rebalance_date_close_prices, twelve_month_returns
