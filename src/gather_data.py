def gather_data(universe, start_date, end_date):
    """
    Gathers the adjusted close prices of all assets and gets the closest date before the first of every month within the time span.

    Parameters:
        universe (list of str): A list of all the assets used.
        start_date (str): First date used in the close prices DataFrame in the format (YYYY-MM-DD). 
        end_date (str): Last date used in the close prices DataFrame in the format (YYYY-MM-DD).

    Returns:
    pd.DataFrame: A DataFrame containing the adjusted close prices of all the assets between the start and end date. Indexed by date with assets as columns.
    list: A list containing either the first of every month between the start and end date, or the closest date before the first of the month. Used as the rebalane dates.
    """
    import yfinance as yf
    import pandas as pd

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