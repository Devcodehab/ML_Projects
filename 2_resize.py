import cv2
import imutils as imu
img = cv2.imread("image1.png")
resizeImg = imu.resize(img,width = 20)
cv2.imwrite("resizedimg.png",resizeImg)
