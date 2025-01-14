"""Splitting data to use in ml flow
"""
import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import os
from datetime import datetime


def main():
    """Slipt the dataframe in test and train and save this data set"""
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)

    relative_path = os.path.join("data", "processed", "Cleaned_MiningProcess.csv")
    df_ml = pd.read_csv(relative_path)
    df_ml["date"] = pd.to_datetime(df_ml["date"], errors="coerce")

    test_start = datetime.strptime(
        params["data_split"]["test_start"], "%Y-%m-%d %H:%M:%S"
    )
    test_end = datetime.strptime(params["data_split"]["test_end"], "%Y-%m-%d %H:%M:%S")
    train_start = datetime.strptime(
        params["data_split"]["train_start"], "%Y-%m-%d %H:%M:%S"
    )
    train_end = datetime.strptime(
        params["data_split"]["train_end"], "%Y-%m-%d %H:%M:%S"
    )

    train_data = df_ml[(df_ml["date"] >= train_start) & (df_ml["date"] <= train_end)]
    test_data = df_ml[(df_ml["date"] >= test_start) & (df_ml["date"] <= test_end)]

    train_data.to_csv("data/interim/train_MiningProcess.csv", index=False)
    test_data.to_csv("data/interim/test_MiningProcess.csv", index=False)

    print("Data split completed. Train and test datasets are saved")


if __name__ == "__main__":
    main()
