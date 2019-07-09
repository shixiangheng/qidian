import multiprocessing as mp
import cv2
import numpy as np
import os

img = cv2.imread("01.jpg")

cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
#cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
