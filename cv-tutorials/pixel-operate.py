import cv2
import numpy as np

img1 = cv2.imread("LinuxLogo.jpg")
img2 = cv2.imread("WindowsLogo.jpg")
print(img1.shape)
print(img2.shape)
cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

add = cv2.add(img1, img2)
cv2.imshow("add", add)

substract = cv2.subtract(img1, img2)
cv2.imshow("substract", substract)

divide = cv2.divide(img1, img2)
cv2.imshow("divide", divide)

multiply = cv2.multiply(img1, img2)
cv2.imshow("multiply", multiply)

mean1 = cv2.mean(img1)
print(mean1)

mean1, dev1 = cv2.meanStdDev(img1)
print(mean1)
print(dev1)


cv2.waitKey(0)
cv2.destroyAllWindows()