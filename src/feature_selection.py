"""
This script performs feature engineering on training and test datasets.
Functions:
    feature_engineering(data: pd.DataFrame) -> pd.DataFrame:
    Executes feature engineering on the given data by scaling numeric columns.
    main():
        Main function that configures logging, loads parameters, loads data,
        applies feature engineering, and saves the processed data.
Usage:
Run this script as the main module to execute the feature engineering process
    on the training and test datasets specified in the parameters file.
    None

Returns:
    _type_: _description_
"""
import pandas as pd
import logging
import yaml
from sklearn.preprocessing import StandardScaler
from utils.dvc.params import get_params
from utils.dvc.dvclogging import configure_logging
from utils.data.preprocessing import save_data, check_data_load


def feature_engineering(data):
    """Executa a engenharia de características nos dados."""
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
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


def main():
    """Executa a engenhência de características
    nos dados de treinamento e teste."""
    configure_logging()
    logging.info("Feature Selection")
    feature_selection = get_params("feature_selection")
    feature_selection_path = feature_selection["path"]
    train_path = feature_selection_path["train_path"]
    test_path = feature_selection_path["test_path"]
    train_out_path = feature_selection_path["train_out_path"]
    test_out_path = feature_selection_path["test_out_path"]

    train_data, test_data = check_data_load(train_path, test_path)

    processed_train_data = feature_engineering(train_data)
    processed_test_data = feature_engineering(test_data)

    save_data(processed_train_data, train_out_path)
    save_data(processed_test_data, test_out_path)


if __name__ == "__main__":
    main()
