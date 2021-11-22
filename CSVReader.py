import pandas as pd


class CSVReader:
    """
    Reads the CSV file and yields the information
    supports 2 options:
    1. reads the data line by line and yields it
    2. reads the data chunk by chunk and yields it

    """

    def __init__(self, file_name):
        self.file_name = file_name

    def read_line_by_line(self):
        for row in open(self.file_name, 'r', encoding='UTF-8'):
            yield row

    def read_chunks(self):
        df = pd.read_csv(self.file_name, encoding='UTF-8', chunksize=10000000)
        for chunk in df:
            yield chunk