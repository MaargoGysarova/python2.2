import csv
import os


def write_into_csv(way_to_dataset, way_to_files):
    with open("dataset_csv_first", 'w+', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(way_to_files)):
            file_writer.writerow(
                [f'{way_to_dataset + way_to_files[i]}', f'..\\dataset{way_to_files[i]}', f'{way_to_files[i][1]}'])


def get_way_to_files(way_to_dataset, name):
    ways_to_files = list()
    folder_way = way_to_dataset + '\\' + name
    num_of_files = sorted(os.listdir(folder_way))  # кол-во файлов

    for file_num in range(1, num_of_files):
        way_to_file = folder_way + f'\\{file_num:04}' + '.jpg'
        ways_to_files.append(way_to_file)

    return ways_to_files
