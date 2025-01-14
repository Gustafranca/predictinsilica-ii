"""model evaluation"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib


def load_data(features_path, target_path):
    """Carrega os dados de features e o target."""
    features = pd.read_csv(features_path)
    target = pd.read_csv(target_path)
    return features, target


def evaluate_model(features, target):
    """Avalia o modelo usando métricas apropriadas."""
    model = joblib.load("models/linear_regression_model.pkl")
    predictions = model.predict(features)
    mse = mean_squared_error(target, predictions)
    r2 = r2_score(target, predictions)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")


def main():
    """evaluation"""
    features_path = "data/interim/train_features.csv"
    target_path = "data/interim/train_target.csv"
    features, target = load_data(features_path, target_path)
    evaluate_model(features, target)


if __name__ == "__main__":
    main()
