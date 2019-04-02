# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
#print(cv2.__version__)
myimage=cv2.imread(r"C:\Users\user\Desktop\shyam\s2.png")
#to convertimage
#myimage1=cv2.imread(r"C:\Users\user\Desktop\shyam\s2.png",0)

myimage1=cv2.imread(r"C:\Users\user\Desktop\shyam\s2.png",cv2.IMREAD_GRAYSCALE)
face=cv2.CascadeClassifier(r"C:\Users\user\Desktop\shyam\haarcascades\haarcascade_frontalface_default.xml")

face1=face.detectMultiScale(myimage1,1.3,5)
#print('number face in myimages')
#print(len(face))
#x=face[:,0]
#y=face[:,1]
#w=face[:,2]
#h=face[:,3]
for x,y,w,h in face1:
    cv2.rectangle(myimage,(x,y),(x+w,y+h),(0,0,255),3)
    #cv2.imshow("facedetector",myimage)

cv2.imshow("mywindow",myimage)
cv2.waitKey(4)
cv2.destroyAllWindows()



#cv2.rectangle(myimage,(x,y),(w,h),(0,0,255),3)
#print(type(myimage))
#print(myimage)
#print(myimage.shape)
#print(myimage.dtype)
#to show image
#myimage3=myimage[::-1,::-1]
#cv2.imshow("mywindow",myimage3)
#myimage4=myimage[:,::6]




# face detect  line draw

#cv2.line(myimage,(308,429),(499,431),(255,0,0),5)
#rectangle draws

#cv2.rectangle(myimage,(99,44),(191,167),(255,0,0))


#face detect



