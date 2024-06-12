from MenuConfigWindow import MenuConfigWindow
from FilterType import FilterType
from data.FilteringConfigWindowData import FilteringConfigWindowData
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt


class FiltersConfigWindow(MenuConfigWindow):
    def __init__(self, uiClass, callbackDoneFunc=None):
        super().__init__(uiClass)
        self.__checkBoxes = [
            self._ui.lowPassFilterCheckBox,
            self._ui.highPassFilterCheckBox,
            self._ui.bandPassFilterCheckBox
        ]
        self.__data = FilteringConfigWindowData()
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
            sender = self.sender()
            self.__uncheckAllCheckBoxesInsteadOf(sender)

        elif state == Qt.CheckState.Unchecked.value:
            self._ui.freqFromInput.setEnabled(False)
            self._ui.freqToInput.setEnabled(False)
            self._ui.freqInput.setEnabled(False)

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
        if self._ui.lowPassFilterCheckBox.isChecked():
            self.__data.setFilterType(FilterType.LOWPASS)
        if self._ui.highPassFilterCheckBox.isChecked():
            self.__data.setFilterType(FilterType.HIGHPASS)
        if self._ui.bandPassFilterCheckBox.isChecked():
            self.__data.setFilterType(FilterType.BANDPASS)

        filterOrder = self._ui.filterOrderSpinBox.value()
        freq = self._ui.freqInput.text()
        freqFrom = self._ui.freqFromInput.text()
        freqTo = self._ui.freqToInput.text()

        try:
            self.__data.setFilterOrder(int(filterOrder))
        except:
            self.__data.setFilterOrder(None)

        try:
            self.__data.setFreq(float(freq))
        except:
            self.__data.setFreq(None)

        try:
            self.__data.setFreqTo(float(freqTo))
        except:
            self.__data.setFreqTo(None)

        try:
            self.__data.setFreqFrom(float(freqFrom))
        except:
            self.__data.setFreqFrom(None)

        if self.__callbackDoneFunc:
            self.__callbackDoneFunc(self.__data)
        self.close()

    def __uncheckAllCheckBoxesInsteadOf(self, target):
        for chBox in self.__checkBoxes:
            if chBox is not target:
                chBox.setChecked(False)

        if target is self._ui.lowPassFilterCheckBox or target is self._ui.highPassFilterCheckBox:
            self._ui.freqInput.setEnabled(True)
            self._ui.freqFromInput.setEnabled(False)
            self._ui.freqToInput.setEnabled(False)
        elif target is self._ui.bandPassFilterCheckBox:
            self._ui.freqInput.setEnabled(False)
            self._ui.freqFromInput.setEnabled(True)
            self._ui.freqToInput.setEnabled(True)
