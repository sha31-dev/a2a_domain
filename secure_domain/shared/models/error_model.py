from datetime import (
    datetime,
    timezone,
)
from typing import (
    Any,
    Optional,
    Dict,
)
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from uuid import uuid4


class ErrorModel(BaseModel):
    """
    Represents a standardized structure for capturing, describing, and tracking errors occurring
    within the system.
    """

    model_config = ConfigDict(extra="forbid")

    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for the error.",
    )

    code: Optional[str] = Field(
        default=None,
        description="Code associated with the error.",
    )

    context: Optional[Dict[str, Any]] = Field(
        default=None,
        description=(
            "Optional key value pairs to group the error with, eg: instance_id, request_id, etc."
        ),
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc).replace(microsecond=0),
        description="Timestamp at which the error occurred.",
    )

    detail: str = Field(
        description="Explanation of the error, specific to the occurrence.",
        examples=["Connection pool timed out after 30 seconds."],
    )

    meta: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Metadata related to the error.",
    )

    title: str = Field(
        description="Summary of the error.",
        examples=["Connection Pool Timeout"],
    )

    trace: Optional[str] = Field(
        default=None,
        description="Error trace for debugging.",
        exclude=True,
    )

    type: Optional[str] = Field(
        default=None,
        description="Type of the error.",
    )
