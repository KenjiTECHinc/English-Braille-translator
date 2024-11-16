import os
import cv2
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
le = LabelEncoder()

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense

images = []
labels = []

path = 'data/raw/character_set1/training_data/'

dir_list = os.listdir(path)
for i in dir_list:
    dir = os.path.join(path, i)
    file_list = os.listdir(dir)

    images = []
    labels = []

    for j in file_list:
        files = os.path.join(dir, j)
        img = cv2.imread(files)
        img = cv2.resize(img, (64,64))
        img = np.array(img, dtype=np.float32)
        img = img/255
        images.append(img)
        labels.append(i)

    X = np.array(images)
    print(f'{i}')
    print(f'-> len(X) = {len(X)}')
    print(f'-> X.shape = {X.shape}')

    y = np.array(labels)
    print(f'-> len(y) = {len(y)}')
    print(f'-> y.shape = {y.shape}')

    y = le.fit_transform(y)
    X_sh, y_sh = shuffle(X, y, random_state=42)

