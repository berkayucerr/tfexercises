

import cv2
import numpy as np
from matplotlib import pyplot as plt
    
img = cv2.imread('open.png',0)
#img = cv2.medianBlur(img,5)

n = 6
kernel = np.ones((n,n),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)



#closing = cv2.dilate(img,kernel,iterations = 1)
#closing = cv2.erode(closing,kernel,iterations = 1)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#opening = cv2.erode(img,kernel,iterations = 1)
#opening = cv2.dilate(opening,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('processed')
plt.xticks([]), plt.yticks([])
plt.show()















