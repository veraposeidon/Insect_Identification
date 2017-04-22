# coding=utf-8
# 二值化和大津法
# Otsu's Binarization
# 大津法细节介绍：
# http://www.cnblogs.com/herway/archive/2011/09/23/2186698.html
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding

import cv2
import numpy as np
from matplotlib import pyplot as plt

RiceImg = cv2.imread('picture/ricetest.png', 0)
blur = cv2.GaussianBlur(RiceImg, (5, 5), 0)
# find normalized_histogram, and its cumulative distribution function
hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.max()
Q = hist_norm.cumsum()

bins = np.arange(256)

fn_min = np.inf
thresh = -1

for i in xrange(1, 256):
    p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
    q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
    b1, b2 = np.hsplit(bins, [i])  # weights

    # finding means and variances
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2

    # calculates the minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print thresh, ret

ret1, manual = cv2.threshold(RiceImg, thresh, 255, cv2.THRESH_BINARY)
title = ['Origin', 'filter', 'manual', 'function']
images = [RiceImg, blur, manual, otsu]

for i in xrange(4):
    plt.subplot(1, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# 综上，OpenCV自带的OTSU效果最棒
