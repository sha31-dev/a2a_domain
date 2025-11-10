from typing import (
    Any,
    Dict,
)


class ResourceNotFoundException(Exception):
    """
    Rasied when resource matching the filters is not found.
    """

    def __init__(self, key: str, resource: str, value: str):
        self.extra: Dict[str, Any] = {
            "key": key,
            "resource": resource,
            "value": value,
        }

        message = f"[{resource}] with key [{key}] having value [{value}] not found."
        super().__init__(message)
