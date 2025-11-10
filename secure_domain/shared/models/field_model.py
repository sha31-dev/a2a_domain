from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import (
    List,
    Optional,
)
from secure_domain.shared.types import (
    FieldType,
    FieldValue,
)


class FieldModel(BaseModel):
    """
    Represents a single input or parameter within a form.
    A field defines the structure and behavior of a single form element, including its name, data
    type, default value, visibility, validation requirements etc.
    """

    model_config = ConfigDict(extra="forbid")

    default: Optional[FieldValue] = Field(
        default=None,
        description="Default value of the field.",
    )

    description: Optional[str] = Field(
        default=None,
        description="Description of the field.",
    )

    hidden: bool = Field(
        default=False,
        description="Flag indicating if the field is hidden.",
    )

    label: Optional[str] = Field(
        default=None,
        description="Display name of the field.",
    )

    name: str = Field(description="Name of the field.")

    options: Optional[List[FieldValue]] = Field(
        default=None,
        description="List of options to select the value of the field from.",
    )

    placeholder: Optional[str] = Field(
        default=None,
        description="Placeholder text for the field.",
    )

    required: bool = Field(
        default=True,
        description="Flag indicating if the field is required.",
    )

    type: FieldType = Field(
        default="string",
        description="Data type of the field.",
    )
