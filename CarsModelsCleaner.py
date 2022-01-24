import csv

import numpy as np

from BuildMakeModelMap import BuildMakeModelMap
from CSVReader import CSVReader
from Tools import Tools


# read input file and write clean map of makers - models with appearances to temp file (without weird chars ./- and multiple spaces)
# read temp file to create list of most common makers - models
# replace models to common and add to a new column to the output file


class CarsModelsCleaner:
    """
    # cleans the data of the model column
    # gets a src file as input (the data with clean makes), adds a column of the cleaned model and writes the result in the output file
    # builds the dictionary of makers and main models: models that appear more than 20 times (reads all makers and appearances from a file)
    input_file - the data file with clean makes
    output_file - output file to write data with a new column of clean models
    main_make_models_file - output file to write map of makers with models
    """
    def __init__(self, input_file, output_file, main_make_models_file):
        self.main_makers_models = self.build_clean_makes_models_with_appearances(input_file, main_make_models_file, 20)
        #self.add_final_clean_models_to_file(input_file, output_file)

    def add_final_clean_models_to_file(self, original_file, output_file_with_clean_makes):
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
        self.write_headers()
        self.replace_makes_to_main_makes()

    def build_clean_makes_models_with_appearances(self, input_file, output_file, min_appearances):
        """
        read original file and write clean map of makers with appearances to temp file
        (only type 4 rows and clean make - all lowered case and without weird chars ./- or multiple spaces)

        :param input_file: the data with clean makes
        :param makes_models_with_appearances_file: the output file to write clean map of makers - models with appearances
        """
        builder = BuildMakeModelMap(input_file)
        builder.build_main_models(min_appearances)
        builder.write_to_file(output_file)
        return builder.get_make_models_map()

    def write_headers(self):
        chunk = next(self.gen)
        self.headers = chunk.columns
        self.headers = np.insert(self.headers, Tools.CLEAN_MODEL_COLUMN, 'clean make')
        self.writer.writerow(self.headers)
        self.replace_models_to_main_models_of_chunk(chunk)

    def replace_makes_to_main_makes(self):
        while True:
            try:
                chunk = next(self.gen)
                self.replace_models_to_main_models_of_chunk(chunk)
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.clean_file.close()

    def replace_models_to_main_models_of_chunk(self, chunk):
        """
        goes line by line in the chunk, adds a column with the cleaned make and writes the new line in the destined file
        """
        for row in chunk.values:
            try:
                make = row[Tools.CLEAN_MAKE_COLUMN]
                model = row[Tools.ORIGINAL_MODEL_COLUMN]
                try:
                    model_cleaned = Tools.clean_model(model)
                    models_with_appearances_of_make = self.main_makers_models[make]      # list of all models of current make
                    for model_with_appearances in models_with_appearances_of_make:
                        main_model = model_with_appearances[0]     # take only the model name, without the appearances
                        if model_cleaned in main_model:
                            model_cleaned = main_model
                            if main_model not in model_cleaned:
                                print("changed ", model_cleaned, " to ", main_model)
                            break
                    row = np.insert(row, Tools.CLEAN_MODEL_COLUMN, model_cleaned)
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

    def load_main_makers_models(self, makes_models_with_appearances_file, min_appearances):
        """
        builds a list of all makes that appear more than appearances times
        (the makes are assumed to be clean already)
        :param makes_with_appearances_file: the file that contains all makes and appearances (created after parsing)
        :param min_appearances: the threshold
        :return: list of main makes
        """
        makers_reader = CSVReader(makes_models_with_appearances_file)
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
