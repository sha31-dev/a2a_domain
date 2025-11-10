from typing import (
    Any,
    Dict,
)


class ResourceAlreadyExistsException(Exception):
    """
    Rasied when resource matching the filters already exists.
    """

    def __init__(self, key: str, resource: str, value: str):
        self.extra: Dict[str, Any] = {
            "key": key,
            "resource": resource,
            "value": value,
        }

        message = f"[{resource}] with key [{key}] having value [{value}] already exists."
        super().__init__(message)
