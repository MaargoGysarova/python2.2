# create dataframe from csv file 6 columns

import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import random
import cv2


def create_histogram(df, mark_class):
    """
    Создание гистограммы по метке класса
    :return: histogram
    """
    result = [[], [], []]
    path_image_list = filter_dataframe_mark_class(df, "Num_class", mark_class)
    i = random.randint(0, len(path_image_list))
    path_way = path_image_list.iloc[i, 0]
    # create histogram for image
    img = cv2.imread(path_way)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

    return result


def read_csv(name_of_csv, num_of_columns):
    """
    Чтение csv файла по колонкам
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


def filter_dataframe_mark_class(df, column, value):
    """
    Фильтрация по метке класса
    :return: dataframe
    """
    df = df[df[column] == value]
    print(df)
    # save dataframe to csv file
    df.to_csv("filter_dataframe_mark_class.csv", sep='\t', encoding='utf-8')
    return df


def filter_dataframe_wight_and_height_and_mark(df, column1, column2, column3, value1, value2, value3):
    """
    Фильрация по ширине, высоте и метке класса
    :return: dataframe
    """
    df = df[(df[column1] <= value1) & (df[column2] <= value2) & (df[column3] == value3)]
    print(df)
    # save dataframe to csv file
    df.to_csv("filter_dataframe_wight_and_height.csv", sep='\t', encoding='utf-8')
    return df


def group_dataframe_pixel(df):
    """
    Группировка по количеству пикселей
    :return: dataframe
    """
    # copy dataframe
    df1 = df.copy()
    # rename column
    df1.rename(columns={'Number_of_pixels': 'Min_pixel'}, inplace=True)
    # copy column
    df1['Max_pixel'] = df1['Min_pixel']
    df1['Mean_pixel'] = df1['Min_pixel']

    # group dataframe by column
    df1 = df1.groupby(['Class']).agg({'Min_pixel': 'min', 'Max_pixel': 'max', 'Mean_pixel': 'mean'})
    print(df1)

    df1.to_csv("group_dataframe_pixel.csv", sep='\t', encoding='utf-8')


def create_dataframe(path_of_csv):
    """
    Создание dataframe из csv файла
    :return: dataframe
    """
    list_abs_way = read_csv(path_of_csv, 1)
    list_name_class = read_csv(path_of_csv, 3)
    list_mark = ["Num_class"]
    list_image_width = ["Image_width"]
    list_image_height = ["Image_hight"]
    list_image_depth = ["Number_of_chanel"]
    list_image_pix = ["Number_of_pixels"]
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
    return df


if __name__ == '__main__':
    path_to_csv = "../Laba2/dataset_csv_first.csv"
    create_dataframe(path_to_csv)
    filter_dataframe_mark_class(create_dataframe(path_to_csv), "Num_class", "0")
    filter_dataframe_wight_and_height_and_mark(create_dataframe(path_to_csv), "Image_width", "Image_hight", "Num_class", 400, 400, "0")
    group_dataframe_pixel(create_dataframe(path_to_csv))
    create_histogram(create_dataframe(path_to_csv), "0")
