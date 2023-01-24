import cv2 as cv

#Read an Image
img = cv.imread('Photos/cat_large.jpg')

#Show Image
cv.imshow('Cat', img)

#Rescale and Resize image
def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)

# #READING VIDEO
# capture = cv.VideoCapture("Videos/dog.mp4")

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

