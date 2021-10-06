import cv2
import os
import time



haarCascade= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


cam = cv2.VideoCapture(0)


a = "Person Detected"

b = "Person Not Detected"

while True:
    
  
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face =  haarCascade.detectMultiScale(grayImg,1.3,4)
   
    if len(face) != 0:
        cv2.putText(img, a, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 165, 0), 2)
    else:
        cv2.putText(img, b, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 165, 0), 2)
        
        
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
       

   
    cv2.imshow("FaceDetection",img)
    
    
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()


    
   
cam.release()
cv2.destroyAllWindows()
