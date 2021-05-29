

import cv2
import numpy as np
from matplotlib import pyplot as plt
    
img = cv2.imread('morp.png')


kernel = np.ones((5,5),np.float32)/25



#dst = cv2.blur(img,(5,5)) 


#dst = cv2.GaussianBlur(img,(5,5),0)
#
#dst = cv2.medianBlur(img,5)



## construct the Sobel x-axis kernel
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
 
## construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")


laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")


dst = cv2.filter2D(img,-1,laplacian)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('processed')
plt.xticks([]), plt.yticks([])
plt.show()
 





