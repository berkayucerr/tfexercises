import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
#img = cv2.imread('opencv-logo.png',0)

img = cv2.GaussianBlur(img,(3,3),0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


dp=1 # Inverse ratio of the accumulator resolution to the image resolution
minDist=50 # Minimum distance between the centers of the detected circles
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp,minDist,
                            param1=50,param2=30,minRadius=10,maxRadius=30)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)


#cv2.imshow('thresh',img)
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()