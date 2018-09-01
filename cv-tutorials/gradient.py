import cv2
import numpy as np 

img = cv2.imread("20180824031639239.jpg")

grad_x = cv2.Sobel(img, cv2.CV_32F, 1, 0)
grad_y = cv2.Sobel(img, cv2.CV_32F, 0, 1)

grad_x = cv2.Scharr(img, cv2.CV_32F, 1, 0)
grad_y = cv2.Scharr(img, cv2.CV_32F, 0, 1)

gradx = cv2.convertScaleAbs(grad_x)
grady = cv2.convertScaleAbs(grad_y)

cv2.imshow("gradx", gradx)
cv2.imshow("grady", grady)

gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)
cv2.imshow("gradxy", gradxy)

dst = cv2.Laplacian(img, cv2.CV_32F)
laplace = cv2.convertScaleAbs(dst)
cv2.imshow("laplace", laplace)

# cv2.filter2D() for customized kernel

cv2.waitKey(0)
cv2.destroyAllWindows()