from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFileDialog
from uuid import uuid4
from ui import (addSignalConfigWindowUI, mainWindowUI, fourierTransformConfigWindowUI,
                windowingConfigWindowUI, filtersConfigWindowUI, spectrogramConfigWindowUI,
                melSpectrogramConfigWindowUI, chromagramConfigWindowUI, errorWindowUI)
from menuConfigWindows.AddSignalConfigWindow import AddSignalConfigWindow
from menuConfigWindows.FourierTransformConfigWindow import FourierTransformConfigWindow
from menuConfigWindows.WindowingConfigWindow import WindowingConfigWindow
from menuConfigWindows.FiltersConfigWindow import FiltersConfigWindow
from menuConfigWindows.SpectrogramConfigWindow import SpectrogramConfigWindow
from menuConfigWindows.MelSpectrogramConfigWindow import MelSpectrogramConfigWindow
from menuConfigWindows.ChromagramConfigWindow import ChromagramConfigWindow
from ErrorWindow import ErrorWindow
from enums.WindowFunctions import WindowFunctions
from enums.FilterType import FilterType
from SoundAnalyzer import SoundAnalyzer
from PlotVisualizer import PlotVisualizer
from WavReader import WavReader
from SignalData import SignalData
from WavWriter import WavWriter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__soundAnalyzer = SoundAnalyzer()
        self.__ui = mainWindowUI.Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__configurateMenuButtonsHandlers()
        self.__configuratePlotsTabWidget()

    def __configurateMenuButtonsHandlers(self):
        self.__ui.addSignalPushBtn.clicked.connect(self.__addSignalBtnHandler)
        self.__ui.fourierTransformPushBtn.clicked.connect(self.__fourierTransformBtnHandler)
        self.__ui.filtersPushBtn.clicked.connect(self.__filtersBtnHandler)
        self.__ui.windowingPushBtn.clicked.connect(self.__windowingBtnHandler)
        self.__ui.spectrogramPushBtn.clicked.connect(self.__spectrogramBtnHandler)
        self.__ui.melSpectrogramPushBtn.clicked.connect(self.__melSpectrogramBtnHandler)
        self.__ui.chromagramPushBtn.clicked.connect(self.__chromagramBtnHandler)

    def __configuratePlotsTabWidget(self):
        self.__ui.plotsTabWidget.tabCloseRequested.connect(lambda index: self.__closeTab(index))

    def __addPlotTab(self, tabName: str):
        tab = QWidget()
        tab.setLayout(QVBoxLayout())
        self.__ui.plotsTabWidget.addTab(tab, tabName)
        return tab

    def __closeTab(self, index):
        tab = self.__ui.plotsTabWidget.widget(index)
        signalId = tab.property('signalId')
        if signalId is not None:
            self.__soundAnalyzer.deleteSignal(signalId)
        self.__ui.plotsTabWidget.removeTab(index)

    def __plotSignalWaveForm(self, fileUrl, ampNorm, tab, ylabel, saveWav: bool = False):
        signal, sr = WavReader.readWave(fileUrl, norm=ampNorm)
        PlotVisualizer.drawWaveForm(
            signal=signal,
            sampleRate=sr,
            title='Wave form',
            tab=tab,
            ylabel=ylabel,
            saveWav=saveWav
        )

    def __plotWindowing(self, fileUrl, tab, windowFunc: WindowFunctions, windowParam: float | None = None):
        signal, sr = WavReader.readWave(fileUrl)
        windowed = SoundAnalyzer.windowing(signal, windowFunc, windowParam)
        signalId = str(uuid4().hex)
        tab.setProperty('signalId', signalId)
        signalData = SignalData(windowed, sr, signalId)
        self.__soundAnalyzer.addSignal(signalData)
        title = f'Windowed wave form ({windowFunc.value})'
        if windowFunc == WindowFunctions.KAISER:
            title = f'Windowed wave form ({windowFunc.value}, $\\beta$={windowParam})'
        if windowFunc == WindowFunctions.GAUSSIAN:
            title = f'Windowed wave form ({windowFunc.value}, $\\sigma$={windowParam})'
        PlotVisualizer.drawWaveForm(
            windowed, sr, tab, title,
            'Amplitude', True, self.__saveWavCallback
        )

    def __plotFiltering(
            self, fileUrl, tab, filterType: FilterType,
            freq: float | None = None, freqFrom: float | None = None, freqTo: float | None = None,
            filterOrder: int | None = None
    ):
        signal, sr = WavReader.readWave(fileUrl)
        filtered = None
        title = ''
        match filterType.value:
            case FilterType.LOWPASS.value:
                title = f'Filtered wave form (type: {filterType.value}, order: {filterOrder}, {freq}Hz)'
                filtered = SoundAnalyzer.lowpass_filter(signal, freq, sr, filterOrder)
            case FilterType.HIGHPASS.value:
                title = f'Filtered wave form (type: {filterType.value}, order: {filterOrder}, {freq}Hz)'
                filtered = SoundAnalyzer.highpass_filter(signal, freq, sr, filterOrder)
            case FilterType.BANDPASS.value:
                title = f'Filtered wave form (type: {filterType.value}, order: {filterOrder}, {freqFrom}-{freqTo}Hz)'
                filtered = SoundAnalyzer.bandpass_filter(signal, [freqFrom, freqTo], sr, filterOrder)

        signalId = str(uuid4().hex)
        tab.setProperty('signalId', signalId)
        signalData = SignalData(filtered, sr, signalId)
        self.__soundAnalyzer.addSignal(signalData)
        PlotVisualizer.drawWaveForm(
            filtered, sr, tab, title,
            'Amplitude', True, self.__saveWavCallback
        )

    def __plotFourierTransform(self, fileUrl, tab, halfSpec: bool = False, posAmp: bool = False):
        signal, sr = WavReader.readWave(fileUrl)
        xf, yf = SoundAnalyzer.fourierTransform(
            signal=signal, sampleRate=sr, N=len(signal), halfSpec=halfSpec, posAmp=posAmp
        )
        PlotVisualizer.drawFourierTransform(xf, yf, tab=tab)

    def __plotSpectrogram(self, fileUrl, tab, colorBarLabel: str, toDecibels: bool = False, view3d: bool = False):
        signal, sr = WavReader.readWave(fileUrl)
        if view3d:
            freqBins, timestamps, spec = SoundAnalyzer.spectrogram3d(signal=signal, sampleRate=sr,
                                                                     convertToDb=toDecibels)
            PlotVisualizer.drawSpectrogram3d(freqBins, timestamps, spec, tab, colorBarLabel)
        else:
            spec = SoundAnalyzer.spectrogram(signal=signal, convertToDb=toDecibels)
            PlotVisualizer.drawSpectrogram(spec, sampleRate=sr, tab=tab, colorBarLabel=colorBarLabel)

    def __plotMelSpectrogram(self, fileUrl, tab, colorBarLabel: str, toDecibels: bool = False):
        signal, sr = WavReader.readWave(fileUrl)
        melSpec = SoundAnalyzer.melSpectrogram(signal=signal, sampleRate=sr, convertToDb=toDecibels)
        PlotVisualizer.drawMelSpectrogram(melSpec, sampleRate=sr, tab=tab, colorBarLabel=colorBarLabel)

    def __plotChromagram(self, fileUrl, tab):
        signal, sr = WavReader.readWave(fileUrl)
        chroma = SoundAnalyzer.chromagram(signal=signal, sampleRate=sr)
        PlotVisualizer.drawChromagram(chroma, tab)

    def __addSignalBtnHandler(self):
        self.childConfigWindow = AddSignalConfigWindow(
            addSignalConfigWindowUI.Ui_addSignalConfigWindow(),
            callbackDoneFunc=self.__addSignalConfigWindowCallback
        )
        self.childConfigWindow.show()

    def __fourierTransformBtnHandler(self):
        self.childConfigWindow = FourierTransformConfigWindow(
            fourierTransformConfigWindowUI.Ui_fourierTransformConfigWindow(),
            callbackDoneFunc=self.__fourierTransformConfigWindowCallback
        )
        self.childConfigWindow.show()

    def __windowingBtnHandler(self):
        self.childConfigWindow = WindowingConfigWindow(
            windowingConfigWindowUI.Ui_windowingConfigWindow(),
            callbackDoneFunc=self.__windowingWindowCallback
        )
        self.childConfigWindow.show()

    def __filtersBtnHandler(self):
        self.childConfigWindow = FiltersConfigWindow(
            filtersConfigWindowUI.Ui_filtersConfigWindow(),
            callbackDoneFunc=self.__filteringWindowCallback
        )
        self.childConfigWindow.show()

    def __spectrogramBtnHandler(self):
        self.childConfigWindow = SpectrogramConfigWindow(
            spectrogramConfigWindowUI.Ui_spectrogramConfigWindow(),
            callbackDoneFunc=self.__spectrogramConfigWindowCallback
        )
        self.childConfigWindow.show()

    def __melSpectrogramBtnHandler(self):
        self.childConfigWindow = MelSpectrogramConfigWindow(
            melSpectrogramConfigWindowUI.Ui_melSpectrogramConfigWindow(),
            callbackDoneFunc=self.__melSpectrogramConfigWindowCallback
        )
        self.childConfigWindow.show()

    def __chromagramBtnHandler(self):
        self.childConfigWindow = ChromagramConfigWindow(
            chromagramConfigWindowUI.Ui_chromagramConfigWindow(),
            callbackDoneFunc=self.__chromagramConfigWindowCallback
        )
        self.childConfigWindow.show()

    def __addSignalConfigWindowCallback(self, configData):
        try:
            fUrl = configData.getFileUrl()
            if len(fUrl) != 0:
                fName = configData.getFileName()
                ampNorm = configData.getNormalizeAmplitude()
                tab = self.__addPlotTab(fName)
                ylabel = 'Normalized amplitude' if ampNorm else 'Amplitude'
                self.__plotSignalWaveForm(fUrl, ampNorm, tab, ylabel, saveWav=False)
        except:
            self.__openErrorWindow()

    def __fourierTransformConfigWindowCallback(self, configData):
        try:
            fUrl = configData.getFileUrl()
            if len(fUrl) != 0:
                fName = configData.getFileName()
                tab = self.__addPlotTab(fName)
                halfSpec = configData.getHalfSpectrum()
                posAmp = configData.getPositiveSpectrum()
                self.__plotFourierTransform(fUrl, tab, halfSpec, posAmp)
        except:
            self.__openErrorWindow()

    def __chromagramConfigWindowCallback(self, configData):
        try:
            fUrl = configData.getFileUrl()
            if len(fUrl) != 0:
                fName = configData.getFileName()
                tab = self.__addPlotTab(fName)
                self.__plotChromagram(fUrl, tab)
        except:
            self.__openErrorWindow()

    def __windowingWindowCallback(self, configData):
        try:
            windowFunc = configData.getWindowFunc()
            windowParam = configData.getWindowParam()
            if windowFunc is not None:
                if (
                        windowFunc == WindowFunctions.KAISER or windowFunc == WindowFunctions.GAUSSIAN) and windowParam is None:
                    return

                fUrl = configData.getFileUrl()
                if len(fUrl) != 0:
                    fName = configData.getFileName()
                    tab = self.__addPlotTab(fName)
                    self.__plotWindowing(fUrl, tab, windowFunc, windowParam)
        except:
            self.__openErrorWindow()

    def __filteringWindowCallback(self, configData):
        try:
            filterType = configData.getFilterType()
            if filterType is not None:
                freq = configData.getFreq()
                freqTo = configData.getFreqTo()
                freqFrom = configData.getFreqFrom()
                filterOrder = configData.getFilterOrder()
                if (filterType == FilterType.LOWPASS or filterType == FilterType.HIGHPASS) and freq is None:
                    return
                if filterType == FilterType.BANDPASS and (freqTo is None or freqFrom is None):
                    return

                fUrl = configData.getFileUrl()
                if len(fUrl) != 0:
                    fName = configData.getFileName()
                    tab = self.__addPlotTab(fName)
                    self.__plotFiltering(fUrl, tab, filterType, freq, freqFrom, freqTo, filterOrder)
        except:
            self.__openErrorWindow()

    def __spectrogramConfigWindowCallback(self, configData):
        try:
            fUrl = configData.getFileUrl()
            if len(fUrl) != 0:
                fName = configData.getFileName()
                tab = self.__addPlotTab(fName)
                toDecibels = configData.getConvertToDecibels()
                colorBarLabel = 'Decibels' if toDecibels else 'Amplitude'
                view3d = configData.getView3d()
                self.__plotSpectrogram(fUrl, tab, colorBarLabel=colorBarLabel, toDecibels=toDecibels, view3d=view3d)
        except:
            self.__openErrorWindow()

    def __melSpectrogramConfigWindowCallback(self, configData):
        try:
            fUrl = configData.getFileUrl()
            if len(fUrl) != 0:
                fName = configData.getFileName()
                tab = self.__addPlotTab(fName)
                toDecibels = configData.getConvertToDecibels()
                colorBarLabel = 'Decibels' if toDecibels else 'Amplitude'
                self.__plotMelSpectrogram(fUrl, tab, colorBarLabel=colorBarLabel, toDecibels=toDecibels)
        except:
            self.__openErrorWindow()

    def __saveWavCallback(self, tab):
        try:
            signalData = self.__soundAnalyzer.getSignalDataById(tab.property('signalId'))
            file = QFileDialog.getSaveFileName()
            if len(file[0]) != 0:
                WavWriter.write(signalData.getData(), signalData.getSr(), file[0] + '.wav')
        except:
            self.__openErrorWindow()

    def __openErrorWindow(self):
        self.childConfigWindow = ErrorWindow(errorWindowUI.Ui_errorWindow())
        self.childConfigWindow.show()
