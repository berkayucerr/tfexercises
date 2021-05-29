

import cv2
import numpy as np
from matplotlib import pyplot as plt
    
#img = cv2.imread('foto.jpg')
#
#kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#
#img_sharpened = cv2.filter2D(img, -1, kernel)
#

#
#cv2.imwrite("sharpened.jpg",img_sharpened)
#
#edges = cv2.Canny(img,100,200)
#
#
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#plt.show()


img = cv2.imread('foto.jpg')
img_sharpened = cv2.imread('sharpened.jpg')

edges = cv2.Canny(img,100,200)
edges_sharpened = cv2.Canny(img_sharpened,100,200)


plt.subplot(121),plt.imshow(edges,cmap = 'gray')
plt.title('Edges Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges_sharpened,cmap = 'gray')
plt.title('Edges Sharpened Image'), plt.xticks([]), plt.yticks([])
plt.show()



