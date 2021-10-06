import cv2
import os
import time
dataset = "dataset"
name = input("Enter your Name : ")

path = os.path.join(dataset,name)
if not os.path.isdir(path):
     os.mkdir(path)

(width,height) = (130,100)

haarCascade= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


cam = cv2.VideoCapture(0)

count = 1


while count<31:
    print(count)

    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face =  haarCascade.detectMultiScale(grayImg,1.3,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceOnly =grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeImg)
        count+= 1
        
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image captured suceesfully")    
cam.release()


