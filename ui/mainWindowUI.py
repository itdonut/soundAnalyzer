# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QWidget)
# import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1528, 790)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addSignalPushBtn = QPushButton(self.centralwidget)
        self.addSignalPushBtn.setObjectName(u"addSignalPushBtn")
        self.addSignalPushBtn.setGeometry(QRect(30, 10, 180, 50))
        self.addSignalPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSignalPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.fourierTransformPushBtn = QPushButton(self.centralwidget)
        self.fourierTransformPushBtn.setObjectName(u"fourierTransformPushBtn")
        self.fourierTransformPushBtn.setGeometry(QRect(30, 80, 180, 50))
        self.fourierTransformPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fourierTransformPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.filtersPushBtn = QPushButton(self.centralwidget)
        self.filtersPushBtn.setObjectName(u"filtersPushBtn")
        self.filtersPushBtn.setGeometry(QRect(30, 150, 180, 50))
        self.filtersPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.filtersPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.windowingPushBtn = QPushButton(self.centralwidget)
        self.windowingPushBtn.setObjectName(u"windowingPushBtn")
        self.windowingPushBtn.setGeometry(QRect(30, 220, 180, 50))
        self.windowingPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.windowingPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.spectrogramPushBtn = QPushButton(self.centralwidget)
        self.spectrogramPushBtn.setObjectName(u"spectrogramPushBtn")
        self.spectrogramPushBtn.setGeometry(QRect(30, 290, 180, 50))
        self.spectrogramPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.spectrogramPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.melSpectrogramPushBtn = QPushButton(self.centralwidget)
        self.melSpectrogramPushBtn.setObjectName(u"melSpectrogramPushBtn")
        self.melSpectrogramPushBtn.setGeometry(QRect(30, 360, 180, 50))
        self.melSpectrogramPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.melSpectrogramPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.chromagramPushBtn = QPushButton(self.centralwidget)
        self.chromagramPushBtn.setObjectName(u"chromagramPushBtn")
        self.chromagramPushBtn.setGeometry(QRect(30, 430, 180, 50))
        self.chromagramPushBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chromagramPushBtn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"font-size: 18px;")
        self.plotsTabWidget = QTabWidget(self.centralwidget)
        self.plotsTabWidget.setObjectName(u"plotsTabWidget")
        self.plotsTabWidget.setGeometry(QRect(240, 10, 1281, 771))
        self.plotsTabWidget.setStyleSheet(u"pane {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.plotsTabWidget.setTabsClosable(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 600, 151, 131))
        self.label.setStyleSheet(u"image: url(./resources/logo.png);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.plotsTabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sound Analyzer", None))
        self.addSignalPushBtn.setText(QCoreApplication.translate("MainWindow", u"Wave form", None))
        self.fourierTransformPushBtn.setText(QCoreApplication.translate("MainWindow", u"Fourier Transform", None))
        self.filtersPushBtn.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.windowingPushBtn.setText(QCoreApplication.translate("MainWindow", u"Windowing", None))
        self.spectrogramPushBtn.setText(QCoreApplication.translate("MainWindow", u"Spectrogram", None))
        self.melSpectrogramPushBtn.setText(QCoreApplication.translate("MainWindow", u"Mel-spectrogram", None))
        self.chromagramPushBtn.setText(QCoreApplication.translate("MainWindow", u"Chromagram", None))
        self.label.setText("")
    # retranslateUi

