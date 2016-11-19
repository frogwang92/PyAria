import subject


class Engine(subject.Subject):
    def __init__(self):
        self.__active = False
        self.ev_start = subject.Event()
        self.ev_pause = subject.Event()
        self.ev_end   = subject.Event()

    def run(self):
        pass

    def initialize(self, feed, algo):
        self.__datafeed = feed
        self.__algorithm = algo
        pass