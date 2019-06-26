import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("00000.ppm")   


a=img[411:446,774:815]
img=a
e = cv2.Canny(a,100,200)

newImg = a
newImg = cv2.resize(a, (300,300))


cv2.imwrite('a.ppm',a)
cv2.imwrite('n.ppm',newImg)
cv2.imwrite('e.ppm',e)

