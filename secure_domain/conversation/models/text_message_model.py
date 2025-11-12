from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from typing import (
    Literal,
    Optional,
)


class TextMessageModel(BaseModel):
    """
    Represents a plain text message exchanged between actors.
    This message part is used for natural language communication between actors.
    It may also include reasoning traces if the agent exposes its thought process or rationale.
    """

    model_config = ConfigDict(extra="forbid")

    reasoning: Optional[str] = Field(
        default=None,
        description="Reasoning done by the agent to come up with the answer.",
    )

    text: str = Field(description="Message content as text.")

    type: Literal["text"] = "text"
