import csv

from CSVReader import CSVReader


class WriteMakersWithAppearancesToFile:
    """
    helper class to write to file all the makers and how many times each of them appears
    gets input file and output file paths
    """

    def __init__(self, src, dest):
        reader = CSVReader(src)
        self.gen = reader.read_line_by_line()
        makers = {}
        next(self.gen)  # header, don't parse
        while True:
            try:
                row = next(self.gen)
                make = row.split(',')[8]
                if make in makers.keys():
                    makers[make] = makers[make] + 1
                else:
                    makers[make] = 1
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        # makers = {'mazda':2, 'honda':15, 'fiat':1}
        self.write_to_file(dest, makers)

    def write_to_file(self, file_name, dict_to_print):
        sorted_dict = dict(sorted(dict_to_print.items(), key=lambda item: item[1]))
        with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in sorted_dict.items():
                writer.writerow([key, value])
