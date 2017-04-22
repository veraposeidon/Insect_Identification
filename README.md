# Insect_Identification
##项目介绍：
####名称：
基于机器视觉的害虫种类及数量检测
####要求：
数目检测和昆虫种类识别

##项目进度

- [x] 2017/4/8---------二值化 
- [x] 2017/4/9---------图片中昆虫虫体计数 
- [x] 2017/4/22-------PyQt和OpenCV_VideoFrame结合做出基本界面
- [ ] 摄像头Frame中检测虫体数目，并在界面中显示标出
- [ ] 学习昆虫图像特征的提取，参考论文中提出的几个特征量
- [ ] 提取特征量并进行保存
- [ ] 按照神经网络方法搭建训练模型

##文件介绍
*   Thresholding.py----------大津法程序实现和OpenCV大津法函数的效果对比
*   Count.py-------------------实现加载图片，二值化（大津法），查找轮廓进行计数的效果
*   MainWindow.ui-----------PyQtDesigner设计的主界面文件
*   MainWindow.py----------PyUIC转换而成的主界面程序
*   VideoMainWindow.py-- PyQt结合OpenCV实现在界面中显示视频画面
##参考书籍
1.  《OpenCV3 计算机视觉Python语言实现》
2.  《机器学习》
3.  《Python机器学习实践与Kaggle实战》
 
##参考链接及对应解决方案
####计数
1. 大米计数（http://blog.csdn.net/jia20003/article/details/7605653）
2. 二值化大津法原理介绍（http://www.cnblogs.com/herway/archive/2011/09/23/2186698.html）
3. OpenCV二值化教程（http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding）

####界面
1. PyQt结合OpenCVVideoFrame(https://github.com/seym45/webcamViewer)
2. PyQt基础教程（http://zetcode.com/gui/pyqt5/）

####分类
1. 