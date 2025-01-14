"""Splitting data to use in ml flow
"""
import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import os
from datetime import datetime
from utils.data.time_padronization import date_time_padronization
from utils.data.preprocessing import spliting_data, save_data


def main():
    """Slipt the dataframe in test and train and save this data set"""
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)

    relative_path = os.path.join("data", "processed", "Cleaned_MiningProcess.csv")
    df_ml = pd.read_csv(relative_path)
    df_ml["date"] = pd.to_datetime(df_ml["date"], errors="coerce")

    train_start, test_start, train_end, test_end = date_time_padronization(
        "train_start", "test_start", "train_end", "test_end"
    )
    train_data, test_data = spliting_data(
        df_ml, train_start, test_start, train_end, test_end
    )
    save_data(train_data, params["data_split"]["train_out_path"])
    save_data(test_data, params["data_split"]["test_out_path"])

    print("Data split completed. Train and test datasets are saved")


if __name__ == "__main__":
    main()
