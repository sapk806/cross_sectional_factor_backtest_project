import pandas as pd
import numpy as np

def analysis(portfolio_values: pd.Series):
    """
    Calculates performance metrics to determine strategy's efficiency.

    Performance Metrics Include:
        - Cumulative Returns
        - Sharpe Ratio
        - t-value
        - Max Drawdown

    Args:
        portfolio_values (pd.Series): Series containing the returns of the portfolio based on the strategy, indexed by rebalance date.
    
    Returns:
        float: Final cumulative return of the portfolio. Taken from the cumulative return series.
        float: t-value of the Sharpe ratio. Calculated using Sharpe ratio and the number of months.
        float: Sharpe Ratio of the portfolio. Calculated using annualized average of the returns and annualized std of the returns.
        float: Max drawdown of the portfolio, taken from the minimum of the drawdowns list.
        pd.Series: Series containing the rolling maximum values of cumulative return, indexed by rebalance date.
        str: Interpretation of the t-value and its significance.
        pd.Series: Series containing the cumulative returns of the portfolio, indexed by rebalance date.

    """

    cumreturns = (1 + portfolio_values).cumprod()
    cumreturn = cumreturns.iloc[-1] - 1

    avg_returns = np.average(portfolio_values)
    annualized_avg_returns = (1 + avg_returns)**12 - 1

    std_returns = portfolio_values.std(ddof = 1)
    annualized_std_returns = std_returns * np.sqrt(12)

    n_months = int(len(cumreturns.index))

    sharpe_ratio = annualized_avg_returns / annualized_std_returns

    t_value = sharpe_ratio * np.sqrt(n_months)
    t_value_interpretation = None
    if t_value < 1:
        t_value_interpretation = 'Not Significant'
    elif 1 <= t_value < 2:
        t_value_interpretation = 'Weak Evidence'
    elif 2 <= t_value < 3:
        t_value_interpretation = 'Statistically Significant'
    elif t_value >= 3:
        t_value_interpretation = 'Strongly Significant'
    
    drawdowns = {}
    maximums = {}
    highest_value = -np.inf
    for date in cumreturns.index:
        value = cumreturns.loc[date]
        if value > highest_value:
            highest_value = value
        current_drawdown = (value - highest_value) / highest_value
        drawdowns[date] = current_drawdown
        maximums[date] = highest_value

    drawdowns = pd.Series(drawdowns)
    maximums = pd.Series(maximums)

    max_drawdown = drawdowns.min()

    drawdowns.to_csv('results/drawdowns.csv')
    cumreturns.to_csv('results/cumulative_returns.csv')
    return cumreturn, t_value, sharpe_ratio, max_drawdown, maximums, t_value_interpretation, cumreturns