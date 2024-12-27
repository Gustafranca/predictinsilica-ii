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
    df = pd.read_csv(file_path, decimal=',')
    return df

def pre_process_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace comma data to float with a dot

    Args:
        df (pd.DataFrame): dataset

    Returns:
        pd.DataFrame: data with rights types
    """
    df_process = df.copy()
    object_cols = df_process.select_dtypes(include=['object']).columns
    df_process[object_cols] = df_process[object_cols].replace(',', '.'
                                                    ,regex=True)
    for col in object_cols:
        df_process[col] = pd.to_numeric(df_process[col], errors='coerce')
    logging.info(f"Columns data type {df_process.dtypes}")
    print('Processed')
    print(df.info())
    return df_process


def date_time(df: pd.DataFrame) -> pd.DataFrame:
    """data column standardization"""
    if 'date' in df.columns:
        try:
            df['date'] = pd.to_datetime(df['date'])
            print('changed')
        except Exception as e:
            print("Error converting 'date'column"+e)
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
        df_clean = df_clean.loc[(df_clean[column] >= lower_bound ) &
                            (df_clean[column] <= upper_bound)]
    print("outliears have been removed")
    return df_clean

def save_cvs_processed(df : pd.DataFrame, file_path: str) -> None:
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



