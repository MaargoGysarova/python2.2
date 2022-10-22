import csv
import os
import shutil
from csv_file_first import get_way_to_files


def write_into_csv(way_to_dataset, way_to_files, name):
    names = list()
    num_names = get_way_to_files(way_to_dataset, name)[1]
    i = 0
    with open("dataset_csv_second", 'w+', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(way_to_files)):
            if i < num_names[0]:
                way_to_file = f'dataset/{way_to_files[i]}'
                file_writer.writerow(
                    [f'{way_to_files[i]}', f'  dataset_all_names/{os.path.basename(way_to_files[i])}',
                     name[0]])
            else:
                way_to_file = f'dataset/{way_to_files[i]}'
                file_writer.writerow(
                    [f'{way_to_files[i]}', f'  dataset_all_names/{os.path.basename(way_to_files[i])}',
                     name[1]])


def get_way_to_files2(way_to_dataset, name):
    num_names = get_way_to_files(way_to_dataset, name)[1]
    ways_to_files = list()
    ways_to_files = get_way_to_files(way_to_dataset, name)[0]
    ways_to_files_second = list()
    i = 1
    for file in ways_to_files:
        file = "../python2.1/dataset" + "/" + file
        if i < num_names[0]:
            way_to_file = os.path.abspath("../python2.1") + "/" + f'dataset_all_names/{name[0]}_{i:04}.jpg'
            ways_to_files_second.append(way_to_file)
            shutil.copyfile(file, way_to_file)
            i += 1
        else:
            way_to_file = os.path.abspath("../python2.1") + "/" + f'dataset_all_names/{name[1]}_{i:04}.jpg'
            ways_to_files_second.append(way_to_file)
            shutil.copyfile(file, way_to_file)
            i += 1

    return ways_to_files_second


if __name__ == '__main__':
    name = ['tiger', 'leopard']
    if os.path.isdir('../python2.1/dataset_all_names') == 1:
        shutil.rmtree('../python2.1/dataset_all_names')
    os.mkdir('../python2.1/dataset_all_names')
    way_to_dataset = os.path.abspath("../python2.1/dataset")
    ways_to_files = get_way_to_files2(way_to_dataset, name)

    write_into_csv(way_to_dataset, ways_to_files, name)

    print("Работа окончена(часть 2)")
