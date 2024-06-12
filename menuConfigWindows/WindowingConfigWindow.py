from MenuConfigWindow import MenuConfigWindow
from enums.WindowFunctions import WindowFunctions
from data.WindowingConfigWindowData import WindowingConfigWindowData
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt


class WindowingConfigWindow(MenuConfigWindow):
    def __init__(self, uiClass, callbackDoneFunc=None):
        super().__init__(uiClass)
        self.__checkBoxes = [
            self._ui.bohmanWindowCheckBox,
            self._ui.barlettWindowCheckBox,
            self._ui.blackmannWindowCheckBox,
            self._ui.barlettHannCheckBox,
            self._ui.lanczosWindowCheckBox,
            self._ui.hammingWindowCheckBox,
            self._ui.hannWindowCheckBox,
            self._ui.gaussianWindowCheckBox,
            self._ui.kaiserWindowCheckBox,
            self._ui.triangularWindowCheckBox
        ]
        self.__data = WindowingConfigWindowData()
        self.__callbackDoneFunc = callbackDoneFunc
        self.__configurateButtonsHandlers()
        self.__configurateCheckBoxesHandlers()

    def __configurateButtonsHandlers(self):
        self._ui.chooseFilePushBtn.clicked.connect(self.__chooseFilePushBtnHandler)
        self._ui.deleteFilePushBtn.clicked.connect(self.__deleteFilePushBtnHandler)
        self._ui.configDonePushBtn.clicked.connect(self.__configDonePushBtnHandler)

    def __configurateCheckBoxesHandlers(self):
        for chBox in self.__checkBoxes:
            chBox.stateChanged.connect(self.__checkBoxCheckHandler)

    def __checkBoxCheckHandler(self, state):
        if state == Qt.CheckState.Checked.value:
            self.__uncheckAllCheckBoxesInsteadOf(self.sender())

    def __chooseFilePushBtnHandler(self):
        file = QFileDialog.getOpenFileUrl(filter='WAV (*.wav)')
        self.__data.setFileUrl(file[0].url().replace('file:///', ''))
        self.__data.setFileName(file[0].fileName())
        if len(file[0].url()) != 0:
            self._ui.fileNameLabel.setText(file[0].fileName())

    def __deleteFilePushBtnHandler(self):
        self._ui.fileNameLabel.setText('Choose wav file')
        self.__data.setFileUrl('')
        self.__data.setFileName('')

    def __configDonePushBtnHandler(self):
        if self._ui.bohmanWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.BOHMAN)
        if self._ui.barlettWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.BARLETT)
        if self._ui.blackmannWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.BLACKMANN)
        if self._ui.barlettHannCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.BARLETT_HANN)
        if self._ui.lanczosWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.LANCZOS)
        if self._ui.hammingWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.HAMMING)
        if self._ui.hannWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.HANN)
        if self._ui.gaussianWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.GAUSSIAN)
        if self._ui.kaiserWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.KAISER)
        if self._ui.triangularWindowCheckBox.isChecked():
            self.__data.setWindowFunc(WindowFunctions.TRIANGULAR)

        windowFunc = self.__data.getWindowFunc()
        windowParam = ''
        if windowFunc == WindowFunctions.KAISER:
            windowParam = self._ui.betaParamInput.text()
        if windowFunc == WindowFunctions.GAUSSIAN:
            windowParam = self._ui.sigmaParamInput.text()

        try:
            self.__data.setWindowParam(float(windowParam))
        except:
            self.__data.setWindowParam(None)

        if self.__callbackDoneFunc:
            self.__callbackDoneFunc(self.__data)
        self.close()

    def __uncheckAllCheckBoxesInsteadOf(self, target):
        for chBox in self.__checkBoxes:
            if chBox is not target:
                chBox.setChecked(False)
