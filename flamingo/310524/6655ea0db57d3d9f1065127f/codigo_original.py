import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    data = data.dropna()
    X = data.drop("price", axis=1)
    y = data["price"]
    return X, y


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return model, mse


if __name__ == "__main__":
    file_path = "housing_data.csv"
    data = load_data(file_path)
    X, y = preprocess_data(data)
    model, mse = train_model(X, y)
    print(f"Model trained with Mean Squared Error: {mse}")
