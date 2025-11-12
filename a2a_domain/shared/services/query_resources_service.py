from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    AsyncIterator,
    Dict,
    Generic,
    List,
    Optional,
    TypeVar,
    Union,
)
from a2a_domain.shared.models import (
    QueryModel,
    ResourceModel,
)


T = TypeVar("T", bound=Union[ResourceModel, Dict[str, Any]])


class IQueryResourcesService(ABC, Generic[T]):
    @abstractmethod
    def execute(
        self,
        query_model: Optional[QueryModel],
        batch_size: int = 1000,
    ) -> AsyncIterator[List[T]]:
        """
        Queries resources matching the filters in batches.

        Args:
            query_model (QueryModel): Properties required for querying resources.
            batch_size (int): Number of resources to retrieve in a batch.

        Yields:
            AsyncIterator[List[T]]: List of resources matching the filters.
        """

        raise NotImplementedError()
