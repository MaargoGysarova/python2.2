from Laba3.get_one_way import main


class SimpleIterator:
    def __init__(self, class_name, file_name):  # метка класса, имя файла csv
        self.num = -1
        self.counter = -1
        self.class_name = class_name
        self.file_name = file_name
        self.rows = []
        if self.class_name == 'tiger':
            self.rows = main(0)[0]
            self.num = main(0)[1]
        else:
            self.rows = main(1)[0]
            self.num = main(1)[1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num:
            self.counter += 1
            return self.rows[self.counter]
        else:
            print("None")
            raise StopIteration


if __name__ == '__main__':
    it = SimpleIterator("tiger", "dataset_csv_first")
    for i in range(0, 200):
        print(next(it))
