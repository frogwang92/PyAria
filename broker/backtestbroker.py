class BackTestBroker(object):
    def __init__(self, portfolio):
        self.__portfolio = portfolio

    def buy(self, position, percentage):
        pass

    def sell(self, percentage):
        pass


class Portfolio(object):
    """support one hold only"""
    def __init__(self, money = 1000000, holdshare = 0, position = 0):
        """position = 0 means there is no holdshare in the portfolio"""
        self.money = money
        self.position = position
        self.holdshare = holdshare

    def portfolio_change(self, money, holdshare, position):
        self.money += money
        self.holdshare += holdshare
        self.position = position
