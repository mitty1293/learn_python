from abc import ABC, abstractmethod


class MediatorInterfaceB(ABC):
    @abstractmethod
    def notify_task_completion(self):
        pass


class ObjectB:
    def __init__(self, mediator):
        self.mediator = mediator

    def do_task(self):
        self.mediator.notify_task_completion()
