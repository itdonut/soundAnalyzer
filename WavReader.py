import librosa
import numpy as np
from scipy.io import wavfile


class WavReader:
    def __init__(self):
        pass

    @staticmethod
    def readWave(url: str, norm: bool = True):
        if norm:
            signal, sr = librosa.load(url)
            return signal, sr

        sr, wav = wavfile.read(url)  # might be warning because can't read some metadata

        if len(wav.shape) > 1:  # if stereo
            wav = np.mean(wav, axis=1)  # get only one chanel

        signal = np.asarray(wav, dtype=np.float32)  # need to convert after wavfile.read()
        return signal, sr
