import numpy as np
import cv2
cap = cv2.VideoCapture('20161021_172121.mp4')
count = 0

while count<1000:
   # Capture frame-by-frame
   ret, frame = cap.read()
   frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   rows,cols = frame.shape
   #flp = cv2.getRotationMatrix2D((cols/2, rows/2),90,1)
   #dst = cv2.warpAffine(frame,flp,(cols,rows))
   
   final = cv2.resize(frame,(200,80))
   #Our operations on the frame come here
   name = "frame%d.jpg"%count
   cv2.imwrite(name, final)     # save frame as JPEG file
   count +=1


