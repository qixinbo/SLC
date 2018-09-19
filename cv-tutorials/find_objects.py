import cv2
import numpy as np 

img = cv2.imread("20180824031639239.jpg")

# Useful functions:
# 	cv2.HoughLines()
# 	cv2.HoughCircles()
# 	cv2.findContours()
# 	cv2.approxPolyDP()
#	cv2.dilate()
#	cv2.erode()
# cv2.morphologyEx()
# cv2.MORPH_OPEN()
# cv2.MORPH_CLOSE()
# cv2.watershed()

cv2.waitKey(0)
cv2.destroyAllWindows()