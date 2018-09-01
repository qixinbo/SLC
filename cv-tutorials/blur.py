import cv2
import numpy as np

img1 = cv2.imread("20180824031639239.jpg")
print(img1.shape)
cv2.imshow("img1", img1)

blur = cv2.blur(img1, (15, 1))
blur2 = cv2.blur(img1, (1, 15))
cv2.imshow("blur", blur)
cv2.imshow("blur2", blur2)

# custom blur = cv2.filter2D()

mblur = cv2.medianBlur(img1, 5)
cv2.imshow("medianBlur", mblur)


cv2.waitKey(0)
cv2.destroyAllWindows()