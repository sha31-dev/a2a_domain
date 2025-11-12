from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import Literal
from a2a_domain.shared.models import FormModel


class FormMessageModel(BaseModel):
    """
    Represents an interactive form used by the actors to gather information.
    This message part is used to request structured input by dynamically generating a form composed
    of the defined fields.
    """

    model_config = ConfigDict(extra="forbid")

    form: FormModel = Field(description="Form to be send to and from the agent.")

    type: Literal["form"] = "form"
