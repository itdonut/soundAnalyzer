import numpy as np
import librosa
from scipy.signal import butter, sosfiltfilt, spectrogram as scipyspectrogram
from scipy.signal.windows import *
from scipy.fft import fft, fftfreq

from enums.WindowFunctions import WindowFunctions


class SoundAnalyzer:
    def __init__(self):
        self.__signalsData = list()

    def addSignal(self, data):
        self.__signalsData.append(data)

    def deleteSignal(self, signalId):
        for idx, data in enumerate(self.__signalsData):
            if data.getId() == signalId:
                self.__signalsData.pop(idx)

    def getSignalDataById(self, signalId):
        for data in self.__signalsData:
            if data.getId() == signalId:
                return data

    @staticmethod
    def chromagram(signal, sampleRate):
        S = np.abs(librosa.stft(y=signal, n_fft=2048)) ** 2
        chroma = librosa.feature.chroma_stft(S=S, sr=sampleRate)
        return chroma

    @staticmethod
    def windowing(signal, windowFunc: WindowFunctions, windowParam: float):
        match windowFunc:
            case WindowFunctions.KAISER:
                return signal * kaiser(len(signal), windowParam, sym=False)
            case WindowFunctions.GAUSSIAN:
                return signal * gaussian(len(signal), windowParam, sym=False)
            case WindowFunctions.BARLETT:
                return signal * bartlett(len(signal), sym=False)
            case WindowFunctions.HANN:
                return signal * hann(len(signal), sym=False)
            case WindowFunctions.TRIANGULAR:
                return signal * triang(len(signal), sym=False)
            case WindowFunctions.HAMMING:
                return signal * hamming(len(signal), sym=False)
            case WindowFunctions.BARLETT_HANN:
                return signal * barthann(len(signal), sym=False)
            case WindowFunctions.LANCZOS:
                return signal * lanczos(len(signal), sym=False)
            case WindowFunctions.BOHMAN:
                return signal * bohman(len(signal), sym=False)
            case WindowFunctions.BLACKMANN:
                return signal * blackman(len(signal), sym=False)

    @staticmethod
    def fourierTransform(signal, sampleRate, N, halfSpec: bool = False, posAmp: bool = False):
        yf = fft(signal)
        xf = fftfreq(N, 1 / sampleRate)

        if halfSpec and posAmp:
            xf = xf[:N // 2]
            yf = np.abs(yf[:N // 2])
            return xf, yf
        if halfSpec and not posAmp:
            xf = xf[:N // 2]
            yf = yf[:N // 2]
            return xf, yf
        if not halfSpec and posAmp:
            yf = np.abs(yf)
            return xf, yf

        return xf, yf

    @staticmethod
    def spectrogram(signal, convertToDb: bool = False):
        audio_stft = librosa.core.stft(y=signal, hop_length=512, n_fft=2048)
        spec = np.abs(audio_stft)
        if convertToDb:
            spec = librosa.amplitude_to_db(spec)

        return spec

    @staticmethod
    def spectrogram3d(signal, sampleRate, convertToDb: bool = False):
        freqBins, timestamps, spec = scipyspectrogram(signal, sampleRate)
        if convertToDb:
            spec = 10.0 * np.log10(spec)  # might be warning because divide by zero

        return freqBins, timestamps, spec

    @staticmethod
    def melSpectrogram(signal, sampleRate, convertToDb: bool = False):
        mel_spectrogram = librosa.feature.melspectrogram(y=signal, sr=sampleRate, hop_length=512, n_fft=2048)
        mel_spectrogram = np.abs(mel_spectrogram)
        if convertToDb:
            mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

        return mel_spectrogram

    @staticmethod
    def lowpass_filter(data, cutoff, sr, order):
        sos = butter(order, cutoff, 'lowpass', fs=sr, output='sos')
        filtered_data = sosfiltfilt(sos, data)
        return filtered_data

    @staticmethod
    def highpass_filter(data, cutoff, sr, order):
        sos = butter(order, cutoff, 'highpass', fs=sr, output='sos')
        filtered_data = sosfiltfilt(sos, data)
        return filtered_data

    @staticmethod
    def bandpass_filter(data, cutoff: list[float], sr, order):
        sos = butter(order, cutoff, 'bandpass', fs=sr, output='sos')
        filtered_data = sosfiltfilt(sos, data)
        return filtered_data
