import cv2
import numpy as np

# EPF = Edge preserving filtering 

img1 = cv2.imread("lena.jpg")
print(img1.shape)
cv2.imshow("img1", img1)

dst = cv2.bilateralFilter(img1, 0, 100, 15)
cv2.imshow("dst", dst)

dst1 = cv2.pyrMeanShiftFiltering(img1, 10, 50)
cv2.imshow("dst1", dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()