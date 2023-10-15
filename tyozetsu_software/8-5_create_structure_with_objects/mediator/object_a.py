from abc import ABC, abstractmethod


class MediatorInterfaceA(ABC):
    @abstractmethod
    def notify_activity_done(self):
        pass


class ObjectA:
    def __init__(self, mediator):
        self.mediator = mediator

    def some_activity(self):
        self.mediator.notify_activity_done()

    def finish_the_work(self):
        pass
