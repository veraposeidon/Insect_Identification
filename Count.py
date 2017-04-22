# coding=utf-8
# 先读图，然后二值化,通过找轮廓来进行计数

import cv2
import numpy as np
from matplotlib import pyplot as plt

origin = cv2.imread('picture/ricetest.png')
RiceImg = cv2.imread('picture/ricetest.png', 0)

blur = cv2.GaussianBlur(RiceImg, (5, 5), 0)

# 大津法二值化：此处可以用原理代码来巴拉巴拉一大段
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 输出阈值
print ret

# 找轮廓
contours = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
num = len(contours[1])
print num
# 画轮廓
cv2.drawContours(origin, contours[1], -1, (0, 0, 255), 1)
cv2.putText(origin, 'Rice Num:  ' + str(num), (1, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 100, 100), 2, cv2.LINE_AA)

cv2.namedWindow('RiceO', cv2.WINDOW_AUTOSIZE)
cv2.imshow('RiceO', origin)

k = cv2.waitKey(0)

# 'ESC'
if k == 27:
    cv2.destroyAllWindows()
