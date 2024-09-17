
import numpy as np 
import cv2 as cv 


img = cv.imread('./mo.jpg')

_, th1 = cv.threshold(img,55,255,cv.THRESH_BINARY)
_, th2 = cv.threshold(img,200,255,cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_, th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
_, th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

img = cv.resize(img,(512,512))
th1 = cv.resize(th1,(512,512))
th2 = cv.resize(th2,(512,512))
th3 = cv.resize(th3,(512,512))
th4 = cv.resize(th4,(512,512))
th5 = cv.resize(th5,(512,512))

cv.imshow('Original Image',img)
cv.imshow('Th1',th1)
cv.imshow('Th2',th2)
cv.imshow('Th3',th3)
cv.imshow('Th4',th4)
cv.imshow('Th5',th5)
cv.waitKey(0)
cv.destroyAllWindows()