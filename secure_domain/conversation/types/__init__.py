from typing import (
    Literal,
    Union,
)
from secure_domain.conversation.models.data_message_model import DataMessageModel
from secure_domain.conversation.models.error_message_model import ErrorMessageModel
from secure_domain.conversation.models.file_message_model import FileMessageModel
from secure_domain.conversation.models.form_message_model import FormMessageModel
from secure_domain.conversation.models.text_message_model import TextMessageModel


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
