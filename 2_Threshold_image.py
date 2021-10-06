import cv2

img = cv2.imread("image1.png")

grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImage,200,255,cv2.THRESH_BINARY)[1]

cv2.imwrite("threshold3.png",thresImg)



