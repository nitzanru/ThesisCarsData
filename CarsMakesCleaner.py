import csv
import numpy as np
from CSVReader import CSVReader
from Tools import Tools
from WriteType4MakesWithAppearancesToFile import WriteType4MakesWithAppearancesToFile

# remove all class types that aren't 4
# read original file and write clean map of makers with appearances to temp file (without weird chars ./- and multiple spaces)
# read temp file to create list of most common makers
# replace makers to common and add to a new column to the output file
# removed triumph

class CarsMakesCleaner:
    """
    # cleans the data of the make column
    # gets a src file as input (the original data), adds a column of the cleaned make and writes the result in the output file
    # builds the list of main makers: makers that appear more than 2000 times (reads all makers and appearances from a file that it created in the previous step)
    original_file - the original file of data
    original_file_with_clean_makes - output file to write original data with new column of clean makes
    makes_with_appearances_file - output file to write map of makers with appearances
    """

    def __init__(self, original_file, makes_with_appearances_file, original_file_with_clean_makes, write_all_lines):
        self.write_clean_makes_with_appearances(original_file, makes_with_appearances_file)
        self.main_makers = self.load_main_makers(makes_with_appearances_file, 2000)     # the makers that appear more than 2000 times
        self.add_final_clean_makes_to_file(original_file, original_file_with_clean_makes, write_all_lines)

    def add_final_clean_makes_to_file(self, original_file, output_file_with_clean_makes, write_all_lines):
        """
        given the original data and the list of most common makes - replace the makes to the main and add the result in a new column
        :param original_file: original data
        :param output_file_with_clean_makes: original data with clean makes
        """
        reader = CSVReader(original_file)
        self.gen = reader.read_chunks()
        self.clean_file = open(output_file_with_clean_makes, newline='', mode='w', encoding='UTF-8')
        self.writer = csv.writer(self.clean_file)
        # in order to write the headers, we must do this
        self.write_headers(write_all_lines)
        self.replace_makes_to_main_makes(write_all_lines)

    def write_clean_makes_with_appearances(self, original_file, makes_with_appearances_file):
        """
        read original file and write clean map of makers with appearances to temp file
        (only type 4 rows and clean make - all lowered case and without weird chars ./- or multiple spaces)

        :param original_file: the original data
        :param makes_with_appearances_file: the output file to write clean map of makers with appearances
        """
        writer = WriteType4MakesWithAppearancesToFile(original_file)
        writer.parse_column(makes_with_appearances_file, Tools.ORIGINAL_MAKE_COLUMN)

    def write_headers(self, write_all_lines):
        chunk = next(self.gen)
        self.headers = chunk.columns
        self.headers = np.insert(self.headers, Tools.CLEAN_MAKE_COLUMN, 'clean_make')   # index of clean make is 9
        # self.headers = np.insert(self.headers, 11, 'clean model')   # index of clean model is 11
        self.writer.writerow(self.headers)
        self.replace_makes_to_main_makes_of_chunk(chunk, write_all_lines)

    def replace_makes_to_main_makes(self, write_all_lines):
        while True:
            try:
                chunk = next(self.gen)
                self.replace_makes_to_main_makes_of_chunk(chunk, write_all_lines)
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.clean_file.close()

    def replace_makes_to_main_makes_of_chunk(self, chunk, write_all_lines):
        """
        goes line by line in the chunk, adds a column with the cleaned make and writes the new line in the destined file
        """
        # clean_chunk = pd.DataFrame(columns=self.headers)
        for row in chunk.values:
            try:
                cleaned = False
                make = row[Tools.ORIGINAL_MAKE_COLUMN]
                try:
                    make_cleaned = Tools.clean_make(make)
                    for main_make in self.main_makers:
                        if main_make in make_cleaned:
                            make_cleaned = main_make
                            cleaned = True
                            break
                    if write_all_lines:    # if we need to write all lines (even not clean)
                        row = np.insert(row, Tools.CLEAN_MAKE_COLUMN, make_cleaned)
                        self.writer.writerow(row)
                    else:    # if we need to write only clean lines (ignore not clean)
                        if cleaned:     # if the line was cleaned
                            row = np.insert(row, Tools.CLEAN_MAKE_COLUMN, make_cleaned)
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

    # @staticmethod
    # def clean_symbols(make):
    #     """
    #     changes the make to be lower cased and cleans the symbols of the make - removes '-' ',' and spaces
    #     returns the clean make
    #     """
    #     try:
    #         parsed = make.lower()
    #     except AttributeError:  # no maker (nan)
    #         return make
    #     parsed = parsed.replace('-', ' ')
    #     parsed = parsed.replace(',', ' ')
    #     parsed = parsed.replace(';', ' ')
    #     parsed = parsed.replace('/', ' ')
    #     parsed = parsed.replace('\\', ' ')
    #     parsed = ' '.join(parsed.split())   # replace multiple spaces by one
    #     return parsed

    #
    # def clean_model(self, model):
    #     model_clean_symbols = self.clean_symbols(model)
    #     return model_clean_symbols

    def load_main_makers(self, makes_with_appearances_file, min_appearances):
        """
        builds a list of all makes that appear more than appearances times
        (the makes are assumed to be clean already)
        :param makes_with_appearances_file: the file that contains all makes and appearances (created in the previous step)
        :param min_appearances: the threshold
        :return: list of main makes
        """
        makers_reader = CSVReader(makes_with_appearances_file)
        makers_gen = makers_reader.read_line_by_line()
        main_makers = []
        while True:
            try:
                row = next(makers_gen)
                times = row.split(',')[1]
                if int(times) > min_appearances:
                    main_makers.append(row.split(',')[0])
            except UnicodeDecodeError:
                print('error - bad line')
            except Exception:   # empty line - stop
                break
        print('main makers:', main_makers)
        return main_makers
