import csv
import os
import shutil
from csv_file_first import get_way_to_files


def write_into_csv(way_to_dataset, way_to_files):
    with open("dataset_csv_first", 'w+', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(way_to_files)):
            way_to_file = f'dataset/{way_to_files[i]}'
            file_writer.writerow(
                [f'{way_to_dataset + "/" + way_to_files[i]}', f'  /dataset/{way_to_files[i]}',
                 os.path.basename(os.path.dirname(way_to_file))])


def get_way_to_files2(way_to_dataset, name):
    ways_to_files = list()
    ways_to_files = get_way_to_files(way_to_dataset, name)

    i = 0
    for file in ways_to_files:
        way_to_file = "dataset/dataset_allnames/f'{name}_{i:04}'+'.jpg'"
        shutil.copy(file,way_to_file)
        i += 1



