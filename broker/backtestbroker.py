class BackTestBroker(object):
    def __init__(self, portfolio):
        self.__portfolio = portfolio

    def buy(self, position, percentage):
        pass

    def sell(self):
        pass


class Portfolio(object):
    def __init__(self, money, position):
        self.__money = money
        self.__position = position
