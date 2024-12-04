from heisskleber import Sink

from .service import Service

from .config import ProducerConf


class Producer(Service):
    config: ProducerConf
    sink: Sink

    def __init__(self, config: ProducerConf) -> None:
        self.config = config


class CSVFileLogger(Producer):
    def __init__(self, config: ProducerConf) -> None:
        super().__init__(config)
        # create file handle logic

    def __call__(self, data: str) -> None:
        # write data to file
        pass
