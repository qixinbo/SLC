import cv2
import numpy as np

img1 = cv2.imread("LinuxLogo.jpg")
print(img1.shape)
cv2.imshow("img1", img1)

roi = img1[50:120, 100: 240]
cv2.imshow("roi", roi)

copyImg = img1.copy()
h, w = img1.shape[:2]
mask = np.zeros([h+2, w+2], np.uint8)
cv2.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100,100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.imshow("flood", copyImg)


cv2.waitKey(0)
cv2.destroyAllWindows()