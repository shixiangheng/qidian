import numpy as np
import cv2

img=cv2.imread('haer.jpg',0)

img=cv2.line(img,(0,0),(255,255),(0,0,255),5)

print(img)

##cv2.imshow('haer',img)

cv2.imwrite('hcp.jpg',img)

cv2.destroyAllWindows()
