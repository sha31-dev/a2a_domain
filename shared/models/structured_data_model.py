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
from shared.types import DataLabels


class StructuredDataModel(BaseModel):
    """
    Represents a structured data block exchanged between components.
    Provides a unified schema for carrying structured information.
    """

    model_config = ConfigDict(extra="forbid")

    data: Dict[str, Any] = Field(
        description="Structured data object.",
        examples=[
            {"action_item": {"id": "364251e9-8744-4b41-aa17-5581f8d4e83b"}},
            {"action_items": [{"id": "364251e9-8744-4b41-aa17-5581f8d4e83b"}]},
            {"approval": True},
            {"parameters": {"key1": "value1", "key2": "value2"}},
        ],
    )

    description: Optional[str] = Field(
        default=None,
        description="Description of the data.",
    )

    label: DataLabels = Field(description="Label for the data.")
