# src/utils.py

import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def basic_info(df):
    print(df.info())
    print(df.describe())