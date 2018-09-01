import cv2
import numpy as np

img1 = cv2.imread("LinuxLogo.jpg")
img2 = cv2.imread("WindowsLogo.jpg")
print(img1.shape)
print(img2.shape)
cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

bit_add = cv2.bitwise_and(img1, img2)
cv2.imshow("bit_add", bit_add)

bit_or = cv2.bitwise_or(img1, img2)
cv2.imshow("bit_or", bit_or)

bit_no = cv2.bitwise_not(img1)
cv2.imshow("bit_no", bit_no)


cv2.waitKey(0)
cv2.destroyAllWindows()