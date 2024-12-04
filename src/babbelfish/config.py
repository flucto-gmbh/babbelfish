from heisskleber.config import Config as HKConf

from dataclasses import dataclass


@dataclass
class ServiceConf:
    name: str


@dataclass
class ConsumerConf(ServiceConf):
    SourceConf: HKConf


@dataclass
class ProducerConf(ServiceConf):
    SinkConf: HKConf


@dataclass
class ProducerConsumerConf(ServiceConf):
    SourceConf: HKConf
    SinkConf: HKConf
