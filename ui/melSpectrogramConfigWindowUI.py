# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'melSpectrogramConfigWindow.ui'
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

class Ui_melSpectrogramConfigWindow(object):
    def setupUi(self, melSpectrogramConfigWindow):
        if not melSpectrogramConfigWindow.objectName():
            melSpectrogramConfigWindow.setObjectName(u"melSpectrogramConfigWindow")
        melSpectrogramConfigWindow.resize(400, 300)
        self.convertToDecibelsCheckBox = QCheckBox(melSpectrogramConfigWindow)
        self.convertToDecibelsCheckBox.setObjectName(u"convertToDecibelsCheckBox")
        self.convertToDecibelsCheckBox.setGeometry(QRect(20, 120, 131, 20))
        self.fileNameLabel = QLabel(melSpectrogramConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 30, 261, 16))
        self.chooseFilePushBtn = QPushButton(melSpectrogramConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 30, 75, 24))
        self.deleteFilePushBtn = QPushButton(melSpectrogramConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 60, 75, 24))
        self.configDonePushBtn = QPushButton(melSpectrogramConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(150, 220, 75, 24))

        self.retranslateUi(melSpectrogramConfigWindow)

        QMetaObject.connectSlotsByName(melSpectrogramConfigWindow)
    # setupUi

    def retranslateUi(self, melSpectrogramConfigWindow):
        melSpectrogramConfigWindow.setWindowTitle(QCoreApplication.translate("melSpectrogramConfigWindow", u"Mel-spectrogram config", None))
        self.convertToDecibelsCheckBox.setText(QCoreApplication.translate("melSpectrogramConfigWindow", u"Convert to decibels", None))
        self.fileNameLabel.setText(QCoreApplication.translate("melSpectrogramConfigWindow", u"Choose wav file", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("melSpectrogramConfigWindow", u"File", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("melSpectrogramConfigWindow", u"Delete", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("melSpectrogramConfigWindow", u"Done", None))
    # retranslateUi

