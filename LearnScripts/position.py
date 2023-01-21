import cv2 as cv 
import numpy as np 

img = cv.imread("Photos/cat.jpg")
cv.imshow("frame", img) 
cv.waitKey(0)