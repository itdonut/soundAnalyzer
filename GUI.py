from MainWindow import MainWindow


class GUI:
    def __init__(self):
        self.__mainWindow = MainWindow()

    def init(self):
        self.__initMainWindow()

    def __initMainWindow(self):
        self.__mainWindow.showMaximized()
