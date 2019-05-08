#coding=utf-8
from PIL import Image
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)


path = "E:/Documents/Python_Script/Insect_Identification/dataset"

fly = Image.open(path+'/fly0.jpg')
zhizhu = Image.open(path + '/zhizhu0.jpg')
jingui = Image.open(path + '/jingui2.jpg')
wo = Image.open(path + '/wo0.jpg')

plt.subplot(2,2,1)
plt.title(u'蝴蝶样本',fontproperties=font)
plt.imshow(fly)

plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,2)
plt.title(u'蜘蛛样本',fontproperties=font)   #第三幅图片标题
plt.imshow(zhizhu)

plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,3)
plt.title(u'金龟子样本',fontproperties=font)   #第三幅图片标题
plt.imshow(jingui)

plt.axis('off')     #不显示坐标尺寸

plt.subplot(2,2,4)
plt.title(u'蜗牛样本',fontproperties=font)   #第三幅图片标题
plt.imshow(wo)

plt.axis('off')     #不显示坐标尺寸

plt.show()