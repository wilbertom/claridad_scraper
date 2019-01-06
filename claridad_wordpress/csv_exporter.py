import csv


class CsvExporter:

    def __init__(self, fp):
        self._csv = csv.writer(fp)
        self._csv.writerow(self.headers)

    @property
    def headers(self):
        raise NotImplementedError

    def row(self, data):
        raise NotImplementedError

    def export(self, data):
        self._csv.writerow(self.row(data))

    def get(self, field, row):
        index = self.headers.index(field)
        return row[index]
