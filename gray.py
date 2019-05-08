#coding=utf-8
#用来进行灰度化
import cv2

img = cv2.imread('picture/ricetest.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('picture/ricetestgray.jpg',gray)