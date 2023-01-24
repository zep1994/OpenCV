import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale-0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

cv.waitKey(0)

READING VIDEO
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

