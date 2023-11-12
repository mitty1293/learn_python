from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def invoke(self) -> None:
        pass
