from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class MenuConfigWindow(QWidget):
    def __init__(self, uiClass):
        super().__init__()
        self._ui = uiClass
        self._ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
