from datetime import datetime
from pydantic import (
    ConfigDict,
    Field,
)
from typing import Optional
from secure_domain.shared.models.resource_model import ResourceModel
from secure_domain.shared.types import FileLabels


class FileModel(ResourceModel):
    """
    Represents metadata and classification details for a file within the system.
    Provides descriptive information about files that may be stored, processed,
    or referenced within the system.
    """

    model_config = ConfigDict(extra="forbid")

    description: Optional[str] = Field(
        default=None,
        description="Description related to the file.",
    )

    extension: Optional[str] = Field(
        default=None,
        description="Extension of the file.",
    )

    label: FileLabels = Field(description="Label for the file. Specifies the intended use.")

    modified_at: Optional[datetime] = Field(
        default=None,
        description="Timestamp at which the resource was modified.",
    )

    name: str = Field(description="Name of the file.")

    url: str = Field(description="URL where is file is hosted.")
