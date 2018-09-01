import cv2
# Color space includes: RGB, HSV, HIS, YCrCb, YUV
# RGB = BGR, Blue, Green, Red
# HSV = Hue, Saturation, Value

img = cv2.imread("20180824031639239.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("yuv", yuv)

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow("ycrcb", ycrcb)

cv2.waitKey(0)
cv2.destroyAllWindows(param)