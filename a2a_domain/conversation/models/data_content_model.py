from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import Literal
from a2a_domain.shared.models import StructuredDataModel


class DataContentModel(BaseModel):
    """
    Represents structured data exchanged between the actors.
    Used to send or receive structured data objects such as execution outputs, query results, form
    submissions, serialized Pydantic models etc.
    """

    model_config = ConfigDict(extra="forbid")

    data: StructuredDataModel = Field(
        description="Data to be send to and from the agent.",
    )

    type: Literal["data"] = "data"
