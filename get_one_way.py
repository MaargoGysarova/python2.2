import os
import random
from typing import List


def get_way(name: List, num_of_file: int ) -> str:
    """

    :param name: names of images
    :param num_of_file: num of images
    :return: way to file
    """
    way_to_dataset = os.path.abspath("../python2.1/dataset")
    return f'{way_to_dataset}/{name}/{num_of_file:04}.jpg'


if __name__ == '__main__':
    way_to_dataset = os.path.abspath("../python2.1/dataset")
    name = ['tiger', 'leopard']
    print("tiger-1 leopard-2")
    i = int(input())
    folder_way = way_to_dataset + '/' + name[i]
    num_of_files = os.listdir(folder_way)
    for file in range(1, len(num_of_files) + 1):
        print(get_way(name[0], random.randint(0, len(num_of_files))))
        file += 1

