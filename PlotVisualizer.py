import librosa.display
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize, Qt
import matplotlib.pyplot as plt


class PlotVisualizer:
    def __init__(self):
        pass

    @staticmethod
    def drawWaveForm(signal, sampleRate, tab, title: str, ylabel: str, saveWav: bool = False, saveWavCallback=None):
        fig, ax = plt.subplots()
        librosa.display.waveshow(y=signal, sr=sampleRate, ax=ax)
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel(ylabel)

        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, tab.parent().parent())
        if saveWav:
            btn = QPushButton('Save as WAV')
            btn.setFixedSize(QSize(130, 30))
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(u"background-color: rgb(0, 96, 206);\n"
                              "color: white;\n"
                              "font-weight: bold;\n"
                              "border: none;\n"
                              "font-size: 14px;")
            btn.clicked.connect(lambda: saveWavCallback(tab))
            toolbar.addWidget(btn)

        tab.layout().addWidget(canvas)
        tab.layout().addWidget(toolbar)

    @staticmethod
    def drawFourierTransform(xf, yf, tab):
        fig, ax = plt.subplots()
        plt.plot(xf, yf)
        plt.title('Fourier transform')
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')

        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, tab.parent().parent())

        tab.layout().addWidget(canvas)
        tab.layout().addWidget(toolbar)

    @staticmethod
    def drawSpectrogram(spec, sampleRate, tab, colorBarLabel: str):
        fig, ax = plt.subplots()
        librosa.display.specshow(spec, sr=sampleRate, x_axis='time', y_axis='hz', hop_length=512)
        plt.title(f'Spectrogram ({colorBarLabel})')
        plt.xlabel('Time (s)')
        plt.colorbar(label=colorBarLabel)

        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, tab.parent().parent())

        tab.layout().addWidget(canvas)
        tab.layout().addWidget(toolbar)

    @staticmethod
    def drawSpectrogram3d(freqBins, timestamps, spec, tab, colorBarLabel: str):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        surf = ax.plot_surface(freqBins[:, None], timestamps[None, :], spec, cmap='magma')  # cmap=cm.coolwarm
        plt.title(f'Spectrogram 3d ({colorBarLabel})')
        plt.xlabel('Hz')
        plt.ylabel('Time (s)')
        fig.colorbar(surf, label=colorBarLabel)

        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, tab.parent().parent())

        tab.layout().addWidget(canvas)
        tab.layout().addWidget(toolbar)

    @staticmethod
    def drawChromagram(chroma, tab):
        fig, ax = plt.subplots()
        s = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
        plt.title('Chromagram')
        plt.xlabel('Time (s)')
        fig.colorbar(s, label='Intensity')

        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, tab.parent().parent())

        tab.layout().addWidget(canvas)
        tab.layout().addWidget(toolbar)

    @staticmethod
    def drawMelSpectrogram(melSpectrogram, sampleRate, tab, colorBarLabel: str):
        fig, ax = plt.subplots()
        librosa.display.specshow(
            melSpectrogram,
            sr=sampleRate,
            x_axis='time',
            y_axis='mel',
            hop_length=512,
            cmap='magma'
        )
        plt.colorbar(label=colorBarLabel)
        plt.title(f'Mel-Spectrogram ({colorBarLabel})')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency')

        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(canvas, tab.parent().parent())

        tab.layout().addWidget(canvas)
        tab.layout().addWidget(toolbar)
