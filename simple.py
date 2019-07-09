import multiprocessing as mp
import cv2
import numpy as np
import os

img = cv2.imread("spl.jpg")
img=cv2.Canny(img, 200, 300)

cv2.imwrite("c.jpg", img)
