

class OHLCV:
    __open = 0
    __high = 0
    __low  = 0
    __close = 0
    __volume = 0

    def __init__(self, open, high, low, close, volume):
        self.__open = open
        self.__high = high
        self.__low = low
        self.__close = close
        self.__volume = volume

    def get_open(self):
        self.__open

    def get_high(self):
        self.__high

    def get_low(self):
        self.__low

    def get_close(self):
        self.__close

    def get_volume(self):
        self.__volume