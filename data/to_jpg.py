import cv2
import os

names = []
with open(train_list, 'rt') as f:
    names = f.readlines()

image_dir = "./image"
to_dir = "./jpg"

for name in names:
    image = cv2.imread()