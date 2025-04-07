import pandas as pd
import numpy as np

# Create mock data
np.random.seed(42)

# Number of samples
n_samples = 100

# Independent variables
X_mock = pd.DataFrame(
    {
        "column1": np.random.randn(n_samples),
        "column2": np.random.randn(n_samples),
        "column3": np.random.randn(n_samples),
    }
)

# Dependent variable with balanced classes
y_mock = np.random.choice([0, 1], size=n_samples)

# Create a DataFrame
data_mock = X_mock.copy()
data_mock["target_column"] = y_mock

# Save to CSV (if needed)
data_mock.to_csv("mock_data.csv", index=False)

# Print a few rows of the data
print(data_mock.head())
