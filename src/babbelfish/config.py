from dataclasses import dataclass, fields
from pathlib import Path
from typing import Any, TypeVar

import yaml
from heisskleber.core import BaseConf as HKConf

T = TypeVar("T", bound="ServiceConf")


@dataclass
class ServiceConf:
    name: str

    @classmethod
    def from_file(cls: type[T], file: str | Path) -> T:
        path = Path(file)
        with path.open() as f:
            return cls.from_dict(dict(yaml.safe_load(f)))

    @classmethod
    def from_dict(cls: type[T], config_dict: dict[str, Any]) -> T:
        valid_fields = {f.name for f in fields(cls)}
        filtered_dict = {k: v for k, v in config_dict.items() if k in valid_fields}
        return cls(**filtered_dict)


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
