# coding=utf-8
# 先读图，然后二值化,
# 似圆度

import cv2
import math
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
cv2.drawContours(origin, maxContour, -1, (0, 255, 0), 3)
print "最大面积" + str(largest_area)

# 质心计算
M = cv2.moments(maxContour)
Centroid_x = int(M['m10'] / M['m00'])
Centroid_y = int(M['m01'] / M['m00'])
print "质心" + str(Centroid_x) + " " + str(Centroid_y)
cv2.circle(origin, (Centroid_x, Centroid_y), 3, (255, 0, 0), -1)

ContourItems = maxContour.shape[0]
# 遍历轮廓每个点，求与质心最近的距离，作为最大内接圆半径,
# 初始化一个距离
min_radius = math.pow((maxContour[0][0][0] - Centroid_x), 2) + math.pow((maxContour[0][0][1] - Centroid_y), 2)
for item in range(ContourItems):
    point_x = maxContour[item][0][0]
    point_y = maxContour[item][0][1]
    local_radius = math.pow((point_x - Centroid_x), 2) + math.pow((point_y - Centroid_y), 2)
    if local_radius <= min_radius:
        min_radius = local_radius

min_radius = int(math.sqrt(min_radius))
cv2.circle(origin, (Centroid_x, Centroid_y), min_radius, (0, 255, 255), 2)

# 遍历轮廓每个点，求与质心最远的距离，作为最小外接圆半径,
# 初始化一个距离
max_radius = math.pow((maxContour[0][0][0] - Centroid_x), 2) + math.pow((maxContour[0][0][1] - Centroid_y), 2)
for item in range(ContourItems):
    point_x = maxContour[item][0][0]
    point_y = maxContour[item][0][1]
    local_radius = math.pow((point_x - Centroid_x), 2) + math.pow((point_y - Centroid_y), 2)
    if local_radius >= max_radius:
        max_radius = local_radius

max_radius = int(math.sqrt(max_radius))
cv2.circle(origin, (Centroid_x, Centroid_y), max_radius, (255, 0, 255), 2)

P_pherical = min_radius * 1.0 / max_radius
P_pherical = round(P_pherical,3)
print "球状性： " + str(P_pherical)

cv2.putText(origin, 'min_radius : ' + str(min_radius), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)
cv2.putText(origin, 'max_radius: ' + str(max_radius), (50, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)
cv2.putText(origin, 'P_pherical: ' + str(P_pherical), (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)

cv2.namedWindow('Butterfly', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Butterfly', origin)
cv2.imwrite('picture/p-pherical.png',origin)

k = cv2.waitKey(0)

# 'ESC'
if k == 27:
    cv2.destroyAllWindows()
