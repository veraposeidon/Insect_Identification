#coding=utf-8
#显示灰度图效果
from PIL import Image
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=15)


path = "E:/Documents/Python_Script/Insect_Identification/picture"

cang = Image.open(path+'/cangtest0gray.jpg')
rice = Image.open(path+'/ricetestgray.jpg')
flygray = Image.open(path+'/fly0gray.jpg')
zhizhugray = Image.open(path+'/zhizhu0gray.jpg')

plt.subplot(2,2,1)
plt.title(u'蝴蝶灰度图',fontproperties=font)
plt.imshow(flygray,plt.cm.gray)
plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,2)
plt.title(u'蜘蛛灰度图',fontproperties=font)   #第三幅图片标题
plt.imshow(zhizhugray,plt.cm.gray)
plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,3)
plt.title(u'粘板灰度图',fontproperties=font)   #第三幅图片标题
plt.imshow(cang,plt.cm.gray)
plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,4)
plt.title(u'大米灰度图',fontproperties=font)   #第三幅图片标题
plt.imshow(rice,plt.cm.gray)
plt.axis('off')     #不显示坐标尺寸

plt.show()