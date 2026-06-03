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
            raise ValueError("Improper numeric data")
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    try:
        np.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        print(f"Numeric value {i}: {np.output()[1]}")
    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    print(f"Text value 0: {tp.output()[1]}")
    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    print("Processing data: [{'log_level': 'NOTICE', 'log_message':"
          " 'Connection to server'}, {'log_level': 'ERROR',"
          " 'log_message': 'Unauthorized access!!'}]")
    lp.ingest([
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ])
    print("Extracting 2 values...")
    print(f"Log entry 0: {lp.output()[1]}")
    print(f"Log entry 1: {lp.output()[1]}")


if __name__ == "__main__":
    main()
