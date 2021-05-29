# -*- coding: utf-8 -*-
"""

@author: IbrahimD
"""

# import the necessary packages
import imutils
import cv2
from Tracking import Tracking


resize_width = 600

camera = cv2.VideoCapture("peopleCount.mp4")


(grabbed, frame_prev) = camera.read()
frame_prev = imutils.resize(frame_prev, width=resize_width)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgmask = fgbg.apply(frame_prev)

#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (600,450))


Track_blobs = Tracking(50)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

# keep looping
while True:

    (grabbed, frame) = camera.read()
    if grabbed==False:
        break
        
        
    frame = imutils.resize(frame, width=resize_width)
    
        
    frame_diff = fgbg.apply(frame)
    
    
    ret,mask = cv2.threshold(frame_diff,127,255,cv2.THRESH_BINARY)
    mask = cv2.dilate(mask, kernel, iterations=2)
    
        
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    		cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    
    # only proceed if at least one contour was found
    for cnt in cnts:
    
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
#        x1,y1,w,h = cv2.boundingRect(cnt)
#        M = cv2.moments(cnt)
#        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        # only proceed if the radius meets a minimum size
        if radius>50 and radius<200:		
            Track_blobs.track(x,y,radius)
    
                
    			
    for blob in Track_blobs.blob_list:
                   
        cv2.circle(frame, (int(blob.x), int(blob.y)), int(blob.radius),(0, 255, 255), 2)
        cv2.putText(frame, str(blob.number) ,(int(blob.x),int(blob.y)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                
     
        
#    out.write(frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
        
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
#out.release()
camera.release()
cv2.destroyAllWindows()