import cv2
import numpy as np
img = cv2.imread("00000.ppm")   
a=img[411:446,774:815]
img=a
newImg = a
newImg = cv2.resize(a, (300,300))
gray = cv2.cvtColor(newImg,cv2.COLOR_RGB2GRAY)

cv2.imwrite('a.ppm',a)
cv2.imwrite('n.ppm',newImg)

 
img = cv2.GaussianBlur(gray,(3,3),0)
e = cv2.Canny(img, 50, 150)
cv2.imwrite('e.ppm',e)
