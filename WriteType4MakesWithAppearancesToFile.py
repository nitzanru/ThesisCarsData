# cylinder capacity 13
from WriteColumnWithAppearancesToFile import WriteColumnWithAppearancesToFile


class WriteType4MakesWithAppearancesToFile(WriteColumnWithAppearancesToFile):
    """
    helper class to write to file all the make column data (after basic cleaning of chars and lower case)
    and how many times each of them appears. Take only data of test_class_id = 4.
    gets input file and output file paths and column index to read
    """

    def parse_column(self, output_file, column):
        value_appearances = {}  # each value and how many time it repeats
        chunk = next(self.gen)
        for row in chunk.values:
            try:
                test_class_id = row[3]
                if test_class_id == 4:  # only if it's a private car
                    make = row[column]
                    cleaned_make = self.clean_value(make)
                    if cleaned_make in value_appearances.keys():
                        value_appearances[cleaned_make] = value_appearances[cleaned_make] + 1
                    else:
                        value_appearances[cleaned_make] = 1
            except UnicodeDecodeError:
                print('error - bad line')
            except StopIteration:
                break
        self.write_to_file(output_file, value_appearances)

    def clean_value(self, value):
        return self.clean_make(value)

    @staticmethod
    def clean_make(make):
        """
        check if the make is too detailed and return the "short" name of the make
        e.g honda civic is too detailed, it will be returned as honda
        :return: make as clean as possible - no weird chars and one of the main makes if possible
        """
        try:
            make_clean_symbols = WriteColumnWithAppearancesToFile.clean_symbols(make)
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
        except Exception:
            return make_clean_symbols
        return make_clean_symbols
