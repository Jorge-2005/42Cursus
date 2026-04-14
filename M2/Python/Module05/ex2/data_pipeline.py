from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


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


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        result: list[tuple[int, str]] = []

        while len(result) < nb:
            empty: bool = False
            for p in self._processor:
                try:
                    if len(result) < nb:
                        result.append(p.output())
                        empty = True
                except Exception:
                    continue
            if not empty:
                break
        plugin.process_output(result)
