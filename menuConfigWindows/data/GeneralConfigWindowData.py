class GeneralConfigWindowData:
    def __init__(self):
        self.__fileUrl: str = ''
        self.__fileName: str = ''

    def setFileUrl(self, url: str):
        self.__fileUrl = url

    def setFileName(self, name: str):
        self.__fileName = name

    def getFileUrl(self):
        return self.__fileUrl

    def getFileName(self):
        return self.__fileName
