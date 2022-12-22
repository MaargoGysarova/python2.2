#начало работы
import numpy
import matplotlib
import torch

import os
import glob
import random

import torch
import torch.nn as nn
import torch
import torch.optim as optim
import torch.nn.functional as F

from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset

from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#удалить первые 100 элементов из списка
def delete_first_100_elements(list):
    for i in range(100):
        list.pop(i)
    return list
#цикл от 2 до 10
def cycle_2_10():
    for i in range(2, 10):
        print(i)