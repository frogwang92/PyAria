import subject


class Observer(object):
    def __init__(self):
        pass

    def notify(self, args):
        print("obs notified, args: {}".format(args))


class Engine(subject.Subject):

    def __init__(self):
        super(Engine, self).__init__()
        self.test_event = subject.Event()

    def update_event1(self):
        print("***event 1 updated with no argument***")
        self.update(self.test_event)

    def update_event1_with_args(self):
        print("***event 1 updated with args {}***".format(1, 2, 3))
        self.update(self.test_event, 1, 2, 3)

engine = Engine()
ob = Observer()

engine.subscribe(engine.test_event, ob.notify)
engine.subscribe(engine.test_event, lambda args: print("notified to a lambda with args {}".format(args)))
engine.update_event1()
engine.update_event1_with_args()

print("unsubscribe ob.notify from engine.test_event")
engine.unsubscribe(engine.test_event, ob.notify)
engine.update_event1()