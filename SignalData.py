class SignalData:
    def __init__(self, data, sr, uid):
        self.__data = data
        self.__sr = sr
        self.__id = uid

    def getData(self):
        return self.__data

    def getSr(self):
        return self.__sr

    def getId(self):
        return self.__id
