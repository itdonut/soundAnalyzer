# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrogramConfigWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_spectrogramConfigWindow(object):
    def setupUi(self, spectrogramConfigWindow):
        if not spectrogramConfigWindow.objectName():
            spectrogramConfigWindow.setObjectName(u"spectrogramConfigWindow")
        spectrogramConfigWindow.resize(400, 300)
        self.convertToDecibelsCheckBox = QCheckBox(spectrogramConfigWindow)
        self.convertToDecibelsCheckBox.setObjectName(u"convertToDecibelsCheckBox")
        self.convertToDecibelsCheckBox.setGeometry(QRect(20, 80, 131, 20))
        self.view3dCheckBox = QCheckBox(spectrogramConfigWindow)
        self.view3dCheckBox.setObjectName(u"view3dCheckBox")
        self.view3dCheckBox.setGeometry(QRect(20, 110, 75, 20))
        self.configDonePushBtn = QPushButton(spectrogramConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(160, 220, 75, 24))
        self.chooseFilePushBtn = QPushButton(spectrogramConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 30, 75, 24))
        self.deleteFilePushBtn = QPushButton(spectrogramConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 60, 75, 24))
        self.fileNameLabel = QLabel(spectrogramConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 30, 261, 16))

        self.retranslateUi(spectrogramConfigWindow)

        QMetaObject.connectSlotsByName(spectrogramConfigWindow)
    # setupUi

    def retranslateUi(self, spectrogramConfigWindow):
        spectrogramConfigWindow.setWindowTitle(QCoreApplication.translate("spectrogramConfigWindow", u"Spectrogram config", None))
        self.convertToDecibelsCheckBox.setText(QCoreApplication.translate("spectrogramConfigWindow", u"Convert to decibels", None))
        self.view3dCheckBox.setText(QCoreApplication.translate("spectrogramConfigWindow", u"3D view", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("spectrogramConfigWindow", u"Done", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("spectrogramConfigWindow", u"File", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("spectrogramConfigWindow", u"Delete", None))
        self.fileNameLabel.setText(QCoreApplication.translate("spectrogramConfigWindow", u"Choose wav file", None))
    # retranslateUi

