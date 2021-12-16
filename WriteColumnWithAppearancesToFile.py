import csv

from CSVReader import CSVReader
 # makers= 8
# cylinder capacity 12
class WriteColumnWithAppearancesToFile:
    """
    helper class to write to file all the column data and how many times each of them appears
    gets input file and output file paths and column index to read
    """

    def __init__(self, src, dest, column):
        reader = CSVReader(src)
        self.gen = reader.read_line_by_line()
        value_appearances = {}  # each value and how many time it repeats
        next(self.gen)  # header, don't parse
        while True:
            try:
                row = next(self.gen)
                value = row.split(',')[column]
                if value in value_appearances.keys():
                    value_appearances[value] = value_appearances[value] + 1
                else:
                    value_appearances[value] = 1
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        # makers = {'mazda':2, 'honda':15, 'fiat':1}
        self.write_to_file(dest, value_appearances)

    def write_to_file(self, file_name, dict_to_print):
        sorted_dict = dict(sorted(dict_to_print.items(), key=lambda item: item[1]))
        with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in sorted_dict.items():
                writer.writerow([key, value])
