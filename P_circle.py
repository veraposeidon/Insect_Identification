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
cv2.circle(origin, (Centroid_x, Centroid_y), 3, (255, 255, 255), -1)

# 获取长轴
Major_Axis_Length = 0
Major_Axis_Angle = 0
Major_Axis_End_x = 0
Major_Axis_End_y = 0
Major_Axis_Begin_x = 0
Major_Axis_Begin_y = 0

# 此处需要注意质心是否在轮廓内
# 找长轴
for angle in range(180):
    theta = angle * 3.14 / 180.0
    lengthBackward = 0
    lengthForward = 0
    point_End_x = Centroid_x
    point_End_y = Centroid_y
    point_Begin_x = Centroid_x
    point_Begin_y = Centroid_y

    # 步进越小准确率越高，设置成1可以先找到准确的直线角度，再根据角度和质心得到的直线计算出正确的长轴和轮廓交点
    while cv2.pointPolygonTest(maxContour, (point_End_x, point_End_y), False) > 0:
        lengthForward = lengthForward + 0.1
        point_End_x = int(round(point_End_x + lengthForward * math.cos(theta)))
        point_End_y = int(round(point_End_y + lengthForward * math.sin(theta)))

    while cv2.pointPolygonTest(maxContour, (point_Begin_x, point_Begin_y), False) > 0:
        lengthBackward = lengthBackward + 0.1
        point_Begin_x = int(round(point_Begin_x - lengthBackward * math.cos(theta)))
        point_Begin_y = int(round(point_Begin_y - lengthBackward * math.sin(theta)))

    if lengthForward + lengthBackward >= Major_Axis_Length:
        Major_Axis_Length = lengthForward + lengthBackward
        Major_Axis_Angle = angle
        Major_Axis_End_x = point_End_x
        Major_Axis_End_y = point_End_y
        Major_Axis_Begin_x = point_Begin_x
        Major_Axis_Begin_y = point_Begin_y

# 计算实际长轴长度
Real_Major_Axis_Length = math.sqrt(
    math.pow((Major_Axis_End_x - Major_Axis_Begin_x), 2) + math.pow((Major_Axis_End_y - Major_Axis_Begin_y), 2))

Real_Major_Axis_Length = round(Real_Major_Axis_Length, 1)
print "长轴长度 = " + str(Real_Major_Axis_Length)
print "长轴角度 = " + str(Major_Axis_Angle)
# print "起点 = " + "x: " + str(Major_Axis_Begin_x) + "  y: " + str(Major_Axis_Begin_y)
# print "起点 = " + "x: " + str(Major_Axis_End_x) + "  y: " + str(Major_Axis_End_y)

# 画长轴
cv2.line(origin, (Major_Axis_Begin_x, Major_Axis_Begin_y), (Major_Axis_End_x, Major_Axis_End_y), (255, 0, 0), 2)

# 画以质心为圆心，长轴为直径的圆形用以辅助显示
cv2.circle(origin, (Centroid_x, Centroid_y), int(Real_Major_Axis_Length/2), (0, 0, 255), 3)
# 计算似圆度
P_circle = largest_area * 4.0 / (3.14 * Real_Major_Axis_Length * Real_Major_Axis_Length)
P_circle = round(P_circle, 2)
print "似圆度 = " + str(P_circle)


cv2.putText(origin, 'S_maxContour : ' + str(largest_area), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)
cv2.putText(origin, 'Major_Axis: ' + str(Real_Major_Axis_Length), (50, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)
cv2.putText(origin, 'P_circle: ' + str(P_circle), (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 50, 50), 2, cv2.LINE_AA)


# 显示
cv2.namedWindow('Butterfly', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Butterfly', origin)
cv2.imwrite('picture/p-circle.png',origin)

k = cv2.waitKey(0)

# 'ESC'
if k == 27:
    cv2.destroyAllWindows()