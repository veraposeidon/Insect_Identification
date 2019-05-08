#coding=utf-8
#显示计数效果

import cv2
import math
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=20)

path = "E:/Documents/Python_Script/Insect_Identification/picture"

cang = Image.open(path+'/ttt.png')
cangnum = Image.open(path+'/tttresult.jpg')

title = [u'原始图', u'计数结果']

plt.subplot(1, 2, 1)
plt.imshow(cang)
plt.title(title[0],fontproperties=font)
plt.axis('off')     #不显示坐标尺寸

plt.subplot(1, 2, 2)
plt.imshow(cangnum,'gray')
plt.title(title[1],fontproperties=font)
plt.axis('off')     #不显示坐标尺寸


plt.show()