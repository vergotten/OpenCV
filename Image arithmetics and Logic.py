# -*- coding: utf-8 -*-
import cv2
import numpy as np


img1 = cv2.imread('messi.png')
img2 = cv2.imread('logo.png')

img2 = cv2.resize(img2,None,fx=0.45, fy=0.45, interpolation = cv2.INTER_CUBIC)
'''adding 2 images, цвета смешиваются, итоговые пиксели суммируются'''
#add = cv2.add(img1, img2)
#cv2.imshow('add', add)

'''blending 2 images via weighted, картинки становятся прозрачными'''
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) # 0 - gamma value
#cv2.imshow('weighted', weighted)

'''Bitwise Operations, opaque images'''

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape #.shape returns a tuple of number of rows, columns and channels (if image is color)
roi = img1[0:rows, 0:cols] #левый верхний угол, 0:500, 0:500 - здесь будет лого на img1

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #если значение >=220, то оно становится 255 и наоборот
                                                                     #а потом все инверсируется;
                                                                     #в ret - значение нижнего порога

mask_inv = cv2.bitwise_not(mask) #logo становится черным(0)

#маска (mask) нужна для того, чтобы сказать, какие пиксели (элементы) будут изменены
#roi - отдельный участок
#черный цвет - 0 (нет), белый цвет - 1 (есть)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #накладываю на месси чёрную маску от лого, освобождаю место для лого (чтобы цвета не смешивались)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask) #через маску копирую только нужный участок лого (цветной, без фона ненужного)

dst = cv2.add(img1_bg, img2_fg) #добавляю 1е изображение ко 2му (кусок картинки, не вся, только участок)
img1[0:rows, 0:cols] = dst #вставляю кусок верхней картинки с лого, к img1 (исходному)


cv2.imshow('img1', img1)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()

