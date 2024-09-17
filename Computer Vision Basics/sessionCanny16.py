import cv2 
import numpy as np
import matplotlib.pyplot as plt 


img = cv2.imread('mo.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,100,200)


titles = ['image','canny']
imges = [img,canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(imges[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()