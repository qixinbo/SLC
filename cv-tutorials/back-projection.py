import cv2
import numpy as np
from matplotlib import pyplot as plt

# EPF = Edge preserving filtering 

img1 = cv2.imread("lena.jpg")
print(img1.shape)
cv2.imshow("img1", img1)

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist(img1, [0,1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist, interpolation='nearest')
plt.title("hist")
plt.show()

# cv2.calcBackProject()

cv2.waitKey(0)
cv2.destroyAllWindows()