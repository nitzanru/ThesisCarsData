import csv
from CSVReader import CSVReader

class CarsDataCleaner:
    """
    cleans the data
    gets a src file as input (in this case, already partially cleaned), updates the make and writes the result in the output file
    builds the list of main makers: makers that appear more than 10000 times (reads all makers and appearances from a file)
    """
    def __init__(self, src, dest, makers_file):
        self.main_makers = self.build_main_makers(makers_file, 10000)     # the makers that appear more than 10000 times
        print(sorted(self.main_makers))

        reader = CSVReader(src)
        self.gen = reader.read_chunks()

        self.cleaned_file = open(dest, newline='', mode='w', encoding='UTF-8')
        self.writer = csv.writer(self.cleaned_file)
        # in order to write the headers, we must do this
        chunk = next(self.gen)
        self.writer.writerow(chunk.columns)
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
        self.cleaned_file.close()

    def clean_chunk(self, chunk):
        """
        goes line by line in the chunk, updates the make and writes the new line in the destined file
        """
        for row in chunk.values:
            make_cleaned = self.clean_make(row[8])
            row[8] = make_cleaned
            self.writer.writerow(row)
        print('cleaned chunk')

    def clean_make(self, make):
        """
        check if the make is too detailed and return the "short" name of the make
        e.g honda civic is too detailed, it will be returned as honda
        """
        try:
            for main_make in self.main_makers:
                if main_make in make:
                    return main_make
        except Exception:
            return make
        return make

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
