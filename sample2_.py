#coding=utf-8
#展示样本图片
from PIL import Image
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=20)


path = "E:/Documents/Python_Script/Insect_Identification/picture"

cang = Image.open(path+'/cangtest0.png')
cang1 = Image.open(path+'/ttt.png')
ricetest = Image.open(path+'/ricetest.png')

plt.subplot(1,3,1)
plt.title(u'粘板局部',fontproperties=font)
plt.imshow(cang)
plt.axis('off')     #不显示坐标尺寸

plt.subplot(1,3,2)
plt.title(u'粘板整体',fontproperties=font)   #第三幅图片标题
plt.imshow(cang1)
plt.axis('off')     #不显示坐标尺寸

plt.subplot(1,3,3)
plt.title(u'大米测试样本',fontproperties=font)   #第三幅图片标题
plt.imshow(ricetest)
plt.axis('off')     #不显示坐标尺寸

plt.show()