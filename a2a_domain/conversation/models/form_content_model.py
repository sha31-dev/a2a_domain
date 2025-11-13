from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import Literal
from a2a_domain.shared.models import FormModel


class FormContentModel(BaseModel):
    """
    Represents an interactive form used by the actors to gather information.
    Used to request structured input by dynamically generating a form composed of the defined
    fields.
    """

    model_config = ConfigDict(extra="forbid")

    form: FormModel = Field(description="Form to be send to and from the agent.")

    type: Literal["form"] = "form"
