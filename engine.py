import subject
import feed.tickfeed as fd
import algorithm.backtest_buy_and_hold as algo
import broker.backtestbroker as broker


class Engine(subject.Subject):
    """Engine class is the place to connect everybody together"""
    def __init__(self):
        super(Engine, self).__init__()
        self.ev_start = subject.Event()
        self.ev_pause = subject.Event()
        self.ev_end = subject.Event()
        self.ev_data = subject.Event()
        self.__feed = fd.TickFeed("test.csv")
        self.__algorithm = algo.BackTestBuyAndHold()
        self.__broker = broker.BackTestBroker()
        self.__subscribe_to_update()

    def run(self):
        self.__feed.prepare()
        self.__algorithm.prepare()
        self.update(self.ev_start, [])
        while self.__feed.valid():
            self.__get_next_data()
        self.update(self.ev_end, [])

    def __get_next_data(self):
        data = self.__feed.get()
        self.update(self.ev_data, [data])

    def __subscribe_to_update(self):
        self.subscribe(self.ev_start, self.__algorithm.start)
        self.subscribe(self.ev_data, self.__algorithm.on_data)
