#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = ", ".join(f'"item_{rank}": "{value}"' for rank, value in data)
        print("{" + pairs + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processor:
            tuples = []
            for _ in range(nb):
                if proc._data:
                    tuples.append(proc.output())
            plugin.process_output(tuples)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    csv_plugin = CSVExportPlugin()
    json_plugin = JSONExportPlugin()
    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]  # first batch
    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'},
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]  # second batch

    ds = DataStream()
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Registering Processors")
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)

    print("Send first batch...")
    ds.process_stream(batch1)
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, csv_plugin)
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Send another batch of data: ...")
    ds.process_stream(batch2)
    print("== DataStream statistics ==")
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, json_plugin)
    print("== DataStream statistics ==")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
