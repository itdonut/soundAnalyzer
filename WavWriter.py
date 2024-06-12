from scipy.io import wavfile


class WavWriter:
    @staticmethod
    def write(data, sr, path):
        wavfile.write(path, sr, data)
