# Insect_Identification

## 项目介绍：

#### 名称：

基于机器视觉的害虫种类及数量检测

#### 要求：

数目检测和昆虫种类识别


## 项目进度


- [x] 2017/4/8---------二值化 
- [x] 2017/4/9---------图片中昆虫虫体计数 
- [x] 2017/4/22-------PyQt和OpenCV_VideoFrame结合做出基本界面
- [x] 摄像头Frame中检测虫体数目，并在界面中显示标出
- [x] 学习昆虫图像特征的提取，参考论文中提出的几个特征量
- [x] 提取特征量并进行保存
- [x] 按照神经网络方法搭建训练模型
- [x] 搭建了线性SVM分类训练器
- [x] 将特征提取和UI界面建立连接，实现拍照和预测判断一体

## 机器学习训练算法（参考Python机器学习）
*   LogisticRegression
*   SGDClassfier 还没有尝试
*   LinearSVM 
*   朴素贝叶斯 (文本分类，不用)
*   K邻近（分类）
*   决策树，不用
*   集成模型，不用

## 文件介绍

*   用户界面
    *   MainWindow.ui-----------------------PyQtDesigner设计的主界面文件
    *   MainWindow.py----------------------PyUIC转换而成的主界面程序
*   运行逻辑
    *   VideoMainWindow.py--------------PyQt结合OpenCV实现在界面中显示视频画面
    *   PreProcess.py-------------------------对源数据样本进行预处理
*   特征提取
    *   P_circle.py------------------------------似圆度
    *   P_extend.py----------------------------延长度
    *   P_leaf.py--------------------------------叶状性
    *   P_rect.py--------------------------------矩形度
    *   P_spherical.py------------------------球形度
    *   GetFeatures.py-----------------------提取特征的模块
    *   GetFiveFeatures.py-----------------五个特征提取的测试代码
    *   FeatureExtract.py-------------------提取样本库特征保存到CSV文件
    *   
*   机器学习模块
    *   LinearSVM.py-------------------------线性SVM分类器的训练和模型保存
    *   LinearRegression.py---------------逻辑回归分类器的训练和模型保存
    *   KneiborsClassfier.py---------------KNN分类器的训练和模型保存
    *   Predict.py------------------------------加载预训练模型，对特征进行预测
*   Thresholding.py---------------------------大津法程序实现和OpenCV大津法函数的效果对比
*   Count.py-------------------------------------实现加载图片，二值化（大津法），查找轮廓进行计数的效果
*   GetChineseName.py--------------------分类中英文转换

## 参考书籍

1.  《OpenCV3 计算机视觉Python语言实现》
2.  《机器学习》
3.  《Python机器学习实践与Kaggle实战》

## 参考链接及对应解决方案

#### 1. 计数

1. 大米计数（http://blog.csdn.net/jia20003/article/details/7605653）
2. 二值化大津法原理介绍（http://www.cnblogs.com/herway/archive/2011/09/23/2186698.html）
3. OpenCV二值化教程（http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding）

#### 2. 界面

1. PyQt结合OpenCVVideoFrame(https://github.com/seym45/webcamViewer)
2. PyQt基础教程（http://zetcode.com/gui/pyqt5/）

#### 3. 分类

久远，找不到资源了。

## 后记

这个是大四的时候的毕业设计。

其实并不是很实用，只能拿其清晰的标本图像来做测试。

用到了基本的图像处理、特征提取、机器学习分类器一些知识。