from MenuConfigWindow import MenuConfigWindow
from data.AddSignalConfigWindowData import AddSignalConfigWindowData
from PySide6.QtWidgets import QFileDialog


class AddSignalConfigWindow(MenuConfigWindow):
    def __init__(self, uiClass, callbackDoneFunc=None):
        super().__init__(uiClass)
        self.__data = AddSignalConfigWindowData()
        self.__callbackDoneFunc = callbackDoneFunc
        self.__configurateButtonsHandlers()

    def __configurateButtonsHandlers(self):
        self._ui.chooseFilePushBtn.clicked.connect(self.__chooseFilePushBtnHandler)
        self._ui.deleteFilePushBtn.clicked.connect(self.__deleteFilePushBtnHandler)
        self._ui.configDonePushBtn.clicked.connect(self.__configDonePushBtnHandler)

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
        self.__data.setNormalizeAmplitude(self._ui.normalizeAmplitudeCheckBox.isChecked())
        if self.__callbackDoneFunc:
            self.__callbackDoneFunc(self.__data)
        self.close()
