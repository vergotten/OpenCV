# -*- coding: utf-8 -*-
import cv2
import numpy as np


cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    #HSV - hue, saturation, value (тон, насыщенность, яркость)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([60,0,0])
    upper_green = np.array([150,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #Blurring-размытие, and Smoothing-сглаживание
    kernel = np.ones((15,15), np.float32)/225 #массив 15х15 со значениями 0.00444444444
                                              #ядро фильтра - коэффициенты фильтра
    #smoothed = cv2.filter2D(res, -1, kernel) # -1 - kernel center

    #blur = cv2.GaussianBlur(res, (15,15), 0)
    #median = cv2.medianBlur(res, 15) #ksize - The size of the filter kernel, where the dimensions must be odd
    #bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # false positives - на самом объекте лишние пиксели
    # false negatives - на бэкграунде
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #remove false positives from the background
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #remove false positives on object

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    #cv2.imshow('blur', blur)
    #cv2.imshow('median', median)
    #cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

