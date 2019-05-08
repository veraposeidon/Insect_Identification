# coding=utf-8
# 获取五个特征

import cv2
import math
import numpy as np




def GetFiveFeatures(frame):
    # 判空
    if frame == None:
        return [False, 0.0, 0.0, 0.0, 0.0, 0.0, frame]
    origin = frame
    grayimage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

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

    print "最大面积" + str(largest_area)
    maxContour = contours[1][largest_contour_index]

    # 画轮廓
    cv2.drawContours(origin, maxContour, -1, (0, 0, 255), 2)

    # 1. 矩形度

    # 查找最小外接矩形
    minAreaRect = cv2.minAreaRect(maxContour)
    box = cv2.boxPoints(minAreaRect)
    box = np.int0(box)

    # 画轮廓
    cv2.drawContours(origin, [box], 0, (0, 255, 0), 2)

    # 计算最小外接矩形面积
    minAreaRect_Area = int(cv2.contourArea(box, False))
    print "最小外接矩形面积" + str(minAreaRect_Area)

    # 错误判断，如果分母为零，直接报错
    if minAreaRect_Area == 0.0:
        return [False, 0.0, 0.0, 0.0, 0.0, 0.0, origin]

    # 特征一：矩形度的计算
    P_rect = largest_area * 1.0 / minAreaRect_Area
    # 统一结果为3位有理数
    P_rect = round(P_rect, 3)
    print "矩形度" + str(P_rect)

    # 2. 延长度
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

    # 找短轴
    # 1. 先得到长轴直线的表达式y=k*x+b，用来计算点到直线距离和判断点在直线上方还是下方
    Major_Axis_k = math.tan(Major_Axis_Angle * 3.14 / 180.0)
    Major_Axis_b = Centroid_y - Major_Axis_k * Centroid_x

    # 2. 点(x0,y0)到直线(Ax+By+C=0)的距离为d =abs (A*x0+B*y0+C)/sqrt(A^2+B^2)
    Minor_Axis_A = Major_Axis_k
    Minor_Axis_B = -1
    Minor_Axis_C = Major_Axis_b

    # 3. 遍历轮廓上的点
    Minor_Axis_Under_length = 0
    Minor_Axis_Above_length = 0
    Minor_Axis_Under_End_x = 0
    Minor_Axis_Under_End_y = 0
    Minor_Axis_Above_End_x = 0
    Minor_Axis_Above_End_y = 0

    # 轮廓点集
    ContourItems = maxContour.shape[0]
    for item in range(ContourItems):
        point_x = maxContour[item][0][0]
        point_y = maxContour[item][0][1]
        # 判断点在直线哪一侧
        # 上侧
        if point_y > int(Major_Axis_k * point_x + Major_Axis_b):
            # 点到直线距离
            dis = abs((Minor_Axis_A * point_x + Minor_Axis_B * point_y + Minor_Axis_C) / math.sqrt(
                Minor_Axis_A * Minor_Axis_A + Minor_Axis_B * Minor_Axis_B))
            if dis >= Minor_Axis_Above_length:
                Minor_Axis_Above_length = dis
                Minor_Axis_Above_End_x = point_x
                Minor_Axis_Above_End_y = point_y
        # 下侧
        elif point_y < int(Major_Axis_k * point_x + Major_Axis_b):
            # 点到直线距离
            dis = abs((Minor_Axis_A * point_x + Minor_Axis_B * point_y + Minor_Axis_C) / math.sqrt(
                Minor_Axis_A * Minor_Axis_A + Minor_Axis_B * Minor_Axis_B))
            if dis >= Minor_Axis_Under_length:
                Minor_Axis_Under_length = dis
                Minor_Axis_Under_End_x = point_x
                Minor_Axis_Under_End_y = point_y
                # 第三种可能就是轮廓与直线的交点

    # # 标记两个点,可以忽略
    cv2.circle(origin, (Minor_Axis_Above_End_x, Minor_Axis_Above_End_y), 4, (255, 255, 255), -1)
    cv2.circle(origin, (Minor_Axis_Under_End_x, Minor_Axis_Under_End_y), 4, (255, 255, 255), -1)
    # 画出两点直线
    cv2.line(origin, (Minor_Axis_Under_End_x, Minor_Axis_Under_End_y), (Minor_Axis_Above_End_x, Minor_Axis_Above_End_y),
             (0, 255, 255), 3)

    # 计算实际短轴长度
    Real_Minor_Axis_Length = math.sqrt(
        math.pow((Minor_Axis_Above_End_x - Minor_Axis_Under_End_x), 2) + math.pow(
            (Minor_Axis_Above_End_y - Minor_Axis_Under_End_y), 2))

    Real_Minor_Axis_Length = round(Real_Minor_Axis_Length, 1)
    print "短轴长度 = " + str(Real_Minor_Axis_Length)

    # 错误判断，如果分母为零，直接报错
    if Real_Minor_Axis_Length == 0.0:
        return [False, P_rect, 0.0, 0.0, 0.0, 0.0, origin]
    # 计算延长度
    P_extend = Real_Major_Axis_Length * 1.0 / Real_Minor_Axis_Length
    P_extend = round(P_extend, 3)

    print "延长度 = " + str(P_extend)
    # 画出与长轴距离最远的两点的辅助线,使用时可以不用，画图用作论文使用
    # 画出长轴右方
    line_above_k = math.tan((Major_Axis_Angle - 90) * 3.14 / 180.0)
    line_above_b = Minor_Axis_Above_End_y - line_above_k * Minor_Axis_Above_End_x
    Minor_Axis_Above_Begin_x = int((line_above_b - Major_Axis_b) / (Major_Axis_k - line_above_k))
    Minor_Axis_Above_Begin_y = int(line_above_k * Minor_Axis_Above_Begin_x + line_above_b)
    cv2.line(origin, (Minor_Axis_Above_Begin_x, Minor_Axis_Above_Begin_y),
             (Minor_Axis_Above_End_x, Minor_Axis_Above_End_y),
             (255, 0, 255), 3)

    line_under_k = math.tan((Major_Axis_Angle - 90) * 3.14 / 180.0)
    line_under_b = Minor_Axis_Under_End_y - line_under_k * Minor_Axis_Under_End_x
    Minor_Axis_Under_Begin_x = int((line_under_b - Major_Axis_b) / (Major_Axis_k - line_under_k))
    Minor_Axis_Under_Begin_y = int(line_under_k * Minor_Axis_Under_Begin_x + line_under_b)
    cv2.line(origin, (Minor_Axis_Under_Begin_x, Minor_Axis_Under_Begin_y),
             (Minor_Axis_Under_End_x, Minor_Axis_Under_End_y),
             (255, 255, 0), 3)

    # 3. 球状型
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

    # 错误判断，如果分母为零，直接报错
    if max_radius == 0.0:
        return [False, P_rect, P_extend, 0.0, 0.0, 0.0, origin]

    P_spherical = min_radius * 1.0 / max_radius
    P_spherical = round(P_spherical, 3)
    print "球状型： " + str(P_spherical)


    # 错误判断，如果分母为零，直接报错
    if Real_Major_Axis_Length == 0.0:
        return [False, P_rect, P_extend, P_spherical, 0.0, 0.0, origin]
    # 4. 叶状型
    P_leaf = min_radius * 1.0 / Real_Major_Axis_Length
    P_leaf = round(P_leaf, 3)
    print "叶状型 = " + str(P_leaf)

    # 错误判断，如果分母为零，直接报错
    if Real_Major_Axis_Length == 0.0:
        return [False, P_rect, P_extend, P_spherical, P_leaf, 0.0, origin]
    # 5. 似圆度
    P_circle = largest_area * 4.0 / (3.14 * Real_Major_Axis_Length * Real_Major_Axis_Length)
    P_circle = round(P_circle, 2)
    print "似圆度 = " + str(P_circle)

    # 错误判断，如果分母为零，直接报错
    if Real_Major_Axis_Length == 0.0:
        return [False, P_rect, P_extend, P_spherical, P_leaf, P_circle, origin]
    # 6. 复杂度
    ArcLength = cv2.arcLength(maxContour, True)
    P_complecate = ArcLength * ArcLength * 1.0 / (4 * 3.14 * largest_area)
    P_complecate = round(P_complecate, 2)
    print "复杂度 = " + str(P_complecate)

    # 可以捎带返回处理完之后的画完辅助线的图
    return [True, P_rect, P_extend, P_spherical, P_leaf, P_circle, origin]
    # return [P_rect, P_extend, P_spherical, P_leaf, P_circle,P_complecate, origin]
