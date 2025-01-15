"""This func cleans the data unsing the module data.preprocessing
"""
import yaml
from utils.data.preprocessing import (
    read_data_frame,
    pre_process_df,
    removing_outliers,
    save_data,
)


def main():
    """Cleans and preprocess raw data and save it in processed"""
    with open("params.yaml", "r") as file:
        params = yaml.safe_load(file)
    df_mining_process_flotation_plant_database = read_data_frame(
        params["data_cleaning"]["raw_data_path"]
    )
    df_processed = pre_process_df(df_mining_process_flotation_plant_database)
    df_removed_outliers = removing_outliers(df_processed)
    save_data(df_removed_outliers,
              params["data_cleaning"]["processed_data_path"])


if __name__ == "__main__":
    main()
