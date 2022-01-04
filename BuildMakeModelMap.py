import csv

from CSVReader import CSVReader
 # clean makers= 9
 # models= 10
 # clean models= 11
# cylinder capacity 13
class BuildMakeModelMap:
    """
    helper class that builds a map of makes and their main models
    for example, the output will be {'honda':[['CV', 2000], ['FV', 1547]], 'suzuki':[['sx4',5471], ['swift',204]]}
    """

    def __init__(self, src, column_key, column_values):
        reader = CSVReader(src)
        self.gen = reader.read_chunks()
        self.full_make_model_map = {}  # each key and list of lists (model and #apperences) = map of make to all models
        self.make_model_map = {}    # map of make and main models only
        #next(self.gen)  # header, don't parse
        while True:
            try:
                chunk = next(self.gen)
                for row in chunk.values:
                    make = row[column_key]
                    model = self.clean_model(row[column_values])
                    if make in self.full_make_model_map.keys():   # make in map
                        found = False
                        for pair in self.full_make_model_map[make]:
                            if pair[0] == model:     # model in make's list
                                pair[1] += 1
                                found = True
                                break
                        if not found:
                            self.full_make_model_map[make].append([model, 1])
                    else:
                        self.full_make_model_map[make] = [[model, 1]]

            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        # makers = {'mazda':2, 'honda':15, 'fiat':1}
        # self.write_to_file(dest, make_model_map)

    def build_main_models(self, appearances):

        for key, values in self.full_make_model_map.items():
            models_list = []
            for model_times_pair in values:
                if model_times_pair[1] >= appearances:   # times is less than threshold
                    models_list.append(model_times_pair)
            self.make_model_map[key] = models_list

    def get_make_model_map(self):
        return self.make_model_map

    def write_to_file(self, dest_file_name):
        with open(dest_file_name, 'w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            for make, values in self.make_model_map.items():
                writer.writerow([make])
                for model_times_pair in values:
                    writer.writerow([model_times_pair[0], model_times_pair[1]])

    def clean_model(self, model):
        """
        changes the model to be lower cased and cleans the symbols - removes '-' ',' and spaces
        returns the clean make
        """
        try:
            parsed = model.lower()
        except AttributeError:  # no maker (nan)
            return model
        parsed = parsed.replace('-', ' ')
        parsed = parsed.replace(',', ' ')
        parsed = parsed.replace(';', ' ')
        parsed = parsed.replace('/', ' ')
        parsed = parsed.replace('\\', ' ')
        parsed = ' '.join(parsed.split())  # replace multiple spaces by one
        return parsed
