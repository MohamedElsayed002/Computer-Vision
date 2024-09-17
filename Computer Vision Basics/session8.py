import cv2
import os 

# os.chdir
# pwd

img = cv2.imread('mosalah.webp')
img2 = cv2.imread('mo.jpg')

b,g,r = cv2.split(img) 
img = cv2.merge((b,g,r))

# ball = img[341:432,394:483]
# img[109:200,100:189] = ball



img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

dst = cv2.addWeighted(img,0.4,img2,0.6,100)

cv2.imshow('Image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()