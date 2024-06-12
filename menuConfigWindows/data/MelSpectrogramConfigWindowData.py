from GeneralConfigWindowData import GeneralConfigWindowData


class MelSpectrogramConfigWindowData(GeneralConfigWindowData):
    def __init__(self):
        super().__init__()
        self.__convertToDecibels: bool = False

    def setConvertToDecibels(self, val: bool):
        self.__convertToDecibels = val

    def getConvertToDecibels(self):
        return self.__convertToDecibels
