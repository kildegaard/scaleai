import numpy as np


def monte_carlo_simulation(
    initial_stock_price,
    annual_volatility,
    annual_interest_rate,
    horizon_in_years,
    num_simulations,
):
    # Calculate the time step
    time_step = 1.0 / (252 * horizon_in_years)

    # Calculate the mean return and volatility in terms of the time step
    mean_return = (annual_interest_rate - 0.5 * annual_volatility**2) * time_step
    volatility = annual_volatility * np.sqrt(time_step)

    # Initialize an array to store the payoffs from each simulation
    payoffs = np.zeros(num_simulations)

    # Run the simulations
    for i in range(num_simulations):
        stock_prices = np.zeros(int(252 * horizon_in_years) + 1)
        stock_prices[0] = initial_stock_price

        # Generate stock prices using geometric Brownian motion
        for j in range(1, len(stock_prices)):
            stock_prices[j] = stock_prices[j - 1] * np.exp(
                mean_return + volatility * np.random.normal()
            )

        # Calculate the payoff of the derivative based on the final stock price
        # Replace this with your own payoff function
        payoffs[i] = max(stock_prices[-1] - initial_stock_price, 0)

    # Calculate the expected value and statistical measures of uncertainty
    expected_value = np.mean(payoffs)
    standard_deviation = np.std(payoffs)
    confidence_interval = (
        expected_value - 1.96 * standard_deviation / np.sqrt(num_simulations),
        expected_value + 1.96 * standard_deviation / np.sqrt(num_simulations),
    )

    return expected_value, standard_deviation, confidence_interval


# Set the parameters
initial_stock_price = 100.0
annual_volatility = 0.20
annual_interest_rate = 0.05
horizon_in_years = 1.0
num_simulations = 100000

# Run the simulation
expected_value, standard_deviation, confidence_interval = monte_carlo_simulation(
    initial_stock_price,
    annual_volatility,
    annual_interest_rate,
    horizon_in_years,
    num_simulations,
)

# Print the results
print(f"Expected Value: {expected_value:.2f}")
print(f"Standard Deviation: {standard_deviation:.2f}")
print(
    f"95% Confidence Interval: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})"
)
