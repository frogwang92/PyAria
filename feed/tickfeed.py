import pandas as pd


class TickFeed(object):
    def __init__(self, filename):
        self.__file = filename

    def prepare(self):
        self.__df = pd.DataFrame.from_csv(self.__file)
        self.__current = 0

    def get(self):
        val = self.__df.iloc[-self.__current]
        self.__current += 1
        return val

    def valid(self):
        return 0 <= self.__current <= self.__df.__len__()
