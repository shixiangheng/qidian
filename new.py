import multiprocessing as mp
import cv2
import numpy as np
import os

val = raw_input("Enter your value: ")
print(type(val)) 

img=cv2.imread(val)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.GaussianBlur(gray,(3,3),0)
canny = cv2.Canny(img, 50, 150)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.imwrite("n.jpg", img)
#print(s)
