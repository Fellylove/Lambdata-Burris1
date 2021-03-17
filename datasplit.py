import pandas as pd
from pandas import dataframe


def split_dates(date_series):
    df = dataframe
    date_series = df[date_series]
    df['day'] = pd.DatetimeIndex(date_series).day
    df['month'] = pd.DatetimeIndex(date_series).month
    df['year'] = pd.DatetimeIndex(date_series).year

    print(df)