from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._counter = 0
        self._total_processed = 0

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
                self._total_processed += 1
            elif isinstance(data, list):
                for i in data:
                    self._data.append((self._counter, str(i)))
                    self._counter += 1
                    self._total_processed += 1
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
                self._total_processed += 1
            elif isinstance(data, list):
                for i in data:
                    self._data.append((self._counter, i))
                    self._counter += 1
                    self._total_processed += 1
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
                self._total_processed += 1
            elif isinstance(data, list):
                for d in data:
                    self._data.append((self._counter, f"{d['log_level']}: "
                                       f"{d['log_message']}"))
                    self._counter += 1
                    self._total_processed += 1
        else:
            raise ValueError("Got exception: Improper Log data")


class DataStream():

    def __init__(self) -> None:
        self._processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for d in stream:
            val = False
            for p in self._processor:
                if p.validate(d):
                    p.ingest(d)
                    val = True
                    break
            if not val:
                print("DataStream error - Can't process element in"
                      f"stream: {d}")

    def print_processors_stats(self) -> None:
        if not self._processor:
            print("No processor found\n")
        else:
            for p in self._processor:
                print(f"{p.__class__.__name__}: total {p._total_processed}"
                      f" items processed, remaining {len(p._data)}"
                      " on processor")


if __name__ == "__main__":
    numericp = NumericProcessor()
    textp = TextProcessor()
    logp = LogProcessor()
    datas = DataStream()
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    datas.print_processors_stats()

    print("Registering Numeric Processor\n")
    datas.register_processor(numericp)

    print("Send first batch of data on stream: ['Hello world',"
          "[3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message':"
          "'Telnet access! Use ssh instead'}, {'log_level': 'INFO',"
          "'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]")
    datas.process_stream([
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! '
          'Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ])
    print("== DataStream statistics ==")
    datas.print_processors_stats()

    print("\nRegistering other data processors")
    datas.register_processor(textp)
    datas.register_processor(logp)
    datas.process_stream([
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh'
          'instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ])
    print("Send the same batch again")
    print("== DataStream statistics ==")
    datas.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    num: int = 0
    value: str = ""
    for i in range(3):
        num, value = numericp.output()
        print(f"Numeric value {num}: {value}")
    print("")
    for i in range(2):
        num, value = textp.output()
        print(f"Numeric value {num}: {value}")
    num, value = logp.output()

    print(f"\nNumeric value {num}: {value}\n")
    print("== DataStream statistics ==")
    datas.print_processors_stats()
