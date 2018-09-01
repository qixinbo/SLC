import cv2
import numpy as np
from matplotlib import pyplot as plt

# EPF = Edge preserving filtering 

img1 = cv2.imread("lena.jpg")
print(img1.shape)
cv2.imshow("img1", img1)

# plt.hist(img1.ravel(), 256, [0, 256])
# plt.show("matplotlib histogram")

color = {'blue', 'green', 'red'}
for i, color in enumerate(color):
	hist = cv2.calcHist([img1],[i], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])
plt.show()

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
equalHist = cv2.equalizeHist(gray)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
dst = clahe.apply(gray)
cv2.imshow("equalHist", equalHist)
cv2.imshow("local equal", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()