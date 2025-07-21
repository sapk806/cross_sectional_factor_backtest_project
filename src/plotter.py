def plotter(cumulative_returns, maximums):
    """
    Plots the cumulative returns of the portfolio with drawdown.

    Parameters:
        cumulative_returns (pd.Series): A series containing the cumulative returns of the portfolio, indexed by rebalance date.
        maximums (pd.Series): A series containing the maximums of the portfolio, indexed by rebalance date.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize = (12, 6))
    plt.plot(cumulative_returns.index, cumulative_returns, label = 'Portfolio Values')
    plt.fill_between(cumulative_returns.index, cumulative_returns, maximums, where = maximums > cumulative_returns, label = 'Drawdowns', color = 'r', alpha = 0.2)
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.title('Portfolio Values with Drawdowns')
    plt.legend()
    plt.grid(True)

    plt.savefig('plots/portfolio_value_plot_w_drawdowns.png')

    plt.show()