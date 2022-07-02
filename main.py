import cv2
import numpy as np

webcam=False

cap=cv2.VideoCapture(0)

while True:
    success, img=cap.read()
    cv2.imshow('Original',img)
    cv2.waitKey(1)
