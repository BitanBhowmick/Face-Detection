import cv2
import numpy as np


def func():
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)

    id=raw_input('Enter user id: ')
    sampleNum=0
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.waitKey(100)

        cv2.imshow("face",img)
        cv2.waitKey(1)
        if(sampleNum>20):
            break;

    cam.release()
    cv2.destroyAllWindows()

func()

execfile("trainer.py")
print("Do you want another face ID?? YES or NO")
x = raw_input()

if x == 'Yes':
    func()
    execfile("trainer.py")
    execfile("detector.py")
elif x== 'No':
    execfile("detector.py")
