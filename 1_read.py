import cv2
img = cv2.imread("image1.png")
cv2.imshow("image1",img)
cv2.imwrite("image1Copy.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
