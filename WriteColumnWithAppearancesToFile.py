import csv
from CSVReader import CSVReader
# cylinder capacity 13
from Tools import Tools


class WriteColumnWithAppearancesToFile:
    """
    helper class to write to file all the column data (after basic cleaning of chars) and how many times each of them appears
    gets input file and output file paths and column index to read
    """

    def __init__(self, input_file):
        reader = CSVReader(input_file)
        self.gen = reader.read_chunks()

    def parse_column(self, output_file, column):
        value_appearances = {}  # each value and how many time it repeats
        chunk = next(self.gen)
        for row in chunk.values:
            try:
                # row = next(self.gen)
                value = row[column]
                cleaned_value = self.clean_value(value)
                if cleaned_value in value_appearances.keys():
                    value_appearances[cleaned_value] = value_appearances[cleaned_value] + 1
                else:
                    value_appearances[cleaned_value] = 1
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.write_to_file(output_file, value_appearances)

    def clean_value(self, value):
        return Tools.clean_symbols(value)

    def write_to_file(self, file_name, dict_to_print):
        sorted_dict = dict(sorted(dict_to_print.items(), key=lambda item: item[1]))
        with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in sorted_dict.items():
                writer.writerow([key, value])




