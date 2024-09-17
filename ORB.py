
import cv2 
import numpy as np
import matplotlib.pyplot as plt 
import os 

print(os.getcwd())

img1 = cv2.imread('./mo.jpg',0)
img2 = cv2.imread('./mo1.jpg',0)

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))



orb = cv2.ORB_create()

kp1 , des1 = orb.detectAndCompute(img1,None)
kp2 , des2 = orb.detectAndCompute(img2,None)
img = cv2.drawKeypoints(img2,kp2,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches,key= lambda x : x.distance)


img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:500],None,flags=2)
cv2.imshow('Keypoints',img3)

plt.imshow(img3)


cv2.waitKey(0)
cv2.destroyAllWindows()