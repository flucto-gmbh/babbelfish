from abc import ABC, abstractmethod
import asyncio
from typing import Any, FileIO
import logging

# TODO: implement configuration class -> checkout heisskleber config

from .config import ServiceConf


class Service(ABC):
    _running: bool = False
    config: ServiceConf
    logger: logging.Logger

    def __init__(self, config: ServiceConf) -> None:
        self.config = config
        self.logger = logging.getLogger(self.config.name)

    @classmethod
    def from_config_file(cls, config_file: FileIO) -> "Service":
        """Instatiate a Service object with a configuration file."""
        return cls(ServiceConf.from_file(config_file))

    @classmethod
    def from_dict(cls, config_dict: dict[str, Any]) -> "Service":
        """Instatiate a Service with a configuration based on a dictionary."""
        return cls(ServiceConf.from_dict(config_dict))

    @abstractmethod
    def _start_hook(self) -> None:
        """Method to be implemented in derived classes, executed upon."""

    @abstractmethod
    def _stop_hook(self) -> None:
        """Method to be implemented in derived classes, executed upon exit."""

    @abstractmethod
    def _exit_hook(self) -> None:
        """Method to be implemented in derived classes, executed upon SIGINT."""

    @abstractmethod
    def _exception_hook(self) -> None:
        """Method to be implemented in derived classes, executed upon an exception."""

    @abstractmethod
    def _runner(self) -> None:
        """Core logic method, to be implemented in derived class."""
        pass

    def start(self) -> None:
        """Start the service."""
        self.logger.info("Starting {} service".format(self.config.name))
        try:
            while True:
                self._runner()
                self.logger.info("Restarting {} service".format(self.config.name))
        except KeyboardInterrupt:
            self._exit_hook()
            self.logger.info("Exiting {} service".format(self.config.name))

    def stop(self) -> None:
        """Stop the service."""
        self._stop_hook()
        self.logger.info("Stopping {} service".format(self.config.name))
