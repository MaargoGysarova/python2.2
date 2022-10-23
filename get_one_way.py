import os
import random

def get_way(name, num_of_file ):
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

