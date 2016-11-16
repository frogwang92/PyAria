import datetime


class Tick:
    __time = datetime.datetime()

    def __init__(self, time):
        self.__time = time
