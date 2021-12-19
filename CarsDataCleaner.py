import csv

import numpy as np
import pandas as pd

from CSVReader import CSVReader

class CarsDataCleaner:
    """
    cleans the data
    gets a src file as input (the original data), adds a column of the cleaned make and writes the result in the output file
    builds the list of main makers: makers that appear more than 10000 times (reads all makers and appearances from a file)
    """
    def __init__(self, src, dest, makers_file):
        self.dest = dest
        #self.main_makers = self.build_main_makers(makers_file, 10000)     # the makers that appear more than 10000 times
        # manufacturers of motorcycles, motorhomes, racing cars, taxis etc. that can be deleted
        self.makers_to_delete = ['kawasaki', 'triumph', 'piaggio', 'harley davidson', 'aprilia', 'ducati', 'lambretta', 'gilera', 'ktm', 'lotus', 'bsa', 'sym', 'tvr', 'moto guzzi', 'kymco', 'norton', 'royal enfield', 'vespa (douglas)', 'abarth', 'leyland daf', 'caterham', 'derbi', 'hyosung', 'buell', 'velocette', 'westfield', 'westfield', 'mz', 'cagiva', 'baotian', 'matchless', 'mbk', 'lexmoto', 'ccm', 'ariel', 'husqvarna', 'vespa', 'tgb', 'smc', 'metrocab', 'italjet', 'auto trail', 'mv agusta', 'jinlun', 'benelli', 'gas gas', 'malaguti', 'lifan']

        #print(sorted(self.main_makers))

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
                test_class_id = row[3]
                if test_class_id == 4: # only if it's a private car
                      #  and make not in self.makers_to_delete:   # only if it's a private car - clean and write new result
                    try:
                        make_cleaned = self.clean_make(make)
                        row = np.insert(row, 9, make_cleaned)
                        self.writer.writerow(row)
                    except Exception:
                        print('error1 ' , row)
                    # clean_chunk = self.add_nd_array_to_data_frame(clean_chunk, row)
            except Exception:
                print('error2 ' , row)
        # clean_chunk.to_csv(self.dest, encoding='utf-8', index=False)
        print('wrote clean chunk')

    def add_nd_array_to_data_frame(self, df, nd_array):
        data_to_append = {}
        for i in range(nd_array.size):
            data_to_append[self.headers[i]] = nd_array[i]
        df = df.append(data_to_append, ignore_index=True)
        return df

    def clean_make_symbols(self, make):
        """
        changes the make to be lower cased and cleans the symbols of the make - removes '-' ',' and spaces
        returns the clean make
        """
        try:
            parsed = make.lower()
        except AttributeError:  # no maker (nan)
            return make
        parsed = parsed.replace('-', ' ')   # put space instead of '-'
        parsed = parsed.replace(',', ' ')   # put space instead of '-'
        parsed = ' '.join(parsed.split())   # replace multiple spaces by one
        return parsed


    def clean_make(self, make):
        """
        check if the make is too detailed and return the "short" name of the make
        e.g honda civic is too detailed, it will be returned as honda
        """
        make_clean_symbols = self.clean_make_symbols(make)
        if 'mercedes' in make_clean_symbols:
            return 'mercedes benz'
        elif make_clean_symbols.__eq__('chrysler jeep'):
            return 'jeep'
        elif make_clean_symbols.__eq__('smart (mcc)'):
            return 'smart'
        # try:
        #     for main_make in self.main_makers:
        #         if main_make in make_clean_symbols:
        #             return main_make
        # except Exception:
        #     return make_clean_symbols
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
        return main_makers
