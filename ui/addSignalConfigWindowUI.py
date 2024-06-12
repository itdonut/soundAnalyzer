# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addSignalConfigWindow.ui'
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

class Ui_addSignalConfigWindow(object):
    def setupUi(self, addSignalConfigWindow):
        if not addSignalConfigWindow.objectName():
            addSignalConfigWindow.setObjectName(u"addSignalConfigWindow")
        addSignalConfigWindow.resize(400, 300)
        self.chooseFilePushBtn = QPushButton(addSignalConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 30, 75, 24))
        self.fileNameLabel = QLabel(addSignalConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 30, 261, 16))
        self.deleteFilePushBtn = QPushButton(addSignalConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 60, 75, 24))
        self.configDonePushBtn = QPushButton(addSignalConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(160, 210, 75, 24))
        self.normalizeAmplitudeCheckBox = QCheckBox(addSignalConfigWindow)
        self.normalizeAmplitudeCheckBox.setObjectName(u"normalizeAmplitudeCheckBox")
        self.normalizeAmplitudeCheckBox.setGeometry(QRect(20, 100, 141, 20))
        self.normalizeAmplitudeCheckBox.setChecked(True)

        self.retranslateUi(addSignalConfigWindow)

        QMetaObject.connectSlotsByName(addSignalConfigWindow)
    # setupUi

    def retranslateUi(self, addSignalConfigWindow):
        addSignalConfigWindow.setWindowTitle(QCoreApplication.translate("addSignalConfigWindow", u"Wave form config", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("addSignalConfigWindow", u"File", None))
        self.fileNameLabel.setText(QCoreApplication.translate("addSignalConfigWindow", u"Choose wav file", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("addSignalConfigWindow", u"Delete", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("addSignalConfigWindow", u"Done", None))
        self.normalizeAmplitudeCheckBox.setText(QCoreApplication.translate("addSignalConfigWindow", u"Normalize amplitude", None))
    # retranslateUi

