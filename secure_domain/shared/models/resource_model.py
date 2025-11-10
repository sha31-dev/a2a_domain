from datetime import (
    datetime,
    timezone,
)
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import (
    Any,
    Dict,
    Optional,
)
from uuid import uuid4


class ResourceModel(BaseModel):
    """
    Represents the blueprint for all domain entities on which CRUD operations can be performed.
    Contains common attributes that are essential for managing resources.
    """

    model_config = ConfigDict(extra="forbid")

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique ID for the resource.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc).replace(microsecond=0),
        description="Timestamp at which the resource was created.",
    )

    meta: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Metadata related to the resource.",
    )

    tags: Optional[str] = Field(
        default=None,
        description="Tags associated with the resource.",
    )
