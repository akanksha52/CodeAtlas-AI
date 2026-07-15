from abc import ABC, abstractmethod

class CodeParser(ABC):
    @abstractmethod
    def parse(self, code: bytes):
        pass