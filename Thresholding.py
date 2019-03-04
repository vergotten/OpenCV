# -*- coding: utf-8 -*-
import cv2
import numpy as np

#img = cv2.imread('book-page.png')
img = cv2.imread('messi.png')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #12-все больше 12, преобразовывается в 255
                                                                    #cv2.THRESH_BINARY - вид трешхолда
                                                                    #retval - возвращается значение мин. порога

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, -5)
#adaptive threshold - функция трэшхолда для каждого пикселя, обычный трешхолд - для всей картинки
#Предпоследняя цифра - размер окрестности, используемой для вычисления порогового значения для каждого пикселя (нечётное значение)
#если ваш район слишком мал (у меня было 3), он работает как обнаружение края
#Последняя цифра - константа С - это константа, вычитаемая из среднего или взвешенного значения

cv2.imshow('img', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
