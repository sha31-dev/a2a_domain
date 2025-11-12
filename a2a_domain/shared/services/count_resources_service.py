from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional
from a2a_domain.shared.models import QueryModel


class ICountResourcesService(ABC):
    @abstractmethod
    async def execute(self, query_model: Optional[QueryModel] = None) -> int:
        """
        Counts resources matching the filters.

        Returns:
            int: Number of resources matching the filters.
        """

        raise NotImplementedError()
