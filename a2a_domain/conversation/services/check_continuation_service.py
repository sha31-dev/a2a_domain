from abc import (
    ABC,
    abstractmethod,
)
from typing import List
from a2a_domain.conversation.models import MessageModel


class ICheckContinuationService(ABC):
    @abstractmethod
    async def execute(
        self,
        message_model: MessageModel,
        previous_message_models: List[MessageModel],
    ) -> bool:
        """
        Determines whether the given message is a continuation of previous messages having the same
        intent.

        Args:
            message_model (MessageModel): Current message to evaluate.
            previous_message_models (List[MessageModel]): List of previous messages.
                These may represent the full history or the most recent subset of messages.

        Returns:
            bool: Flag indicating if message is continuation of the same intent.
        """

        raise NotImplementedError
