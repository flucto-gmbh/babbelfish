from heisskleber import Source

from .service import Service
from .config import ConsumerConf


class Consumer(Service):
    config: ConsumerConf
    source: Source

    def __init__(self, config: ConsumerConf) -> None:
        self.config = config
