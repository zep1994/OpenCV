import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,1),(511,511),(255,0,0),5)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(500,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow("img", img)

cv.waitKey(0)