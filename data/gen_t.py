import os
import cv2
import numpy as np

train_list = "train_list.txt"

trimapdir = ".\\trimap"
maskdir = ".\\mask"

kernel_size = 30

def get_trimap(mask, size=(10, 10)):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, size)

    mask = mask / 255
    mask = mask.astype(np.uint8)

    dilated = cv2.dilate(mask, kernel, iterations=1) * 255
    eroded = cv2.erode(mask, kernel, iterations=1) * 255

    cnt1 = len(np.where(mask >= 0)[0])
    cnt2 = len(np.where(mask == 0)[0])
    cnt3 = len(np.where(mask == 1)[0])
    #print("all:{} bg:{} fg:{}".format(cnt1, cnt2, cnt3))
    assert(cnt1 == cnt2 + cnt3)

    cnt1 = len(np.where(dilated >= 0)[0])
    cnt2 = len(np.where(dilated == 0)[0])
    cnt3 = len(np.where(dilated == 255)[0])
    #print("all:{} bg:{} fg:{}".format(cnt1, cnt2, cnt3))
    assert(cnt1 == cnt2 + cnt3)

    cnt1 = len(np.where(eroded >= 0)[0])
    cnt2 = len(np.where(eroded == 0)[0])
    cnt3 = len(np.where(eroded == 255)[0])
    #print("all:{} bg:{} fg:{}".format(cnt1, cnt2, cnt3))
    assert(cnt1 == cnt2 + cnt3)

    result = dilated.copy()
    #res[((dilated == 255) & (msk == 0))] = 128
    result[((dilated == 255) & (eroded == 0))] = 128

    return result


names = []
with open(train_list, 'rt') as f:
    names = f.readlines()

for index, name in enumerate(names):
    if index % 100 == 0:
        print("{}% \done.".format(round(100*index/len(names))))
        #print("index: {}".format(index))
    mask_name = os.path.join(maskdir, name.split('.')[0] + ".png")
    #print(mask_name)
    trimap_name = os.path.join(trimapdir, name.split('.')[0] + ".png")
    mask = cv2.imread(mask_name, 0)
    trimap = get_trimap(mask, size=(kernel_size, kernel_size))
    cv2.imwrite(trimap_name, trimap)