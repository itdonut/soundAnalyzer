from GeneralConfigWindowData import GeneralConfigWindowData
from enums.FilterType import FilterType


class FilteringConfigWindowData(GeneralConfigWindowData):
    def __init__(self):
        super().__init__()
        self.__filterType: FilterType | None = None
        self.__filterOrder: int | None = None
        self.__freqFrom: float | None = None
        self.__freqTo: float | None = None
        self.__freq: float | None = None

    def setFilterType(self, val: FilterType | None):
        self.__filterType = val

    def setFilterOrder(self, val: int | None):
        self.__filterOrder = val

    def setFreqFrom(self, val: float | None):
        self.__freqFrom = val

    def setFreqTo(self, val: float | None):
        self.__freqTo = val

    def setFreq(self, val: float | None):
        self.__freq = val

    def getFilterType(self):
        return self.__filterType

    def getFilterOrder(self):
        return self.__filterOrder

    def getFreqFrom(self):
        return self.__freqFrom

    def getFreqTo(self):
        return self.__freqTo

    def getFreq(self):
        return self.__freq
