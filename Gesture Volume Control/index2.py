
import HandTrackingModule as htm
import cv2 
import time 
import numpy 
import math 

from pynput.keyboard import Key , Controller
keyboard = Controller()

wCam , hCam = 1280 , 720

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0 

detector = htm.HandDetector(detectionCon=0.7) 

minAngle = -95 
maxAngle = 0
angle = 0 
angleBar = 400 
angleDeg = 0 
minHand = 50 
maxHand = 50 

while True:
    success , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        print(lmList[4],lmList[8])