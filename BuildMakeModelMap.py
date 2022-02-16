import csv

from CSVReader import CSVReader
from CarsMakesCleaner import CarsMakesCleaner
from Tools import Tools


class BuildMakeModelMap:
    """
    helper class that builds a map of makes and their main models
    # need to clean the models - remove weird chars
    for example, the output will be {'honda':[['CV', 2000], ['FV', 1547]], 'suzuki':[['sx4',5471], ['swift',204]]}
    :param input_file
    """

    def __init__(self, input_file):
        reader = CSVReader(input_file)
        self.gen = reader.read_chunks()
        self.full_make_models_map = {}  # map make to models and #appearances
        self.make_models_map = {}    # final map of make to main models only (no appearances)
        while True:
            try:
                chunk = next(self.gen)
                for row in chunk.values:
                    make = row[Tools.CLEAN_MAKE_COLUMN]
                    model = row[Tools.ORIGINAL_MODEL_COLUMN]
                    clean_model = Tools.clean_model(model)
                    try:
                        if 'undefined' in clean_model or 'unclassified' in clean_model:
                            continue
                    except Exception:
                        continue
                    if make in self.full_make_models_map.keys():   # make in map
                        found = False
                        for pair in self.full_make_models_map[make]:     # pair is a model and its number of appearances
                            if pair[0] == clean_model:     # model in make's list - add appearance
                                pair[1] += 1
                                found = True
                                break
                        if not found:   # model not in make's list yet but make exists in map - add new [make-model]
                            self.full_make_models_map[make].append([clean_model, 1])
                    else:   # make not in map yet - add new [make-model]
                        self.full_make_models_map[make] = [[clean_model, 1]]
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        # makers = {'mazda':2, 'honda':15, 'fiat':1}
        # self.write_to_file(dest, make_model_map)

    def build_main_models(self, appearances, is_absolute_appearances):
        """
        build map of makes and models that appear more than appearances
        :param appearances: minimal number of times to appear
        :param is_absolute_appearances - true if min_appearances is number and false if it's percentage
        """
        for make, values in self.full_make_models_map.items():
            number_of_models = 0
            for model_times_pair in values:
                number_of_models += model_times_pair[1]
            models_list = []    # main models
            for model_times_pair in values:     # pairs of model & appearances
                if is_absolute_appearances:
                    threshold = appearances
                else:
                    threshold = (number_of_models * appearances / 100).__ceil__()   # percentage of number of models
                if model_times_pair[1] >= threshold:   # appears more than threshold (percentage)
                    models_list.append(model_times_pair[0])
            if models_list is not None and len(models_list) > 0:
                self.make_models_map[make] = models_list

    def get_make_models_map(self):
        return self.make_models_map

    def write_to_file(self, output_file):
        """
        write the dictionary of makes-models to the desired file
        """
        with open(output_file, 'w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            for make, models in self.make_models_map.items():
                writer.writerow([make])
                # for model in models:
                writer.writerow(models)

