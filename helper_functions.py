import pandas as pd
from pandas import dataframe

def null_count(df):
    """" checks dataframe for missing nulls and returns the number of missing values"""
    print(df.isnull().sum().sum())


def split_dates(date_series):
    """" Function to split dates of format "MM/DD/YYYY" into multiple columns
    (df['month'], df['day'], df['year'])
    and then return the same dataframe with those additional columns."""

    df = dataframe
    date_series = df.date_series
    df['day'] = pd.DatetimeIndex(date_series).day
    df['month'] = pd.DatetimeIndex(date_series).month
    df['year'] = pd.DatetimeIndex(date_series).year
    return df
