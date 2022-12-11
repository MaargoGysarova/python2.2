# create dataframe from csv file 6 columns

import pandas as pd
import csv
import os
import matplotlib.pyplot as plt


def read_csv(name_of_csv, num_of_columns):
    """
    :return: list of lists
    """
    with open(name_of_csv, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        read_list = []
        for row in reader:
            if num_of_columns == 1:
                share_list = row[0].split(';')
                read_list.append(share_list[0])
            else:
                share_list = row[0].split(';')
                read_list.append(share_list[2])
    return read_list


def create_dataframe(path_of_csv):
    """
    :return: dataframe
    """
    list_abs_way = read_csv(path_of_csv, 1)
    list_name_class = read_csv(path_of_csv, 3)
    list_mark = ["Num_point"]
    list_image_width = ["Image_width"]
    list_image_height = ["Image_hight"]
    list_image_depth = ["Number_of_chanel"]
    list_image_pix = ["Number of pixels"]
    for row in list_name_class:
        if row == "tiger":
            list_mark.append("0")
        if row == "leopard":
            list_mark.append("1")

    for row in list_abs_way:
        if row == "Absolute way":
            continue
        else:
            image = plt.imread(row)
            list_image_width.append(image.shape[0])
            list_image_height.append(image.shape[1])
            list_image_depth.append(image.shape[2])
            list_image_pix.append(image.size)

    for i in range(1, len(list_abs_way)):
        try:
            list_abs_way[i] = os.path.abspath(list_abs_way[i])
        except:
            pass


    data = {
        list_abs_way[0]: list_abs_way[1:],
        list_name_class[0]: list_name_class[1:],
        list_mark[0]: list_mark[1:],
        list_image_width[0]: list_image_width[1:],
        list_image_height[0]: list_image_height[1:],
        list_image_depth[0]: list_image_depth[1:],
        list_image_pix[0]: list_image_pix[1:]
    }
    df = pd.DataFrame(data)
    print(df)
    return df


if __name__ == '__main__':
    path_to_csv = "../Laba2/dataset_csv_first.csv"
    create_dataframe(path_to_csv)
