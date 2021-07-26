import csv


class Reader:

    def __init__(self, file):
        self.f = open(file)

    def read(self):
        lines = csv.DictReader(self.f)
        return lines

    def close(self):
        self.f.close()

