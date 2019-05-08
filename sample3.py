#coding=utf-8
#显示大津法效果

import cv2
import math
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=20)

path = "E:/Documents/Python_Script/Insect_Identification/dataset"

fly = Image.open(path+'/fly0.jpg')

#  此处读入图片，作为接口
origin = cv2.imread('dataset/fly0.jpg')
grayimage = cv2.imread('dataset/fly0.jpg', 0)

# 　高斯滤波
blur = cv2.GaussianBlur(grayimage, (5, 5), 0)

# 　二值化：用大津法，此处选项若是THRESH_BINARY_INV，则同意选用白色背景的图片样本
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

title = [u'原始图', u'灰度图', u'二值化图']

plt.subplot(1, 3, 1)
plt.imshow(fly)
plt.title(title[0],fontproperties=font)

plt.subplot(1, 3, 2)
plt.imshow(blur,'gray')
plt.title(title[1],fontproperties=font)

plt.subplot(1, 3, 3)
plt.imshow(otsu,'gray')
plt.title(title[2],fontproperties=font)

plt.show()