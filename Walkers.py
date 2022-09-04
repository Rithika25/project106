import cv2
import numpy as np

# Create our body classifier
body_clasifier=cv2.cascadeclasifier('haarcascade_frontalface_default.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    
    bodies=body_clasifier.detectmutiscale(gray,1.2,3)
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      # roi_color=img(y:y+h,x:x+w)
       #cv2.imwrite("walking.avi")
    cv2.imshow('pedestrials',frame)


    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
