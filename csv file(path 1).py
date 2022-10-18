import csv
import os


def write_into_csv(way_to_dataset, way_to_files):
    with open("dataset_csv_first", 'w', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(way_to_files)):
            file_writer.writerow([f'{way_to_dataset + way_to_files[i]}', f'..\\dataset{way_to_files[i]}', f'{way_to_files[i][1]}'])




