'''
Author: pipecat
'''
import numpy as np
import cv2

# 导入一张图像 模式为彩色图片
img = cv2.imread('test1.png', cv2.IMREAD_UNCHANGED)

print("================打印一下图像的属性================")
print("图像对象的类型 {}".format(type(img)))
print(img.shape)
print("图像宽度: {} pixels".format(img.shape[1]))
print("图像高度: {} pixels".format(img.shape[0]))
print("通道: {}".format(img.shape[2]))
print("图像分辨率: {}".format(img.size))
print("数据类型: {}".format(img.dtype))

ret, mask = cv2.threshold(img[:, :, 3], 10, 255, cv2.THRESH_BINARY)

cv2.imwrite('result.jpg',mask)
cv2.imwrite('result_png.png', mask)

cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()