import os


def get_way(num_of_file: int, name,index) -> str:
    """

    :param name: names of images
    :param num_of_file: num of images
    :return: way to file
    """
    way_to_dataset = os.path.abspath("../../python2.1/dataset")
    return f'{way_to_dataset}/{name[index]}/{num_of_file:04}.jpg'


def main(index):
    way_to_dataset = os.path.abspath("../../python2.1/dataset")
    name = ['tiger', 'leopard']
    folder_way = way_to_dataset + '/' + name[index]
    num_of_files = os.listdir(folder_way)
    rows = []
    for file in range(1, len(num_of_files) + 1):
        rows.append(get_way(file, name ,index))
        file += 1
    return rows, len(num_of_files)


