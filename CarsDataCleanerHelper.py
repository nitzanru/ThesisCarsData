import csv

from CSVReader import CSVReader

class CarsDataCleanerHelper:
    """
    helper class to get to know the data, especially the columns of 'make' and 'color'
    """

    def __init__(self, file_name):
        reader = CSVReader(file_name)
        self.colors = {}
        self.makers_file = open('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\cars_last_record_edited_makers.csv', newline='', mode='w', encoding='UTF-8')
        self.writer = csv.writer(self.makers_file)
        self.gen = reader.read_chunks()
        # in order to write the headers, we must do this
        chunk = next(self.gen)
        self.writer.writerow(chunk.columns)
        self.clean_chunk(chunk)
        # number_of_rows = 1  # 49019679

    def clean(self):
        while True:
            try:
                chunk = next(self.gen)
                self.clean_chunk(chunk)
                # make = row.split(',')[8]
                # parsed_make = self.parse(make)
                # parsed_row = row.replace(make, parsed_make)
                # self.write_row(parsed_row.strip())
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.makers_file.close()
        print(self.colors)

    def clean_chunk(self, chunk):
        for row in chunk.values:
            make_cleaned = self.clean_make(row[8])
            row[8] = make_cleaned
            self.writer.writerow(row)
            color = row[10]
            if color in self.colors.keys():
                self.colors[color] = self.colors[color] + 1
            else:
                self.colors[color] = 1
        print('cleaned chunk')

    # mercedes to mercedes-benz
    def clean_make(self, make):
        try:
            parsed = make.lower()   # no maker (nan)
        except AttributeError:
            return make
        parsed = parsed.replace('-', ' ')   # put space instead of '-'
        parsed = parsed.replace(',', ' ')   # put space instead of '-'
        parsed = ' '.join(parsed.split())   # replace multiple spaces by one
        if parsed.__eq__('mercedes'):
            return 'mercedes benz'
        return parsed

    # def write_to_file(self, file_name, dict_to_print):
    #     sorted_dict = dict(sorted(dict_to_print.items(), key=lambda item: item[1]))
    #     with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
    #         writer = csv.writer(csv_file)
    #         for key, value in sorted_dict.items():
    #             writer.writerow([key, value])
