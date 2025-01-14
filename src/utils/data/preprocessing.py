"""
This module contains functions to preprocess the data
"""

import logging
import pandas as pd
import os


def read_data_frame(file_path: str) -> pd.DataFrame:
    """reading df

    Args:
        file_path (str): file path of the data frame

    Returns:
        pd.DataFrame: return the df
    """
    df = pd.read_csv(file_path, decimal=",")
    return df


def pre_process_df(df: pd.DataFrame) -> pd.DataFrame:
    """ "
    Preprocess the data frame by converting object columns to numeric and
     removing missing values from the data frame.
    This function performs the following steps:
    2. Identifies columns with data type 'object' and replaces commas
      with dots in these columns.
    3. Converts the object columns to numeric, coercing errors to NaN.
    4. Attempts to convert a column named 'date' to datetime format,
    if it exists.
    6. Checks for missing values in the DataFrame and removes rows with
     any missing values.
    Args:
        df (pd.DataFrame): The input dataset to be preprocessed.
    Returns:
        pd.DataFrame: The preprocessed DataFrame with appropriate
        data types and no missing values.
    """
    df_process = df.copy()
    object_cols = df_process.select_dtypes(include=["object"]).columns
    df_process[object_cols] = df_process[object_cols].replace(",", ".", regex=True)
    for col in object_cols:
        df_process[col] = pd.to_numeric(df_process[col], errors="coerce")
    if col in object_cols == "date":
        try:
            df_process[col] = pd.to_datetime(df_process[col])
        except Exception as e:
            print("Error converting 'date' column" + e)
    logging.info(f"Columns data type {df_process.dtypes}")
    # check for nan or missing values and remove them
    print("Missing values in the data")
    print(df_process.isnull().sum())
    df_process.dropna(inplace=True)
    print("Processed")
    print(df.info())

    return df_process


def date_time(df: pd.DataFrame) -> pd.DataFrame:
    """data column standardization"""
    if "date" in df.columns:
        try:
            df["date"] = pd.to_datetime(df["date"])
            print("changed")
        except Exception as e:
            print("Error converting 'date'column" + e)
    else:
        print("No column named 'date' found it")
    return df


def removing_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Remove outliears from all numerical columns in df using IQR method.

    Args:
        df (pd.Dataframe): Df from whitch to remove outliears

    Returns:
        pd.DataFrame: A dataframe without outliears in numeric columns
    """
    df_clean = df.copy()

    for column in df_clean.select_dtypes(include=["number"]).columns:
        Q1 = df_clean[column].quantile(0.25)
        Q3 = df_clean[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_clean = df_clean.loc[
            (df_clean[column] >= lower_bound) & (df_clean[column] <= upper_bound)
        ]
    print("outliears have been removed")
    return df_clean


def save_cvs_processed(df: pd.DataFrame, file_path: str) -> None:
    """Saving the processed DataFrame
    Args:
        df (pd.DataFrame): DataFrame to be saved
        file_path (str): File path
    """
    try:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.mkdir(directory)
        df.to_csv(file_path, index=False)
        print("Data saved  to" + file_path)
    except Exception as e:
        print(f"An error occured while saving the DataFrame {e}")


def spliting_data(
    df: pd.DataFrame, train_start: str, test_start: str, train_end: str, test_end: str
) -> pd.DataFrame:
    """Split the data into train and test sets

    Args:
        df (pd.DataFrame): Dataframe to split
        train_size (float, optional): Size of the training set. Defaults to 0.8.

    Returns:
        pd.DataFrame: train and test dataframes
    """
    train_data = df[(df["date"] >= train_start) & (df["date"] <= train_end)]
    test_data = df[(df["date"] >= test_start) & (df["date"] <= test_end)]
    return train_data, test_data


def save_data(data, out_path):
    """Salva os dados processados."""
    data.to_csv(out_path, index=False)


def check_data_load(train_path: str, test_path: str):
    """Carrega os dados de treinamento e teste."""
    train_data = pd.read_csv(train_path)
    if test_path:
        test_data = pd.read_csv(test_path)
        return train_data, test_data
    print("Data loading completed. Processed data is saved.")
    return train_data
