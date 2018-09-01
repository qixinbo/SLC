import cv2 as cv

src = cv.imread("20180824031639239.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

print(type(src)) # numpy ndarray
print(src.shape)
print(src.size)
print(src.dtype)
cv.imwrite("/home/qixinbo/temp/1.png", src)
video = cv.VideoCapture(0)
while(True):
	ret, frame = video.read()
	frame = cv.flip(frame, 1)
	cv.imshow("video", frame)
	c = cv.waitKey(50)
	if c == 2:
		break

cv.waitKey(0)

cv.destroyAllWindows()