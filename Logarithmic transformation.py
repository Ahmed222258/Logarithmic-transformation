import cv2
import numpy as np


image=cv2.imread('img/image.png')


imagrresult=np.uint8(np.log1p(image))
thresh=1
imagelog = cv2.threshold(imagrresult, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("LImag",imagelog)