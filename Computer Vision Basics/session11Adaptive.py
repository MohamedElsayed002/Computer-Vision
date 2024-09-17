
import cv2  as cv
import numpy as np



img = cv.imread('./mosalah.webp',0)
_, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Should be odd numbers onlly 
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,111,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,111,2)

img = cv.resize(img,(512,512))
th1 = cv.resize(th1,(512,512))
th2 = cv.resize(th2,(512,512))
th3 = cv.resize(th3,(512,512))
# cv.imshow('Image',img)
# cv.imshow('Threshold',th1)
cv.imshow('Adaptive Mean Threshold',th2)
# cv.imshow('Threshold Gaussian Threshold',th3)





cv.waitKey(0)
cv.destroyAllWindows()