import pandas as pd


def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data


def display_dataset_info(data):
    print("Dataset Information:")
    print(data.info())

    print("\nFirst 5 rows:")
    print(data.head())