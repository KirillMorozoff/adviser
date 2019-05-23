import numpy as np
import pyautogui
import imutils
import cv2

def getMyPosition():
    images = [
        cv2.imread('tmp/croppedField_01_01.png'),
        cv2.imread('tmp/croppedField_01_02.png'),
        cv2.imread('tmp/croppedField_01_03.png'),
        cv2.imread('tmp/croppedField_02_01.png'),
        cv2.imread('tmp/croppedField_02_02.png'),
        cv2.imread('tmp/croppedField_02_03.png')
    ]
    templateDealer = cv2.imread('templates/templateDealer.png')
    gray = cv2.cvtColor(templateDealer, cv2.COLOR_BGR2GRAY)
    w, h = gray.shape[::-1]

    result = []
    for i in images:
        res = cv2.matchTemplate(i,templateDealer,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(cv2.minMaxLoc(res))
        #print(min_val)
        #print("")
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(i, top_left, bottom_right, (0, 255, 0), 2)
        #cv2.imshow('img', i)
        result.append(res)

    threshold = 0.8
    flag = False
    for i in result:
        if i.any() > threshold:
            #cv2.imshow('Result', templateDealer)
            flag = True
        else:
            flag = False

          
    cv2.imshow('Result', result[0])
