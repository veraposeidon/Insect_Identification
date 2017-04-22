# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.videoFrame = QtWidgets.QLabel(self.centralwidget)
        self.videoFrame.setGeometry(QtCore.QRect(10, 0, 341, 271))
        self.videoFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.videoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoFrame.setMidLineWidth(2)
        self.videoFrame.setObjectName("videoFrame")
        self.videoFrame_2 = QtWidgets.QLabel(self.centralwidget)
        self.videoFrame_2.setGeometry(QtCore.QRect(450, 0, 341, 271))
        self.videoFrame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.videoFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoFrame_2.setMidLineWidth(2)
        self.videoFrame_2.setObjectName("videoFrame_2")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapture.setGeometry(QtCore.QRect(140, 350, 75, 23))
        self.btnCapture.setObjectName("btnCapture")
        self.TextFieldAddText = QtWidgets.QLineEdit(self.centralwidget)
        self.TextFieldAddText.setGeometry(QtCore.QRect(470, 350, 201, 20))
        self.TextFieldAddText.setObjectName("TextFieldAddText")
        self.btnAddText = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddText.setGeometry(QtCore.QRect(540, 390, 75, 23))
        self.btnAddText.setWhatsThis("")
        self.btnAddText.setObjectName("btnAddText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.videoFrame.setText(_translate("MainWindow", "Video Frame"))
        self.videoFrame_2.setText(_translate("MainWindow", "Video Frame"))
        self.btnCapture.setText(_translate("MainWindow", "拍照"))
        self.btnAddText.setText(_translate("MainWindow", "添加文字"))

