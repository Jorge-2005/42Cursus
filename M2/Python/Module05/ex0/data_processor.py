from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (0, "no data")


class NumericProcessor(DataProcessor):

    def __init__(self):
        self._data: list[str] = []
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            self._data.append(str(data))
        elif isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                for i in data:
                    self._data.append(str(i))
        else:
            raise ValueError("Got exception: Improper numeric data")

    def ingest(self, data: Any) -> None:
        if isinstance(data, (int, float)):
            self._data.append(str(data))
        elif isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                for i in data:
                    self._data.append(str(i))
        else:
            raise ValueError("Got exception: Improper numeric data")


class TextProcessor (DataProcessor):

    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: Any) -> None:
        pass


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: Any) -> None:
        pass


name = 2.5
if isinstance(name, (str, int)):
    print("hola")
