from __future__ import print_function
import cv2
import numpy as np

import cv2 as cv
import argparse
img = cv2.imread("00000.ppm")   


a=img[411:446,774:815]
img=a

newImg = a
newImg = cv2.resize(a, (300,300))

for i in range(len(contours)-1):
    cv2.drawContours(newImg, contours[i+1], -1, (0,0,0), 8)

cv2.imwrite('a.ppm',a)
cv2.imwrite('n.ppm',newImg)

max_lowThreshold = 100
window_name = 'Edge Map'
title_trackbar = 'Min Threshold:'
ratio = 3
kernel_size = 3
def CannyThreshold(val):
    low_threshold = val
    img_blur = cv.blur(src_gray, (3,3))
    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
    mask = detected_edges != 0
    dst = src * (mask[:,:,None].astype(src.dtype))
    cv.imshow(window_name, dst)
parser = argparse.ArgumentParser(description='Code for Canny Edge Detector tutorial.')
parser.add_argument('--input', help='Path to input image.', default=a)
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.namedWindow(window_name)
cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)
CannyThreshold(0)
cv.waitKey()
