import numpy as np
import cv2 

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        myColorImage = np.zeros((512,512,3), dtype=np.uint8)
        myColorImage[:] = [blue,green,red]

        cv2.imshow('color',myColorImage)


img = cv2.imread('mo.jpg')
cv2.imshow('image',img)
points = []

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()