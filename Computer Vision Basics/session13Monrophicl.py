import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
# import tensorflow as tf 

img = cv2.imread('mo.jpg',0)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)


# img = cv2.resize(img,(556,556))
kernel = np.ones([5,5],np.uint8)
dilation = cv2.dilate(mask,kernel,iterations=2)
erosion = cv2.erode(mask,kernel,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=2)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=2) # the best choice 




closing = cv2.resize(closing,(512,512))

cv2.imshow('image',closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
