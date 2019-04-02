# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:43:56 2019

@author: DELL
"""

import cv2
print(cv2.__version__)

myimage=cv2.imread(r"C:\Users\user\Desktop\shyam\s2.jpg")

myimage1=cv2.imread(r"C:\Users\user\Desktop\shyam\s2.jpg",0)
facedetector=cv2.CascadeClassifier(r"C:\Users\user\Desktop\shyam\haarcascades\haarcascade_frontalface_default.xml")
face=facedetector.detectMultiScale(myimage1,1.1,1)
print(len(face))
#face line draw....between two point...
#cv2.line(myimage,(113,168),(196,167),(255,0,0),5)
#cv2.rectangle(myimage,(99,44),(191,167),(255,0,0))
#image2=myimage1[:,::6]
#print(type(myimage))
#print(myimage)
#print(myimage1.shape)
#print(myimage.dtype)
#cv2.imshow("mywindow",myimage)
cv2.waitKey(0)
#cv2.destroyAllWindows()
#x=face[:,0]
#y=face[:,1]
#w=face[:,2]
#h=face[:,3]
for x,y,w,h in face:
    cv2.rectangle(myimage,(x,y),(w+h,y+h),(0,0,255),1)
    cv2.imshow("facedetected",myimage)
#cv2.rectangle(myimage,(x,y),(x+w,y+h),(0,0,255),3)
#cv2.imshow("facedetected",myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()