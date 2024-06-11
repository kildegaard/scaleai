import pandas as pd

# Creating a mock dataset
data = {
    "feature1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "feature2": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    "feature3": [5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
    "price": [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
}

# Converting the dictionary to a DataFrame
mock_data = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
mock_data.to_csv("housing_data.csv", index=False)
