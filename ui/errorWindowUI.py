# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_errorWindow(object):
    def setupUi(self, errorWindow):
        if not errorWindow.objectName():
            errorWindow.setObjectName(u"errorWindow")
        errorWindow.resize(400, 137)
        self.label = QLabel(errorWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 251, 31))
        self.label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 22px;\n"
"color: red;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(errorWindow)

        QMetaObject.connectSlotsByName(errorWindow)
    # setupUi

    def retranslateUi(self, errorWindow):
        errorWindow.setWindowTitle(QCoreApplication.translate("errorWindow", u"Error window", None))
        self.label.setText(QCoreApplication.translate("errorWindow", u"Something went wrong!", None))
    # retranslateUi

