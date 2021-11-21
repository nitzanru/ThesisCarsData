class LineByLineReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_lines(self):
        for row in open(self.file_name, 'r', encoding="utf-8"):
            yield row
