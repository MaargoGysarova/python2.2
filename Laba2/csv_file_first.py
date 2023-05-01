import csv
import os
from typing import List


def write_into_csv(way_to_dataset: str, ways_to_files: List) -> None:
    """

    :param way_to_dataset: way to folder "dataset"
    :param ways_to_files: ways to each file in folder
    :return: None
    """
    with open("dataset_csv_first", 'w+', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(ways_to_files)):
            way_to_file = f'dataset/{ways_to_files[i]}'
            file_writer.writerow(
                [f'{way_to_dataset + "/" + ways_to_files[i]}', f'  /dataset/{ways_to_files[i]}',
                 os.path.basename(os.path.dirname(way_to_file))])


def get_way_to_files(way_to_dataset: str, name: List) -> List:
    """

    :param way_to_dataset: way to folder "dataset"
    :param name: list of name images (marks)
    :return: ways to files and num of names
    """
    ways_to_files = list()
    num_names = list()
    for i in range(0, len(name)):
        folder_way = way_to_dataset + '/' + name[i]
        num_of_files = os.listdir(folder_way)  # кол-во файлов
        num_names.append(len(num_of_files))
        for file_num in range(1, len(num_of_files) - 1):
            way_to_file = name[i] + f'/{file_num:04}' + '.jpg'
            ways_to_files.append(way_to_file)

    return [ways_to_files, num_names]


def main():
    name = ['tiger', 'leopard']
    way_to_dataset = os.path.abspath("../../python2.1/dataset")
    ways_to_files = get_way_to_files(way_to_dataset, name)[0]
    write_into_csv(way_to_dataset, ways_to_files)

    print("Работа окончена(часть 1)")


if __name__ == '__main__':
    main()
