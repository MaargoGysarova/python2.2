import csv


class SimpleIterator:
    def __init__(self, class_name, file_name):  # метка класса, имя файла csv
        self.num = 0
        self.counter = -1
        self.class_name = class_name
        self.file_name = file_name
        self.rows = list()
        with open(file_name, encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == class_name:
                    self.rows.append(row[0])
                    self.num += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num:
            self.counter += 1
            return self.rows[self.counter]
        else:
            print("None")
            raise StopIteration
