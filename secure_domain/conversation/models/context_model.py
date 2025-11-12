from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import (
    List,
    Optional,
)
from secure_domain.shared.models import (
    FileModel,
    StructuredDataModel,
)


class ContextModel(BaseModel):
    """
    Represents additional information exchanged between actors within a conversation.
    Context can be composed of data, files and texts.
    """

    model_config = ConfigDict(extra="forbid")

    data: Optional[List[StructuredDataModel]] = Field(
        default=None,
        description="Additional data to be send to the agent.",
    )

    files: Optional[List[FileModel]] = Field(
        default=None,
        description="Additional files to be send to the agent.",
    )

    texts: Optional[List[str]] = Field(
        default=None,
        description="Additional text or statements to be send to the agent.",
    )
