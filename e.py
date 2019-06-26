import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('00000.ppm',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
