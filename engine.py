import subject
import feed.tickfeed as fd
import algorithm.backtest_buy_and_hold as algo


class Engine(subject.Subject):
    def __init__(self):
        super(Engine, self).__init__()
        self.ev_start = subject.Event()
        self.ev_pause = subject.Event()
        self.ev_end = subject.Event()
        self.ev_data = subject.Event()
        self.__feed = fd.TickFeed("test.csv")
        self.__algorithm = algo.BackTestBuyAndHold()

    def run(self):
        self.__feed.prepare()
        self.update(self.ev_start, [])
        while self.__feed.valid():
            self.__get_next_data()

        self.update(self.ev_end, [])

    def __get_next_data(self):
        data = self.__feed.get()
        self.update(self.ev_data, [data])
        print data

