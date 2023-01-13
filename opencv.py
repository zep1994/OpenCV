import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)

ret, frame = cap.read()
print(ret)
d
plt.imshow(frame)

cap.release()