from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    NonNegativeInt,
)
from typing import (
    Dict,
    Generic,
    List,
    Optional,
    TypeVar,
)


T = TypeVar("T")


class PaginationMetaModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: NonNegativeInt = Field(description="Number of records selected.")

    limit: NonNegativeInt = Field(
        default=1000,
        description="Number of records to select.",
    )

    offset: NonNegativeInt = Field(
        default=0,
        description="Number of records skipped.",
    )

    total: NonNegativeInt = Field(description="Total number of records available.")


class PaginatedResultModel(BaseModel, Generic[T]):
    model_config = ConfigDict(extra="forbid")

    data: List[T] = Field(
        default=[],
        description="List of queried records.",
    )

    links: Optional[Dict[str, str]] = Field(
        default=None,
        description="Links related to the records.",
    )

    meta: Optional[PaginationMetaModel] = Field(
        default=None,
        description="Metadata related to records.",
    )
