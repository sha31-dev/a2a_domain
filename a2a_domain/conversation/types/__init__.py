from typing import (
    Literal,
    Union,
)
from a2a_domain.conversation.models.data_content_model import DataContentModel
from a2a_domain.conversation.models.error_content_model import ErrorContentModel
from a2a_domain.conversation.models.file_content_model import FileContentModel
from a2a_domain.conversation.models.form_content_model import FormContentModel
from a2a_domain.conversation.models.text_content_model import TextContentModel


Content = Union[
    DataContentModel,
    ErrorContentModel,
    FileContentModel,
    FormContentModel,
    TextContentModel,
]

Context = Union[
    DataContentModel,
    FileContentModel,
    TextContentModel,
]

MessageRole = Literal[
    "agent",
    "human",
]

MessageType = Literal[
    "query",
    "response",
]
