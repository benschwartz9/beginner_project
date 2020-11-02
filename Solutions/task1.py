import cv2
import numpy as np

img =  cv2.imread('../Images/Purdue_Logo.jpg')

#Read and write pixels
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

print(img.shape)
print(img[400, 400])

for x in range(780, 800 ):
    for y in range(747, 767):
        img[x, y] = (0, 0, 255)

cv2.imwrite("../Results/Purdue_Logo_Result.jpg", img)