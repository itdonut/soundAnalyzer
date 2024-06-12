import sys
from PySide6.QtWidgets import QApplication
from GUI import GUI
from PySide6 import QtGui

# "image: url(./resources/logo.png);"
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('resources/logo.png'))
    GUI = GUI()
    GUI.init()
    sys.exit(app.exec())
