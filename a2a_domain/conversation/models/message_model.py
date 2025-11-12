from pydantic import Field
from typing import (
    Any,
    Dict,
    List,
    Optional,
)
from uuid import uuid4
from a2a_domain.conversation.types import (
    MessagePart,
    MessageRole,
    MessageType,
)
from a2a_domain.shared.models import ResourceModel


class MessageModel(ResourceModel):
    """
    Represents a communication unit exchanged between actors within a conversation.
    Each message belongs to a thread and can consist of multiple parts, such as data, errors,
    files, forms, text etc.
    """

    thread_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="ID of the thread the message belongs to.",
    )

    parts: List[MessagePart] = Field(
        description="Content of the message, each being a different type.",
    )

    role: MessageRole = Field(
        default="human",
        description="Sender of the message.",
    )

    scope: Optional[Dict[str, Any]] = Field(
        default=None,
        description=(
            "Optional key value pairs to group the message with. Messages with scope, "
            "when replied to, will contain the same scope in the responding message."
        ),
        examples=[{"tenant_id": "t1", "user_id": "u1"}],
    )

    tags: Optional[List[str]] = Field(
        default=None,
        description="List of tags for categorizing or filtering messages.",
    )

    type: MessageType = Field(
        default="query",
        description="Type of the message.",
    )
