from abc import ABC, abstractmethod


class Aggregate(ABC):
    @abstractmethod
    def iterator(self) -> None:
        raise NotImplementedError
