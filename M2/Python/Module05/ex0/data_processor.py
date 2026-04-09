from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("No data available")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, (int, float)):
                self._data.append((self._counter, str(data)))
                self._counter += 1
            elif isinstance(data, list):
                for i in data:
                    self._data.append((self._counter, str(i)))
                    self._counter += 1
        else:
            raise ValueError("Got exception: Improper Numeric data")


class TextProcessor (DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self._data.append((self._counter, data))
                self._counter += 1
            elif isinstance(data, list):
                for i in data:
                    self._data.append((self._counter, i))
                    self._counter += 1
        else:
            raise ValueError("Got exception: Improper Text data")


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, cont in data.items():
                if not (isinstance(key, str) and isinstance(cont, str)):
                    return False
            return True
        elif isinstance(data, list):
            return all(self.validate(x) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, dict):
                self._data.append((self._counter, str(data)))
                self._counter += 1
            elif isinstance(data, list):
                for d in data:
                    self._data.append((self._counter, f"{d['log_level']}: "
                                       f"{d['log_message']}"))
                    self._counter += 1
        else:
            raise ValueError("Got exception: Improper Log data")


if __name__ == "__main__":
    numericp = NumericProcessor()
    textp = TextProcessor()
    logp = LogProcessor()
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numericp.validate(42)}")
    print(f"Trying to validate input 'Hello': {numericp.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numericp.ingest('foo')
    except ValueError as e:
        print(e)
    print("Processing data: [1, 2, 3, 4, 5]")
    numericp.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    num: int = 0
    value: str = ""
    for i in range(3):
        num, value = numericp.output()
        print(f"Numeric value {num}: {value}")

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {textp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    textp.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    num, value = textp.output()
    print(f"Text value {num}: {value}\n")

    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {logp.validate('Hello')}")
    print("Processing data: [{'log_level': 'NOTICE', 'log_message':"
          "'Connection to server'}, {'log_level': 'ERROR', 'log_message':"
          "'Unauthorized access!!'}]")
    logp.ingest([{'log_level': 'NOTICE', 'log_message':
                'Connection to server'}, {'log_level': 'ERROR', 'log_message':
                 'Unauthorized access!!'}])
    print("Extracting 2 values...")
    for i in range(2):
        num, value = logp.output()
        print(f"Log entry {num}: {value}")
