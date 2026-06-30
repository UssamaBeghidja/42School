#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self.rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) and not isinstance(x, bool)
                       for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append((self.rank_counter, str(item)))
                self.rank_counter += 1
        else:
            self._data.append((self.rank_counter, str(data)))
            self.rank_counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str)
                       for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append((self.rank_counter, str(item)))
                self.rank_counter += 1
        else:
            self._data.append((self.rank_counter, str(data)))
            self.rank_counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and not isinstance(data, bool):
            if "log_level" in data and "log_message" in data:
                return True
        if isinstance(data, list):
            return all(isinstance(x, dict) and not isinstance(x, bool)
                       and "log_level" in x and "log_message" in x
                       for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper dict data")
        if isinstance(data, list):
            for item in data:
                log = f"{item['log_level']}: {item['log_message']}"
                self._data.append((self.rank_counter, log))
                self.rank_counter += 1
        else:
            log = f"{data['log_level']}: {data['log_message']}"
            self._data.append((self.rank_counter, log))
            self.rank_counter += 1


class DataStream:
    def __init__(self) -> None:
        self._processor: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self._processor:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                msg = f"DataStream error - Can't process element: {item}"
                print(msg)

    def print_processors_stats(self) -> None:
        if not self._processor:
            print("No processor found, no data")
            return
        for proc in self._processor:
            name = proc.__class__.__name__.replace('Processor', ' Processor')
            remaining = len(proc._data)
            print(f"{name}: total {proc.rank_counter} items processed,"
                  f" remaining {remaining} on processor")


def main() -> None:
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five']
    ]
    ds = DataStream()
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    ds.register_processor(np)
    print("Send first batch of data on stream: [...]")
    ds.process_stream(batch)
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Registering other data processors")
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    ds.process_stream(batch)
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Consume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    lp.output()
    print("== DataStream statistics ==")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
