def strategy(factor, rebalance_date_close_prices):
    """
    Ranks each asset by factor to decide which assets to long and short until the next rebalance date.

    Parameters:
        factor (pd.DataFrame): A DataFrame containing the percent change of the shifted DataFrame containing the adjusted close prices, removing future bias and finding the return of each asset between rebalance dates.
        rebalance_date_close_prices (pd.DataFrame): A DataFrame containing the adjusted close prices of each asset at each rebalance date in the rebalance tradiong dates list.
    
    Returns:
        pd.Series: A series containing the returns of the portfolio based on the strategy, indexed by rebalance date.
    """
    import pandas as pd
    import numpy as np

    rebalance_returns = rebalance_date_close_prices.pct_change().dropna()

    portfolio_returns = {}
    for rebalance in factor.index[1:]:

        n_long_short = int(.2 * int(len(rebalance_date_close_prices.columns)))
        

        sorted_factors = factor.loc[rebalance].sort_values()
        
        top20p = sorted_factors.index[-n_long_short:]
        bottom20p = sorted_factors.index[:n_long_short]

        rebalance_longs_return = []
        rebalance_shorts_return = []
        for long in top20p:
            long_return = rebalance_returns[long].loc[rebalance]
            rebalance_longs_return.append(long_return)
 
        for short in bottom20p:
            short_return = rebalance_returns[short].loc[rebalance]
            rebalance_shorts_return.append(short_return)


        rebalance_longs_avg_return = np.average(rebalance_longs_return)
        rebalance_shorts_avg_return = np.average(rebalance_shorts_return)

        portfolio_returns[rebalance] = rebalance_longs_avg_return - rebalance_shorts_avg_return
    
    portfolio_returns = pd.Series(portfolio_returns)
    
    portfolio_returns.to_csv('results/portfolio_returns.csv')
    return portfolio_returns
