"""_summary_

Returns:
    _type_: _description_
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(train_path, test_path=None):
    """Carrega os dados de treinamento e teste."""
    train_data = pd.read_csv(train_path)
    if test_path:
        test_data = pd.read_csv(test_path)
        return train_data, test_data
    return train_data


def feature_engineering(data):
    """Executa a engenharia de características nos dados."""

    scaler = StandardScaler()
    numeric_cols = [
        "% Silica Feed",
        "Amina Flow",
        "Ore Pulp pH",
        "Flotation Column 01 Air Flow",
        "Flotation Column 02 Air Flow",
        "Flotation Column 03 Air Flow",
    ]

    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

    return data


def save_data(data, out_path):
    """Salva os dados processados."""
    data.to_csv(out_path, index=False)


def main():
    """_summary_"""
    train_path = "data/interim/train_MiningProcess.csv"
    test_path = "data/interim/test_MiningProcess.csv"
    train_out_path = "data/interim/train_features.csv"
    test_out_path = "data/interim/test_features.csv"

    train_data, test_data = load_data(train_path, test_path)

    processed_train_data = feature_engineering(train_data)
    processed_test_data = feature_engineering(test_data)

    save_data(processed_train_data, train_out_path)
    save_data(processed_test_data, test_out_path)


if __name__ == "__main__":
    main()
