class Subject(object):

    def __init__(self):
        self.__subscribers = {}

    def __register_event(self, ev):
        if ev not in self.__subscribers:
            self.__subscribers[ev] = list()

    def subscribe(self, ev, func):
        self.__register_event(ev)
        self.__subscribers[ev].append(func)

    def unsubscribe(self, ev, func):
        if ev in self.__subscribers:
            if func in self.__subscribers[ev]:
                self.__subscribers[ev].remove(func)

    def update(self, ev, *args):
        Dispatcher.update(self.__subscribers, ev, *args)


class Event(object):
    pass


class Dispatcher(object):

    @staticmethod
    def update(subscribers, ev, *args):
        if ev in subscribers:
            for obs in subscribers[ev]:
                obs(args)
