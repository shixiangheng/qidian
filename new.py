import multiprocessing as mp
import cv2
import numpy as np
import os

img = cv2.imread("st.jpg")
#img=cv2.Canny(img, 200, 300)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#waijie lunkuo external hen useful!
cv2.drawContours(img, contours, 1, (0,0,0), 5)
cv2.imwrite("c.jpg", img)
#cv2.imshow("canny", cv2.imread("canny.jpg"))
'''
img = cv2.imread("s.png")
#img=cv2.Canny(img, 200, 300)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,0,0), 5)
cv2.imwrite("c.png", img)
#cv2.imshow("canny", cv2.imread("canny.jpg"))
#######    useful!!!!!
'''





