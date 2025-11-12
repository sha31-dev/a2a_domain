from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import Literal
from secure_domain.shared.models import FileModel


class FileMessageModel(BaseModel):
    """
    Represents a file reference shared between the actors.
    This message part is used for file attachments or external resources, such as documents,
    datasets, or exported results, referenced by URL.
    """

    model_config = ConfigDict(extra="forbid")

    file: FileModel = Field(
        description="File to be send to and from the agent.",
    )

    type: Literal["file"] = "file"
