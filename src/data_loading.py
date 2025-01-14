"""Chack if the data is loaded correctly.
"""
import pandas as pd
import os


def main():
    """loading data"""
    raw_data_path = os.path.join(
        "data", "raw", "MiningProcess_Flotation_Plant_Database.csv"
    )
    df = pd.read_csv(raw_data_path)
    processed_data_path = os.path.join(
        "data", "processed", "MiningProcess_Flotation_Plant_Database_processed.csv"
    )
    df.to_csv(processed_data_path, index=False)
    print("Data loading completed. Processed data is saved.")


if __name__ == "__main__":
    main()
