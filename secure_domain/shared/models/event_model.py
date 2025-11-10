import hashlib
from pydantic import (
    BaseModel,
    Field,
    model_validator,
)
from typing import (
    Any,
    Dict,
)
from secure_domain.shared.models.resource_model import ResourceModel


class EventModel(ResourceModel):
    name: str = Field(description="Name of the event.")

    properties: BaseModel = Field(
        description="Model used to populate properties.",
        exclude=True,
    )

    @model_validator(mode="before")
    # pylint: disable=no-self-argument
    def update_model(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if values.get("id") is None:
            name = values.get("name")
            properties = values.get("properties")

            properties_dict = (
                properties.model_dump(mode="json") if isinstance(properties, BaseModel) else {}
            )

            composite_key = f"{name}_{properties_dict}"

            # Set event id by generating a unqiue hash from event name and properties.
            values.update(
                {
                    "id": hashlib.md5(composite_key.encode("utf-8")).hexdigest(),
                }
            )

        return values
