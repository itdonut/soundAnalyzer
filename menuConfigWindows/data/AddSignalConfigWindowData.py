from GeneralConfigWindowData import GeneralConfigWindowData


class AddSignalConfigWindowData(GeneralConfigWindowData):
    def __init__(self):
        super().__init__()
        self.__normalizeAmplitude: bool = False

    def setNormalizeAmplitude(self, val: bool):
        self.__normalizeAmplitude = val

    def getNormalizeAmplitude(self):
        return self.__normalizeAmplitude
