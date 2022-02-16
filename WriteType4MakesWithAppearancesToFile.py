# cylinder capacity 13
from Tools import Tools
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
                    try:
                        if 'triumph' in cleaned_make or 'undefined' in cleaned_make or 'unclassified' in cleaned_make:
                            continue
                    except Exception:
                        continue
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
        return Tools.clean_make(value)


