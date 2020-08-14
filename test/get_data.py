import os
import shutil
import cv2

image_root_path = "E:\\Portrait_dataset\\archive\\clip_img"

files_name = []

for file_info in os.walk(image_root_path):
    if len(file_info[1]) == 0:
        for file_name in file_info[2]:
            full_file_name = os.path.join(file_info[0], file_name)
            files_name.append(full_file_name)

dst_path = ".\\..\\data\\image"

print(len(files_name))

matting_root_path = "E:\\Portrait_dataset\\archive\\matting"

mattings_name = []

for matting_info in os.walk(matting_root_path):
    if len(matting_info[1]) == 0:
        for matting_name in matting_info[2]:
            full_matting_name = os.path.join(matting_info[0], matting_name)
            mattings_name.append(full_matting_name)

mask_dst_path = "D:\\Code\\ML\\Semantic_Human_Matting\\data\\mask"
alpha_dst_path = "D:\\Code\\ML\\Semantic_Human_Matting\\data\\alpha"

for index, matting_name in enumerate(mattings_name):
    if index % 1000 == 0:
        print("{}% /done.".format(round(100*index/len(mattings_name))))
    matting_img = cv2.imread(matting_name, cv2.IMREAD_UNCHANGED)
    alpha = matting_img[:, :, 3]
    ret, mask = cv2.threshold(alpha, 10, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(mask_dst_path, os.path.basename(matting_name)), mask)
    cv2.imwrite(os.path.join(alpha_dst_path, os.path.basename(matting_name)), alpha)
    



