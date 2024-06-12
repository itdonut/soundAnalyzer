from GeneralConfigWindowData import GeneralConfigWindowData
from enums.WindowFunctions import WindowFunctions


class WindowingConfigWindowData(GeneralConfigWindowData):
    def __init__(self):
        super().__init__()
        self.__windowParam: float | None = None
        self.__windowFunc: WindowFunctions | None = None

    def setWindowFunc(self, val: WindowFunctions | None):
        self.__windowFunc = val

    def getWindowFunc(self):
        return self.__windowFunc

    def setWindowParam(self, val: float | None):
        self.__windowParam = val

    def getWindowParam(self):
        return self.__windowParam
