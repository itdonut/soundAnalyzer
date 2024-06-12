# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filtersConfigWindow.ui'
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
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_filtersConfigWindow(object):
    def setupUi(self, filtersConfigWindow):
        if not filtersConfigWindow.objectName():
            filtersConfigWindow.setObjectName(u"filtersConfigWindow")
        filtersConfigWindow.resize(400, 300)
        self.lowPassFilterCheckBox = QCheckBox(filtersConfigWindow)
        self.lowPassFilterCheckBox.setObjectName(u"lowPassFilterCheckBox")
        self.lowPassFilterCheckBox.setGeometry(QRect(10, 50, 75, 20))
        self.highPassFilterCheckBox = QCheckBox(filtersConfigWindow)
        self.highPassFilterCheckBox.setObjectName(u"highPassFilterCheckBox")
        self.highPassFilterCheckBox.setGeometry(QRect(10, 80, 75, 20))
        self.bandPassFilterCheckBox = QCheckBox(filtersConfigWindow)
        self.bandPassFilterCheckBox.setObjectName(u"bandPassFilterCheckBox")
        self.bandPassFilterCheckBox.setGeometry(QRect(10, 110, 75, 20))
        self.filterOrderSpinBox = QSpinBox(filtersConfigWindow)
        self.filterOrderSpinBox.setObjectName(u"filterOrderSpinBox")
        self.filterOrderSpinBox.setGeometry(QRect(330, 140, 42, 22))
        self.filterOrderSpinBox.setMinimum(1)
        self.filterOrderSpinBox.setMaximum(4)
        self.label = QLabel(filtersConfigWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 140, 71, 20))
        self.freqFromInput = QLineEdit(filtersConfigWindow)
        self.freqFromInput.setObjectName(u"freqFromInput")
        self.freqFromInput.setEnabled(False)
        self.freqFromInput.setGeometry(QRect(80, 170, 113, 21))
        self.label_2 = QLabel(filtersConfigWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 170, 61, 16))
        self.label_3 = QLabel(filtersConfigWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 200, 61, 16))
        self.freqToInput = QLineEdit(filtersConfigWindow)
        self.freqToInput.setObjectName(u"freqToInput")
        self.freqToInput.setEnabled(False)
        self.freqToInput.setGeometry(QRect(80, 200, 113, 21))
        self.freqInput = QLineEdit(filtersConfigWindow)
        self.freqInput.setObjectName(u"freqInput")
        self.freqInput.setEnabled(False)
        self.freqInput.setGeometry(QRect(80, 140, 113, 21))
        self.label_4 = QLabel(filtersConfigWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 61, 16))
        self.chooseFilePushBtn = QPushButton(filtersConfigWindow)
        self.chooseFilePushBtn.setObjectName(u"chooseFilePushBtn")
        self.chooseFilePushBtn.setGeometry(QRect(300, 20, 75, 24))
        self.chooseFilePushBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.fileNameLabel = QLabel(filtersConfigWindow)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(20, 20, 261, 16))
        self.deleteFilePushBtn = QPushButton(filtersConfigWindow)
        self.deleteFilePushBtn.setObjectName(u"deleteFilePushBtn")
        self.deleteFilePushBtn.setGeometry(QRect(300, 50, 75, 24))
        self.deleteFilePushBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.configDonePushBtn = QPushButton(filtersConfigWindow)
        self.configDonePushBtn.setObjectName(u"configDonePushBtn")
        self.configDonePushBtn.setGeometry(QRect(160, 250, 75, 24))
        self.configDonePushBtn.setCursor(QCursor(Qt.ArrowCursor))

        self.retranslateUi(filtersConfigWindow)

        QMetaObject.connectSlotsByName(filtersConfigWindow)
    # setupUi

    def retranslateUi(self, filtersConfigWindow):
        filtersConfigWindow.setWindowTitle(QCoreApplication.translate("filtersConfigWindow", u"Filters config", None))
        self.lowPassFilterCheckBox.setText(QCoreApplication.translate("filtersConfigWindow", u"Low-pass", None))
        self.highPassFilterCheckBox.setText(QCoreApplication.translate("filtersConfigWindow", u"High-pass", None))
        self.bandPassFilterCheckBox.setText(QCoreApplication.translate("filtersConfigWindow", u"Band-pass", None))
        self.label.setText(QCoreApplication.translate("filtersConfigWindow", u"Filter order", None))
        self.label_2.setText(QCoreApplication.translate("filtersConfigWindow", u"From (Hz)", None))
        self.label_3.setText(QCoreApplication.translate("filtersConfigWindow", u"To (Hz)", None))
        self.label_4.setText(QCoreApplication.translate("filtersConfigWindow", u"Freq (Hz)", None))
        self.chooseFilePushBtn.setText(QCoreApplication.translate("filtersConfigWindow", u"File", None))
        self.fileNameLabel.setText(QCoreApplication.translate("filtersConfigWindow", u"Choose wav file", None))
        self.deleteFilePushBtn.setText(QCoreApplication.translate("filtersConfigWindow", u"Delete", None))
        self.configDonePushBtn.setText(QCoreApplication.translate("filtersConfigWindow", u"Done", None))
    # retranslateUi

