from abc import ABC, abstractmethod


class Tyre(ABC):
    @abstractmethod
    def needs_service(self):
        pass
