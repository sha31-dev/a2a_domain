from typing import (
    Literal,
    Union,
)
from a2a_domain.conversation.models.data_message_model import DataMessageModel
from a2a_domain.conversation.models.error_message_model import ErrorMessageModel
from a2a_domain.conversation.models.file_message_model import FileMessageModel
from a2a_domain.conversation.models.form_message_model import FormMessageModel
from a2a_domain.conversation.models.text_message_model import TextMessageModel


MessagePart = Union[
    DataMessageModel,
    ErrorMessageModel,
    FileMessageModel,
    FormMessageModel,
    TextMessageModel,
]

MessageRole = Literal[
    "agent",
    "human",
]

MessageType = Literal[
    "query",
    "response",
]
