import os

imagedir = ".\\image"

filenames = os.listdir(imagedir)

with open("train_list.txt", "wt") as f:
    for filename in filenames:
        f.write(filename + '\n')

