import csv

import numpy as np

from BuildMakeModelMap import BuildMakeModelMap
from CSVReader import CSVReader
from Tools import Tools


# read input file and write clean map of makers - models with appearances to temp file (without weird chars ./- and multiple spaces)
# read temp file to create list of most common makers - models
# replace models to common and add to a new column to the output file
# removed unclassified model in all makes

#todo vauxhall-opel matcher
# peugeot remove speedfight/zenith/vivacity/looxor/elystar (scooter)

class CarsModelsCleaner:
    """
    # cleans the data of the model column
    # gets a src file as input (the data with clean makes), adds a column of the cleaned model and writes the result in the output file
    # builds the dictionary of makers and main models: models that appear more than 20 times (reads all makers and appearances from a file)
    input_file - the data file with clean makes
    output_file - output file to write data with a new column of clean models
    main_make_models_file - output file to write map of makers with models
    write_all_lines - whether to write to output all lines (even not clean ones) or to write just the clean ones
    """
    def __init__(self, input_file, output_file, main_make_models_file, write_all_lines):
        self.main_makers_models = self.build_clean_makes_models_with_appearances(input_file, main_make_models_file, 100, True)
        self.add_final_clean_models_to_file(input_file, output_file, write_all_lines)

    def add_final_clean_models_to_file(self, original_file, output_file_with_clean_makes, write_all_lines):
        """
        given the original data and the list of most common makes - replace the makes to the main and add the result in a new column
        :param original_file: original data
        :param output_file_with_clean_makes: original data with clean makes
        :param write_all_lines - whether to write to output all lines (even not clean ones) or to write just the clean ones
        """
        reader = CSVReader(original_file)
        self.gen = reader.read_chunks()
        self.clean_file = open(output_file_with_clean_makes, newline='', mode='w', encoding='UTF-8')
        self.writer = csv.writer(self.clean_file)
        self.write_headers(write_all_lines)  # in order to write the headers, we must do this
        self.replace_makes_to_main_makes(write_all_lines)

    def build_clean_makes_models_with_appearances(self, input_file, output_file, min_appearances, is_absolute_appearances):
        """
        read original file and write clean map of makers with appearances to temp file
        (only type 4 rows and clean make - all lowered case and without weird chars ./- or multiple spaces)

        :param input_file: the data with clean makes
        :param output_file: the output file to write clean map of makers - models with appearances
        :param min_appearances - threshold to add model to main
        :param is_absolute_appearances - true if min_appearances is number and false if it's percentage
        """
        builder = BuildMakeModelMap(input_file)
        builder.build_main_models(min_appearances, is_absolute_appearances)
        builder.write_to_file(output_file)
        return builder.get_make_models_map()

    def write_headers(self, write_all_lines):
        chunk = next(self.gen)
        self.headers = chunk.columns
        self.headers = np.insert(self.headers, Tools.CLEAN_MODEL_COLUMN, 'clean_model')
        self.writer.writerow(self.headers)
        self.replace_models_to_main_models_of_chunk(chunk, write_all_lines)

    def replace_makes_to_main_makes(self, write_all_lines):
        while True:
            try:
                chunk = next(self.gen)
                self.replace_models_to_main_models_of_chunk(chunk, write_all_lines)
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.clean_file.close()

    def replace_models_to_main_models_of_chunk(self, chunk, write_all_lines):
        """
        goes line by line in the chunk, adds a column with the cleaned make and writes the new line in the destined file
        """
        for row in chunk.values:
            try:
                cleaned = False
                make = row[Tools.CLEAN_MAKE_COLUMN]
                model = row[Tools.ORIGINAL_MODEL_COLUMN]
                try:
                    model_cleaned = Tools.clean_model(model)
                    models_of_make = self.main_makers_models[make]      # list of all models of current make
                    for main_model in models_of_make:
                        if main_model in model_cleaned:
                            model_cleaned = main_model
                            cleaned = True
                            break
                    if write_all_lines:    # if we need to write all lines (even not clean)
                        row = np.insert(row, Tools.CLEAN_MODEL_COLUMN, model_cleaned)
                        self.writer.writerow(row)
                    else:    # if we need to write only clean lines (ignore not clean)
                        if cleaned:     # if the line was cleaned
                            row = np.insert(row, Tools.CLEAN_MODEL_COLUMN, model_cleaned)
                            self.writer.writerow(row)
                except Exception:
                    print('error1 ', row)
                    # clean_chunk = self.add_nd_array_to_data_frame(clean_chunk, row)
            except Exception:
                print('error2 ', row)
        # clean_chunk.to_csv(self.dest, encoding='utf-8', index=False)
        print('wrote clean chunk')



