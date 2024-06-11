import numpy as np

# Assigned parameters
stock_price = 100.0
annual_volatility = 0.20
annual_interest_rate = 0.05
simulation_horizon = 1.0
num_simulations = 100000

# Time parameters
num_periods = int(simulation_horizon * 252)  # 252 trading days per year
dt = simulation_horizon / num_periods

# Simulate the stock price over time using geometric Brownian motion
np.random.seed(42)
stock_prices = np.zeros((num_simulations, num_periods + 1))
stock_prices[:, 0] = stock_price
for t in range(1, num_periods + 1):
    stock_prices[:, t] = stock_prices[:, t - 1] * np.exp(
        (annual_interest_rate - 0.5 * annual_volatility**2) * dt
        + annual_volatility * np.sqrt(dt) * np.random.normal(0, 1, num_simulations)
    )

# Calculate the payoff of the derivative based on the final stock price
payoffs = np.maximum(stock_prices[:, -1] - stock_price, 0)

# Calculate the expected value of the derivative and relevant statistical measures of uncertainty
expected_value = np.mean(payoffs)
std_err = np.std(payoffs) / np.sqrt(num_simulations)
confidence_interval = (expected_value - 1.96 * std_err, expected_value + 1.96 * std_err)

# Print the results
print("Estimated Expected Value of the Derivative:", expected_value)
print("Standard Error:", std_err)
print("95% Confidence Interval:", confidence_interval)
