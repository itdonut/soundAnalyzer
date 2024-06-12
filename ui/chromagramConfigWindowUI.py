# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chromagramConfigWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_chromagramConfigWindow(object):
    def setupUi(self, chromagramConfigWindow):
        if not chromagramConfigWindow.objectName():
            chromagramConfigWindow.setObjectName(u"chromagramConfigWindow")
        chromagramConfigWindow.resize(400, 300)
        self.fileNameLabel = QLabel(chromagramConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 30, 261, 16))
        self.chooseFilePushBtn = QPushButton(chromagramConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 30, 75, 24))
        self.deleteFilePushBtn = QPushButton(chromagramConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 60, 75, 24))
        self.configDonePushBtn = QPushButton(chromagramConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(160, 210, 75, 24))

        self.retranslateUi(chromagramConfigWindow)

        QMetaObject.connectSlotsByName(chromagramConfigWindow)
    # setupUi

    def retranslateUi(self, chromagramConfigWindow):
        chromagramConfigWindow.setWindowTitle(QCoreApplication.translate("chromagramConfigWindow", u"Chromagram config", None))
        self.fileNameLabel.setText(QCoreApplication.translate("chromagramConfigWindow", u"Choose wav file", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("chromagramConfigWindow", u"File", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("chromagramConfigWindow", u"Delete", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("chromagramConfigWindow", u"Done", None))
    # retranslateUi

