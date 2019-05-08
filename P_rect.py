# coding=utf-8
# 先读图，然后二值化,
# 矩形度

import cv2
import numpy as np
from matplotlib import pyplot as plt

#  此处读入图片，作为接口
origin = cv2.imread('picture/butterfly.png')
grayimage = cv2.imread('picture/butterfly.png', 0)

# 　高斯滤波
blur = cv2.GaussianBlur(grayimage, (5, 5), 0)

# 　二值化：用大津法，此处选项若是THRESH_BINARY_INV，则同意选用白色背景的图片样本
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 找轮廓
contours = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 轮廓集数目

largest_area = 0
largest_contour_index = 0
num = len(contours[1])
for i in range(num):
    area = cv2.contourArea(contours[1][i], False)
    if area > largest_area:
        largest_area = area
        largest_contour_index = i

maxContour = contours[1][largest_contour_index]
# 画轮廓
cv2.drawContours(origin, maxContour, -1, (0, 0, 255), 4)
print "最大面积" + str(largest_area)

# 查找最小外接矩形
minAreaRect = cv2.minAreaRect(maxContour)
box = cv2.boxPoints(minAreaRect)
box = np.int0(box)
# 画轮廓
cv2.drawContours(origin, [box], 0, (0, 255, 0), 4)

# 计算最小外接矩形面积
minAreaRect_Area = int(cv2.contourArea(box, False))
print "最小外接矩形面积" + str(minAreaRect_Area)

# 特征一：矩形度的计算
P_Rect = largest_area * 1.0 / minAreaRect_Area
# 统一结果为3位小数
P_Rect = round(P_Rect, 3)
print "矩形度" + str(P_Rect)

cv2.putText(origin, 'S_maxContour : ' + str(largest_area), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)
cv2.putText(origin, 'S_minAreaRect: ' + str(minAreaRect_Area), (50, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)
cv2.putText(origin, 'P_Rect: ' + str(P_Rect), (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)


# 显示
cv2.namedWindow('Butterfly', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Butterfly', origin)
cv2.imwrite('picture/p-rect.png',origin)

k = cv2.waitKey(0)

# 'ESC'
if k == 27:
    cv2.destroyAllWindows()
