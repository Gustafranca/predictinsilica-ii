"""This func cleans the data unsing the module data.preprocessing
"""
import pandas as pd
import yaml
from utils.data.preprocessing import (read_data_frame,
                                     pre_process_df,
                                     date_time,
                                     removing_outliers,
                                     save_cvs_processed)


def main():
    """Clens raw data and save it in processed
    """
    df = read_data_frame("C:/Users/gfalmeida2/Desktop/Estudo/venv/data/"+
                    "raw/MiningProcess_Flotation_Plant_Database.csv")
    df = date_time(df)
    df = pre_process_df(df)
    df = removing_outliers(df)
    save_cvs_processed(df,"C:/Users/gfalmeida2/Desktop/Estudo/venv/data/"+
    "processed/Cleaned_MiningProcess.csv")

if __name__ == "__main__":
    main()
