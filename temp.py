import cv2
import numpy as np
import os

img = cv2.imread('Images/grayscale.jpg')
median = cv2.medianBlur(img, 3)

compare = np.concatenate((img, median), axis=1)

cv2.imwrite('test.jpg', compare)