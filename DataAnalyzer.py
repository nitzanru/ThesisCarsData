import pandas as pd


class DataAnalyzer:

    def __init__(self, file):
        df = pd.read_csv(file)
        df.info(verbose=True)
        df.head()