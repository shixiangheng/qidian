import cv2
import numpy as np

img = cv2.imread("00000.ppm")    #载入图像


a=img[411:446,774:815]
img=a

newImg = a
newImg = cv2.resize(a, (300,300))

for i in range(len(contours)-1):
    cv2.drawContours(newImg, contours[i+1], -1, (0,0,0), 8)

cv2.imwrite('a.ppm',a)
cv2.imwrite('n.ppm',newImg)
import org.opencv.core.Core;
import org.opencv.core.Mat;

import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class CannyEdgeDetection {
   public static void main(String args[]) throws Exception {
      // Loading the OpenCV core library
      System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

      // Reading the Image from the file and storing it in to a Matrix object
      String file = a;

      // Reading the image
      Mat src = Imgcodecs.imread(file);

      // Creating an empty matrix to store the result
      Mat gray = new Mat();

      // Converting the image from color to Gray
      Imgproc.cvtColor(src, gray, Imgproc.COLOR_BGR2GRAY);
      Mat edges = new Mat();

      // Detecting the edges
      Imgproc.Canny(gray, edges, 60, 60*3);

      // Writing the image
      Imgcodecs.imwrite("edge.ppm", edges);
      System.out.println("Image Loaded");
   } 
}
