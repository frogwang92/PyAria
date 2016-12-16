import subject


class BackTestBroker(subject.Subject):
    """
    we currently do not consider liquidity, every transaction succeed.
    To keep it simple, broker responsible for trade money for share holds or trade holds for money
    """
    def __init__(self):
        super(BackTestBroker, self).__init__()
        self.ev_bought = subject.Event()
        self.ev_selled = subject.Event()

    def buy(self, price, money):
        """
        trade the requested money for some holds.
        :type price: float
        :type money: float
        """
        holds = money/price
        self.update(self.ev_bought, -money, holds)

    def sell(self, price, holds):
        """
        trade the holds for money
        :type price: float
        :type holds: float
        """
        money = price * holds
        self.update(self.ev_selled, money, -holds)


class Portfolio(object):
    """
    support one hold only currently
    seperate portfolio from broker because one portfolio may trade with multi broker in the future
    """
    def __init__(self, money=1000000, holds=0):
        self.money = money
        self.holds = holds

    def __portfolio_change(self, money, holds):
        self.money += money
        self.holds += holds

    def subscribe_to_broker(self, broker):
        broker.subscribe(broker.ev_bought, self.__notify)
        broker.subscribe(broker.ev_selled, self.__notify)

    def __notify(self, args):
        money = args[0]
        holds = args[1]
        self.__portfolio_change(money, holds)