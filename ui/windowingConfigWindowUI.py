# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowingConfigWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_windowingConfigWindow(object):
    def setupUi(self, windowingConfigWindow):
        if not windowingConfigWindow.objectName():
            windowingConfigWindow.setObjectName(u"windowingConfigWindow")
        windowingConfigWindow.resize(400, 300)
        self.bohmanWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.bohmanWindowCheckBox.setObjectName(u"bohmanWindowCheckBox")
        self.bohmanWindowCheckBox.setGeometry(QRect(20, 70, 75, 20))
        self.barlettWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.barlettWindowCheckBox.setObjectName(u"barlettWindowCheckBox")
        self.barlettWindowCheckBox.setGeometry(QRect(20, 100, 75, 20))
        self.blackmannWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.blackmannWindowCheckBox.setObjectName(u"blackmannWindowCheckBox")
        self.blackmannWindowCheckBox.setGeometry(QRect(20, 130, 81, 20))
        self.barlettHannCheckBox = QCheckBox(windowingConfigWindow)
        self.barlettHannCheckBox.setObjectName(u"barlettHannCheckBox")
        self.barlettHannCheckBox.setGeometry(QRect(20, 160, 91, 20))
        self.lanczosWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.lanczosWindowCheckBox.setObjectName(u"lanczosWindowCheckBox")
        self.lanczosWindowCheckBox.setGeometry(QRect(20, 190, 75, 20))
        self.hammingWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.hammingWindowCheckBox.setObjectName(u"hammingWindowCheckBox")
        self.hammingWindowCheckBox.setGeometry(QRect(130, 70, 75, 20))
        self.hannWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.hannWindowCheckBox.setObjectName(u"hannWindowCheckBox")
        self.hannWindowCheckBox.setGeometry(QRect(130, 100, 75, 20))
        self.gaussianWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.gaussianWindowCheckBox.setObjectName(u"gaussianWindowCheckBox")
        self.gaussianWindowCheckBox.setGeometry(QRect(130, 160, 75, 20))
        self.kaiserWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.kaiserWindowCheckBox.setObjectName(u"kaiserWindowCheckBox")
        self.kaiserWindowCheckBox.setGeometry(QRect(130, 190, 75, 20))
        self.triangularWindowCheckBox = QCheckBox(windowingConfigWindow)
        self.triangularWindowCheckBox.setObjectName(u"triangularWindowCheckBox")
        self.triangularWindowCheckBox.setGeometry(QRect(130, 130, 75, 20))
        self.chooseFilePushBtn = QPushButton(windowingConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 20, 75, 24))
        self.chooseFilePushBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.deleteFilePushBtn = QPushButton(windowingConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 50, 75, 24))
        self.deleteFilePushBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.configDonePushBtn = QPushButton(windowingConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(160, 240, 75, 24))
        self.configDonePushBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.fileNameLabel = QLabel(windowingConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 20, 261, 16))
        self.label = QLabel(windowingConfigWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 190, 71, 20))
        self.betaParamInput = QLineEdit(windowingConfigWindow)
        self.betaParamInput.setObjectName(u"betaParamInput")
        self.betaParamInput.setGeometry(QRect(220, 190, 61, 21))
        self.label_2 = QLabel(windowingConfigWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 160, 91, 20))
        self.sigmaParamInput = QLineEdit(windowingConfigWindow)
        self.sigmaParamInput.setObjectName(u"sigmaParamInput")
        self.sigmaParamInput.setGeometry(QRect(220, 160, 61, 21))

        self.retranslateUi(windowingConfigWindow)

        QMetaObject.connectSlotsByName(windowingConfigWindow)
    # setupUi

    def retranslateUi(self, windowingConfigWindow):
        windowingConfigWindow.setWindowTitle(QCoreApplication.translate("windowingConfigWindow", u"Windowing config", None))
        self.bohmanWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Bohman", None))
        self.barlettWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Barlett", None))
        self.blackmannWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Blackmann", None))
        self.barlettHannCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Barlett-Hann", None))
        self.lanczosWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Lanczos ", None))
        self.hammingWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Hamming ", None))
        self.hannWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Hann ", None))
        self.gaussianWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Gaussian ", None))
        self.kaiserWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Kaiser", None))
        self.triangularWindowCheckBox.setText(QCoreApplication.translate("windowingConfigWindow", u"Triangular ", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("windowingConfigWindow", u"File", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("windowingConfigWindow", u"Delete", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("windowingConfigWindow", u"Done", None))
        self.fileNameLabel.setText(QCoreApplication.translate("windowingConfigWindow", u"Choose wav file", None))
        self.label.setText(QCoreApplication.translate("windowingConfigWindow", u"Beta (Kaiser)", None))
        self.label_2.setText(QCoreApplication.translate("windowingConfigWindow", u"Sigma (Gaussian)", None))
    # retranslateUi

