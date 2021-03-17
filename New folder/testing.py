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

    @property
    def split_dates(self):
        return
        df['year'] = pd.DatetimeIndex.date_series.year
        df['month'] = pd.DatetimeIndex.date_series.month
        df['day'] = pd.DatetimeIndex.date_series.year
