from heisskleber import Source, Sink

from .service import Service
from .config import ConsumerProducerConf


class ConsumerProducer(Service):
    config: ConsumerProducerConf
    source: Source
    sink: Sink

    def __init__(self, config: ConsumerProducerConf) -> None:
        self.config = config
