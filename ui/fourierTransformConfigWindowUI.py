# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fourierTransformConfigWindow.ui'
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

class Ui_fourierTransformConfigWindow(object):
    def setupUi(self, fourierTransformConfigWindow):
        if not fourierTransformConfigWindow.objectName():
            fourierTransformConfigWindow.setObjectName(u"fourierTransformConfigWindow")
        fourierTransformConfigWindow.resize(400, 300)
        self.configDonePushBtn = QPushButton(fourierTransformConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(150, 220, 75, 24))
        self.chooseFilePushBtn = QPushButton(fourierTransformConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 30, 75, 24))
        self.deleteFilePushBtn = QPushButton(fourierTransformConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 60, 75, 24))
        self.fileNameLabel = QLabel(fourierTransformConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 30, 261, 16))
        self.halfSpectrumCheckBox = QCheckBox(fourierTransformConfigWindow)
        self.halfSpectrumCheckBox.setObjectName(u"halfSpectrumCheckBox")
        self.halfSpectrumCheckBox.setGeometry(QRect(20, 110, 111, 20))
        self.positiveSpectrumCheckBox = QCheckBox(fourierTransformConfigWindow)
        self.positiveSpectrumCheckBox.setObjectName(u"positiveSpectrumCheckBox")
        self.positiveSpectrumCheckBox.setGeometry(QRect(20, 80, 101, 20))

        self.retranslateUi(fourierTransformConfigWindow)

        QMetaObject.connectSlotsByName(fourierTransformConfigWindow)
    # setupUi

    def retranslateUi(self, fourierTransformConfigWindow):
        fourierTransformConfigWindow.setWindowTitle(QCoreApplication.translate("fourierTransformConfigWindow", u"Fourier transform config", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("fourierTransformConfigWindow", u"Done", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("fourierTransformConfigWindow", u"File", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("fourierTransformConfigWindow", u"Delete", None))
        self.fileNameLabel.setText(QCoreApplication.translate("fourierTransformConfigWindow", u"Choose wav file", None))
        self.halfSpectrumCheckBox.setText(QCoreApplication.translate("fourierTransformConfigWindow", u"Half of spectrum", None))
        self.positiveSpectrumCheckBox.setText(QCoreApplication.translate("fourierTransformConfigWindow", u"Only positive", None))
    # retranslateUi

