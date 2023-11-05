# クラスによる振る舞い

from abc import ABC, abstractmethod


class RunnableInterface(ABC):
    @abstractmethod
    def run(self):
        pass


foo = "Foo"


class RunnableObject(RunnableInterface):
    def __init__(self, value):
        self.value = value

    def run(self):
        print(self.value)


runnableObject = RunnableObject(foo)
runnableObject.run()
