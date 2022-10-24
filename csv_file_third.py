import csv
import os
import shutil
import random
from csv_file_first import get_way_to_files
from typing import List


def write_into_csv(way_to_dataset: str, way_to_files: List, name: List) -> None:
    """

    :param way_to_dataset: way to folder "dataset"
    :param way_to_files: ways to each file in folder
    :param name: names of images
    :return: None
    """
    num_names = get_way_to_files(way_to_dataset, name)[1]
    with open("dataset_csv_third", 'w+', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(way_to_files)):
            if i < num_names[0]:
                file_writer.writerow(
                    [f'{way_to_files[i]}', f'  dataset_all_names/{os.path.basename(way_to_files[i])}',
                     name[0]])
            else:
                file_writer.writerow(
                    [f'{way_to_files[i]}', f'  dataset_all_names/{os.path.basename(way_to_files[i])}',
                     name[1]])


def get_way_to_files3(way_to_dataset: str, name: List) -> List:
    """

    :param way_to_dataset: way to folder "dataset"
    :param name: names of images
    :return: list of ways to files
    """
    num_names = get_way_to_files(way_to_dataset, name)[1]
    ways_to_files = get_way_to_files(way_to_dataset, name)[0]
    ways_to_files_second = list()
    for file in ways_to_files:
        file = "../python2.1/dataset" + "/" + file
        i = random.randint(0, 10000)
        way_to_file = os.path.abspath("../python2.1") + "/" + f'dataset_random_num/{i:04}.jpg '
        ways_to_files_second.append(way_to_file)
        shutil.copyfile(file, way_to_file)
    return ways_to_files_second


if __name__ == '__main__':
    name = ['tiger', 'leopard']
    if os.path.isdir('../python2.1/dataset_random_num') == 1:
        shutil.rmtree('../python2.1/dataset_random_num')
    os.mkdir('../python2.1/dataset_random_num')
    way_to_dataset = os.path.abspath("../python2.1/dataset")
    ways_to_files = get_way_to_files3(way_to_dataset, name)

    write_into_csv(way_to_dataset, ways_to_files, name)

    print("Работа окончена(часть 3)")
