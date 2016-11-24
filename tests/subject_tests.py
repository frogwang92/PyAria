import subject


class Observer(object):
    def __init__(self):
        pass

    def notify(self, args):
        print "notified"


class Observer2(object):
    def __init__(self):
        pass

    def notify(self, args):
        print "obs2 notified, args: %d" % (len(args))


class Engine(subject.Subject):

    def __init__(self):
        super(Engine, self).__init__()
        self.test_event = subject.Event()

    def update_event1(self):
        self.update(self.test_event, [])

    def update_event1_with_args(self):
        self.update(self.test_event, [1, 2, 3])

if __name__ == "__main__":
    engine = Engine()
    ob1 = Observer()
    ob2 = Observer2()

    engine.subscribe(engine.test_event, ob1.notify)
    engine.subscribe(engine.test_event, ob2.notify)
    engine.update_event1()
    engine.update_event1_with_args()

    engine.unsubscribe(engine.test_event, ob1.notify)
    engine.update_event1()
