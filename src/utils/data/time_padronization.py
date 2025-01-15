"""Module to standardize the date column in the dataset
"""
from datetime import datetime
import yaml


def date_time_padronization_train_test_split(
    train_start: str, test_start: str, train_end: str, test_end: str
) -> tuple:
    """'date' column standardization

    Args:
        point (str): date to be standardized

    Returns:
        datetime: standardized date
    """
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    train_start = datetime.strptime(
        params["data_split"][train_start], "%Y-%m-%d %H:%M:%S"
    )
    test_start = datetime.strptime(
        params["data_split"][test_start], "%Y-%m-%d %H:%M:%S"
    )
    train_end = datetime.strptime(params["data_split"][train_end],
                                  "%Y-%m-%d %H:%M:%S")
    test_end = datetime.strptime(params["data_split"][test_end],
                                 "%Y-%m-%d %H:%M:%S")
    return train_start, test_start, train_end, test_end
