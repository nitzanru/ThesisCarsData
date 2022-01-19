import csv
import numpy as np
from BuildMakeModelMap import BuildMakeModelMap
from CSVReader import CSVReader


# remove all class types that aren't 4
# read original file and write clean map of makers with appearances to temp file (without weird chars ./- and multiple spaces)
# read temp file to create list of most common makers
# replace makers to common and add to a new column in the original file

# read edited file with clean makers and build map of make to its clean models with appearances to temp file (without weird chars ./- and multiple spaces)
# read temp file to create list of most common makers and models
# replace models to common and add to a new column

class CarsDataCleaner:
    """
    cleans the data
    gets a src file as input (the original data), adds a column of the cleaned make and writes the result in the output file
    builds the list of main makers: makers that appear more than 10000 times (reads all makers and appearances from a file)
    """
    def __init__(self, src, dest, makers_file):
        self.dest = dest
        self.main_makers = self.build_main_makers(makers_file, 2000)     # the makers that appear more than 2000 times
        make_model_map_builder = BuildMakeModelMap('C:\\Users\\nrukhamin\\Desktop\\BGU\\thesis\\cars_last_record\\mini.csv', 9, 10)
        make_model_map_builder.build_main_models(10)
        reader = CSVReader(src)
        self.gen = reader.read_chunks()

        self.clean_file = open(dest, newline='', mode='w', encoding='UTF-8')
        self.writer = csv.writer(self.clean_file)
        # in order to write the headers, we must do this
        self.write_headers()

    def write_headers(self):
        chunk = next(self.gen)
        self.headers = chunk.columns
        self.headers = np.insert(self.headers, 9, 'clean make')   # index of clean make is 9
        self.headers = np.insert(self.headers, 11, 'clean model')   # index of clean model is 11
        self.writer.writerow(self.headers)
        self.clean_chunk(chunk)

    def clean(self):
        while True:
            try:
                chunk = next(self.gen)
                self.clean_chunk(chunk)
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.clean_file.close()

    def clean_chunk(self, chunk):
        """
        goes line by line in the chunk, adds a column with the cleaned make and writes the new line in the destined file
        """
        # clean_chunk = pd.DataFrame(columns=self.headers)
        for row in chunk.values:
            try:
                make = row[8]
                model = row[9]
                test_class_id = row[3]
                if test_class_id == 4: # only if it's a private car
                    try:
                        make_cleaned = self.clean_make(make)
                        row = np.insert(row, 9, make_cleaned)
                        model_cleaned = self.clean_model(model)
                        row = np.insert(row, 11, model_cleaned)
                        self.writer.writerow(row)
                    except Exception:
                        print('error1 ', row)
                    # clean_chunk = self.add_nd_array_to_data_frame(clean_chunk, row)
            except Exception:
                print('error2 ', row)
        # clean_chunk.to_csv(self.dest, encoding='utf-8', index=False)
        print('wrote clean chunk')

    def add_nd_array_to_data_frame(self, df, nd_array):
        data_to_append = {}
        for i in range(nd_array.size):
            data_to_append[self.headers[i]] = nd_array[i]
        df = df.append(data_to_append, ignore_index=True)
        return df


    def clean_model(self, model):
        model_clean_symbols = self.clean_symbols(model)
        return model_clean_symbols


    def clean_make(self, make):
        """
        check if the make is too detailed and return the "short" name of the make
        e.g honda civic is too detailed, it will be returned as honda
        """
        try:
            make_clean_symbols = self.clean_symbols(make)
            if 'mercedes' in make_clean_symbols or 'mcc' in make_clean_symbols:
                return 'mercedes benz'
            elif make_clean_symbols.__eq__('chrysler jeep'):
                return 'jeep'
            elif 'rover' in make_clean_symbols or 'jaguar' in make_clean_symbols:
                return 'jaguar land rover'
            elif make_clean_symbols.__eq__('mini'):
                return 'bmw'
            elif make_clean_symbols.__eq__('lexus'):
                return 'toyota'
            elif 'bedford' in make_clean_symbols:
                return 'vauxhall'
            elif 'lincoln' in make_clean_symbols:
                return 'ford'
            elif 'pontiac' in make_clean_symbols or 'general' in make_clean_symbols or 'gm ' in make_clean_symbols:
                return 'general motors'

            for main_make in self.main_makers:
                if main_make in make_clean_symbols:
                    return main_make
        except Exception:
            return make_clean_symbols
        return make_clean_symbols

    def build_main_makers(self, src, appearances):
        """
        builds a list of all makers that appear more than appearances times
        :param src: the file that contains all makers and appearances (created after parsing)
        :param appearances: the threshold
        :return:
        """
        makers_reader = CSVReader(src)
        makers_gen = makers_reader.read_line_by_line()
        main_makers = []
        while True:
            try:
                row = next(makers_gen)
                times = row.split(',')[1]
                if int(times) > appearances:
                    main_makers.append(row.split(',')[0])
            except UnicodeDecodeError:
                print('error - bad line')
            except Exception:   # empty line - stop
                break
        print('main makers:', main_makers)
        return main_makers

    @staticmethod
    def write_mini_file(original_file, output_file):
        """
        given the original data write a mini file with only 1 chunk
        """
        reader = CSVReader(original_file)
        gen = reader.read_chunks()
        clean_file = open(output_file, newline='', mode='w', encoding='UTF-8')
        writer = csv.writer(clean_file)
        chunk = next(gen)
        headers = chunk.columns
        writer.writerow(headers)
        for row in chunk.values:
            writer.writerow(row)
