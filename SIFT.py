import cv2 
import os 

img = cv2.imread('./OIP.jpg',0)


sift = cv2.SIFT_create()
kp = sift.detect(img)

# img = cv2.drawKeypoints(img,kp,None)
# img = cv2.drawKeypoints(img,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Keypoints', img)




cv2.waitKey(0)
cv2.destroyAllWindows()