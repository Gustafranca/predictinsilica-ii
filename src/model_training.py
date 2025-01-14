"""Modelingusing linear regression algorithm"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    """Using features to train"""
    data = pd.read_csv("data/processed/Cleaned_MiningProcess.csv")
    cols_features = [
        "% Silica Feed",
        "Amina Flow",
        "Ore Pulp pH",
        "Flotation Column 01 Air Flow",
        "Flotation Column 02 Air Flow",
        "Flotation Column 03 Air Flow",
    ]
    target = "% Silica Concentrate"

    X = data[cols_features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")


if __name__ == "__main__":
    main()
