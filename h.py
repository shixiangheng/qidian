import cv2
import numpy as np

img = cv2.imread("00000.ppm")    #载入图像


a=img[411:446,774:815]
img=a
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# 轮廓检测
_ ,contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


newImg = a
newImg = cv2.resize(a, (300,300))

# 画图
for i in range(len(contours)-1):
    cv2.drawContours(newImg, contours[i+1], -1, (0,0,0), 8)

cv2.imwrite('a.ppm',a)
cv2.imwrite('n.ppm',newImg)
