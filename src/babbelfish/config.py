from heisskleber.config import Config as HKConf
from typing import FileIO

from dataclasses import dataclass


@dataclass
class ServiceConf:
    name: str

    @classmethod
    def from_file(cls, file: FileIO) -> "ServiceConf":
        pass

    @classmethod
    def from_dict(cls, config_dict: dict[str, any]) -> "ServiceConf":
        pass


@dataclass
class ConsumerConf(ServiceConf):
    SourceConf: HKConf


@dataclass
class ProducerConf(ServiceConf):
    SinkConf: HKConf


@dataclass
class ConsumerProducerConf(ServiceConf):
    SourceConf: HKConf
    SinkConf: HKConf
