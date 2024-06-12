from GeneralConfigWindowData import GeneralConfigWindowData


class FourierTransformConfigWindowData(GeneralConfigWindowData):
    def __init__(self):
        super().__init__()
        self.__halfSpectrum: bool = False
        self.__positiveSpectrum: bool = False

    def setHalfSpectrum(self, val: bool):
        self.__halfSpectrum = val

    def setPositiveSpectrum(self, val: bool):
        self.__positiveSpectrum = val

    def getHalfSpectrum(self):
        return self.__halfSpectrum

    def getPositiveSpectrum(self):
        return self.__positiveSpectrum
