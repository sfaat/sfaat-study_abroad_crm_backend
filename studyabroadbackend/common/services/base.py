from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseService(ABC):
    """Base class for service-layer business logic.

    Subclasses keep business logic out of views and models by
    implementing `execute` and being called from there instead.
    """

    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def execute(self):
        raise NotImplementedError
