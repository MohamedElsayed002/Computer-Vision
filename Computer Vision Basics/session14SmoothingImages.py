
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 


img = cv2.imread('salt.png')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

averaging = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5) 

cv2.imshow('Original',img)
img = cv2.resize(median,(512,512))
cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()