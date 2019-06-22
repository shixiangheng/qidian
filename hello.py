import cv2




img=cv2.imread('haer.jpg',0)

print(img)

##cv2.imshow('haer',img)

cv2.imwrite('hcp.jpg',img)

cv2.destroyAllWindows()
