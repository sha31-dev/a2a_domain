from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import (
    List,
    Optional,
)
from secure_domain.shared.models.field_model import FieldModel
from secure_domain.shared.types import FormLabels


class FormModel(BaseModel):
    """
    Represents a structured collection of fields used to capture or display user input.
    A form defines a logical grouping of related fields, each representing a specific input
    parameter.
    """

    model_config = ConfigDict(extra="forbid")

    description: Optional[str] = Field(
        default=None,
        description="Description related to the form.",
    )

    fields: List[FieldModel] = Field(
        description="List of fields included in the form.",
    )

    label: FormLabels = Field(description="Label for the form.")

    name: str = Field(description="Name of the form.")
