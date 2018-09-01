import cv2
import numpy as np
# Color space includes: RGB, HSV, HIS, YCrCb, YUV
# RGB = BGR, Blue, Green, Red
# HSV = Hue (0-180), Saturation (0-255), Value (0-255)

img = cv2.imread("20180824031639239.jpg")

b, g, r = cv2.split(img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_hsv = np.array([37, 43, 46])
up_hsv = np.array([77, 255, 255])
hsv = cv2.inRange(hsv, lowerb=low_hsv, upperb=up_hsv)
cv2.imshow("hsv", hsv)

yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("yuv", yuv)

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow("ycrcb", ycrcb)



cv2.waitKey(0)
cv2.destroyAllWindows()