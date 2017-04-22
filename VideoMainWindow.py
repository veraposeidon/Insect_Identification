# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow


class Video():
    def __init__(self, capture):
        self.capture = capture
        self.currentFrame = np.array([])

    def captureFrame(self):
        """
        capture frame and return captured frame
        """
        ret, readFrame = self.capture.read()
        return readFrame

    def captureNextFrame(self):
        """                           
        capture frame and reverse RBG BGR and return opencv image                                      
        """
        ret, readFrame = self.capture.read()
        if (ret == True):
            self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)

    def convertFrame(self):
        """     converts frame to format suitable for QtGui            """
        try:
            height, width = self.currentFrame.shape[:2]
            img = QImage(self.currentFrame, width, height, QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

    def convertSpecifiedFrame(frame):
        """     converts frame to format suitable for QtGui            """
        try:
            height, width = frame.shape[:2]
            img = QImage(frame, width, height, QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            return img
        except:
            return None

    def getImage(self):
        return cv2.imread("picture/test.jpg")


class GUI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video = Video(cv2.VideoCapture(0))
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(24)
        self.update()
        self.ui.btnCapture.clicked.connect(self.cb)
        self.ui.btnAddText.clicked.connect(self.addText)

        self.ret, self.captureFrame = self.video.capture.read()

    def cb(self):
        self.video.captureNextFrame()
        frame = self.video.convertFrame()
        self.ui.videoFrame_2.setPixmap(frame)
        self.ui.videoFrame_2.setScaledContents(True)

        self.captureFrame = self.video.captureFrame()
        cv2.imwrite("picture/test.jpg", self.captureFrame)

        print 'Captured'

    def addText(self):
        imText = self.video.getImage()
        imOrg = self.video.getImage()
        text = "%s" % self.ui.TextFieldAddText.text()
        cv2.putText(imText, text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imwrite("picture/testText.jpg", imText)
        pixmap = QPixmap('picture/testText.jpg')
        self.ui.videoFrame_2.setPixmap(pixmap)
        print 'Text added' + text

    def play(self):
        try:
            self.video.captureNextFrame()
            self.ui.videoFrame.setPixmap(self.video.convertFrame())
            self.ui.videoFrame.setScaledContents(True)
        except TypeError:
            print "No Frame"
            print "No Frame"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = GUI()
    example.show()
    sys.exit(app.exec_())
