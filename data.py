import pandas as pd


def load_data_by_5_minutes(file_path):
    """
    Load data from CSV file and preprocess it for 5-minute interval averages calculation.
    """
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['period_end'])
    return df
