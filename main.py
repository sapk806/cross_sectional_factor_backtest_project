from config import CONFIG
from src.gather_data import gather_data
from src.find_factor import find_factor
from src.strategy import strategy
from src.analysis import analysis
from src.plotter import plotter

def main():
    universe = CONFIG['universe']
    start_date = CONFIG['start_date']
    end_date = CONFIG['end_date']

    close_prices, rebalance_trading_dates = gather_data(universe = universe, start_date = start_date, end_date = end_date)
    rebalance_date_close_prices, factor = find_factor(close_prices = close_prices, rebalance_trading_dates = rebalance_trading_dates)
    portfolio_returns = strategy(factor = factor, rebalance_date_close_prices = rebalance_date_close_prices)
    cumreturn, t_value, sharpe_ratio, max_drawdown, maximums, t_value_significance, cumreturns = analysis(portfolio_values = portfolio_returns)
    plotter(cumulative_returns = cumreturns, maximums = maximums)

    print('REPORT:')
    print(f"Cumulative Return: {round(cumreturn * 100, 2)}%")
    print(f"Sharpe Ratio: {round(sharpe_ratio, 2)}")
    print(f"Max Drawdown: {round(max_drawdown * 100, 2)}%")
    print(f"t-value: {round(t_value, 2)}")
    print(f"t-value Interpretation: {t_value_significance}")

if __name__ == '__main__':
    main()