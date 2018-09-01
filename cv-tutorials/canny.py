import cv2
import numpy as np 

img = cv2.imread("20180824031639239.jpg")

# First step: Gaussian Blur
blur = cv2.GaussianBlur(img, (3, 3), 0)

# Second step: covert color to Gray
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

# Calculate gradient
grad_x = cv2.Sobel(img, cv2.CV_16SC1, 1, 0)
grad_y = cv2.Sobel(img, cv2.CV_16SC1, 0, 1)

# Upper and lower threshold
edge = cv2.Canny(grad_x, grad_y, 200, 250)
cv2.imshow("edge", edge)

colorful = cv2.bitwise_and(img, img, mask=edge)
cv2.imshow("colorful edge", colorful)


cv2.waitKey(0)
cv2.destroyAllWindows()