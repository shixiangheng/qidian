
import cv2

img = cv2.imread("00000.ppm")    #take in photo


a=img[411:446,774:815]   #cut it 
img=a
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imwrite('a.jpg',i)

