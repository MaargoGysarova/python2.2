import csv
import os


def write_into_csv(way_to_dataset, way_to_files):
    with open("dataset_csv_first", 'w+', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=';')
        file_writer.writerow(["Absolute way", "Relative way", "Class"])

        for i in range(0, len(way_to_files)):
            way_to_file = f'dataset/{way_to_files[i]}'
            file_writer.writerow(
                [f'{way_to_dataset + "/" + way_to_files[i]}', f'  /dataset/{way_to_files[i]}',
                 os.path.basename(os.path.dirname(way_to_file))])


def get_way_to_files(way_to_dataset, name):
    ways_to_files = list()
    num_names = list()
    for i in range(0, len(name)):
        folder_way = way_to_dataset + '/' + name[i]
        num_of_files = os.listdir(folder_way)  # кол-во файлов
        num_names.append(len(num_of_files))
        for file_num in range(1, len(num_of_files) + 1):
            way_to_file = name[i] + f'/{file_num:04}' + '.jpg'
            ways_to_files.append(way_to_file)

    return [ways_to_files, num_names]


if __name__ == '__main__':
    name = ['tiger', 'leopard']
    way_to_dataset = os.path.abspath("../python2.1/dataset")
    ways_to_files = get_way_to_files(way_to_dataset, name)[0]

    write_into_csv(way_to_dataset, ways_to_files)

    print("Работа окончена(часть 1)")
