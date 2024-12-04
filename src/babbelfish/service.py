from abc import ABC, abstractmethod
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
        """
        Instatiate a Service object with a configuration file
        """
        # TODO: implement configuration class parsing snafu
        return cls(config_file)

    @classmethod
    def from_dict(cls, config: dict[str, Any]) -> "Service":
        """
        Instatiate a Service with a configuration based on a dictionary
        """
        # TODO: implement from dict parsing logic
        return cls(config)

    @abstractmethod
    def _start_hook(self) -> None:
        """
        method to be implemented in derived classes, executed upon
        """

    @abstractmethod
    def _stop_hook(self) -> None:
        """
        method to be implemented in derived classes, executed upon exit
        """

    @abstractmethod
    def _exit_hook(self) -> None:
        """
        method to be implemented in derived classes, executed upon SIGINT
        """

    @abstractmethod
    def _exception_hook(self) -> None:
        """
        method to be implemented in derived classes, executed upon an exception
        """

    @abstractmethod
    def _runner(self) -> None:
        """
        core logic
        """
        pass

    def start(self) -> None:
        """
        Start the service
        """
        try:
            while True:
                self._runner()
        except KeyboardInterrupt:
            self._exit_hook()
            self.logger.info("Exiting")

    def stop(self) -> None:
        """
        Stop the service
        """
        self._stop_hook()
        self.logger.info("Stopping")
