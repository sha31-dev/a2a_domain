from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Dict,
    Generic,
    Optional,
    TypeVar,
    Union,
)
from a2a_domain.shared.models import ResourceModel
from a2a_domain.shared.types import Expression


T = TypeVar("T", bound=Union[ResourceModel, Dict[str, Any]])


class IRetrieveResourceService(ABC, Generic[T]):
    @abstractmethod
    async def execute(self, filter_model: Optional[Expression] = None) -> Optional[T]:
        """
        Retrieves a single resource matching the filters.

        Args:
            filters (Optional[Expression]): Filters to apply when retrieving resource.

        Returns:
            Optional[T]: Resource matching the filters if it exists.
        """

        raise NotImplementedError()
