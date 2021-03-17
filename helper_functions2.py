import pandas as pd

class my_dataframe:
    """" checks dataframe for missing nulls and returns the number of missing values.
    dataframe should be called df"""

    def __init__(self, df):
        self.df = df

    def null_count(self):
        return self.df.isnull().sum().sum()


class dataframe:
    """" Function to split dates of format "MM/DD/YYYY" into multiple columns
    (df['month'], df['day'], df['year'])
    and then return the same dataframe with
    those additional columns. dataframe must have
    column called date_series"""

    def __init__(self, df):
        self.df = df

    def date_series(self):
        return self.df.date_column

    def split_dates(self):
        self.df['year'] = pd.DatetimeIndex.date_series.year
        self.df['month'] = pd.DatetimeIndex.date_series.month
        self.df['day'] = pd.DatetimeIndex.date_series.year

        return self.df
