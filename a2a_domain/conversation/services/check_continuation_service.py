from abc import (
    ABC,
    abstractmethod,
)
from typing import List
from a2a_domain.conversation.models import TextMessageModel


class ICheckContinuationService(ABC):
    @abstractmethod
    async def execute(
        self,
        text_message_model: TextMessageModel,
        previous_text_message_models: List[TextMessageModel],
    ) -> bool:
        """
        Determines whether the given message is a continuation of previous messages having the
        same intent.

        Args:
            text_message_model (TextMessageModel): Current message to evaluate.
            previous_text_message_models (List[TextMessageModel]): List of previous messages.
                These may represent the full history or the most recent subset of messages.

        Returns:
            bool: Flag indicating if message is continuation of the same intent.
        """

        raise NotImplementedError
