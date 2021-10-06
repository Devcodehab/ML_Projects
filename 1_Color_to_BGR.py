import cv2
img =  cv2.imread("image1.png")
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayimg.jpg",grayimg)
cv2.imshow("original",img)
cv2.imshow("Grayimage",grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows
