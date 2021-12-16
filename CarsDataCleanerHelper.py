import csv

from CSVReader import CSVReader

class CarsDataCleanerHelper:
    """
    helper class to get to know the data, especially the columns of 'make' and 'color'
    write to destined file the cleaned data
    """

    def __init__(self, src, dest):
        reader = CSVReader(src)
        self.cleaned_file = open(dest, newline='', mode='w', encoding='UTF-8')
        self.writer = csv.writer(self.cleaned_file)
        self.gen = reader.read_chunks()
        # in order to write the headers, we must do this
        chunk = next(self.gen)
        self.writer.writerow(chunk.columns)
        self.clean_chunk(chunk)
        self.colors = {}
        # number_of_rows = 1  # 49019679

    def clean(self):
        while True:
            try:
                chunk = next(self.gen)
                self.clean_chunk(chunk)
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.cleaned_file.close()

    def build_colors_appearances(self, chunk):
        for row in chunk.values:
            color = row[10]
            if color in self.colors.keys():
                self.colors[color] = self.colors[color] + 1
            else:
                self.colors[color] = 1
        print('parsed colors of chunk')

    def clean_chunk(self, chunk):
        """
        goes line by line in the chunk, updates the make and writes the new line in the destined file
        """
        for row in chunk.values:
            make_cleaned = self.clean_make(row[8])
            row[8] = make_cleaned
            self.writer.writerow(row)
        print('cleaned chunk')

    # remove '-' and ',' from names, leave only one space
    # mercedes to mercedes-benz
    # chrysler jeep to jeep
    # smart (mcc) to smart
    def clean_make(self, make):
        try:
            parsed = make.lower()   # no maker (nan)
        except AttributeError:
            return make
        parsed = parsed.replace('-', ' ')   # put space instead of '-'
        parsed = parsed.replace(',', ' ')   # put space instead of '-'
        parsed = ' '.join(parsed.split())   # replace multiple spaces by one

        if 'mercedes' in parsed:
            return 'mercedes benz'
        elif parsed.__eq__('chrysler jeep'):
            return 'jeep'
        elif parsed.__eq__('smart (mcc)'):
            return 'smart'
        return parsed

    # def write_to_file(self, file_name, dict_to_print):
    #     sorted_dict = dict(sorted(dict_to_print.items(), key=lambda item: item[1]))
    #     with open(file_name, 'w', newline='', encoding='UTF-8') as csv_file:
    #         writer = csv.writer(csv_file)
    #         for key, value in sorted_dict.items():
    #             writer.writerow([key, value])
