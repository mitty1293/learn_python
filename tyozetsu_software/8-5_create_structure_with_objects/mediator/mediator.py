from object_a import MediatorInterfaceA, ObjectA
from object_b import MediatorInterfaceB, ObjectB


class Mediator(MediatorInterfaceA, MediatorInterfaceB):
    def __init__(self, a: ObjectA, b: ObjectB):
        self.a = a
        self.b = b

    def notify_activity_done(self):
        self.b.do_task()

    def notify_task_completion(self):
        self.a.finish_the_work()
