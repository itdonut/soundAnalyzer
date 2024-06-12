from GeneralConfigWindowData import GeneralConfigWindowData


class SpectrogramConfigWindowData(GeneralConfigWindowData):
    def __init__(self):
        super().__init__()
        self.__convertToDecibels: bool = False
        self.__view3d: bool = False

    def setConvertToDecibels(self, val: bool):
        self.__convertToDecibels = val

    def getConvertToDecibels(self):
        return self.__convertToDecibels

    def setView3d(self, val: bool):
        self.__view3d = val

    def getView3d(self):
        return self.__view3d
