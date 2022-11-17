import os
import random
from typing import List


def get_way(num_of_file: int) -> str:
    """

    :param name: names of images
    :param num_of_file: num of images
    :return: way to file
    """
    way_to_dataset = os.path.abspath("../../python2.1/dataset")
    return f'{way_to_dataset}/tiger/{num_of_file:04}.jpg'


def main():
    way_to_dataset = os.path.abspath("../../python2.1/dataset")
    name = ['tiger', 'leopard']
    print("tiger-1 leopard-2")
    folder_way = way_to_dataset + '/' + name[0]
    num_of_files = os.listdir(folder_way)
    rows = []
    for file in range(1, len(num_of_files) + 1):
        rows.append(get_way(file))
        file += 1
    return rows, len(num_of_files)


if __name__ == '__main__':
    main()
