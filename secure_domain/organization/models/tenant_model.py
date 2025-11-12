from pydantic import (
    ConfigDict,
    Field,
)
from typing import (
    List,
    Optional,
)
from secure_domain.shared.models.resource_model import ResourceModel


class TenantModel(ResourceModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(description="Name of the tenant.")

    preferences: Optional[List[str]] = Field(
        default=None,
        description="Preferences / Prompts / Rules set against the tenant.",
    )
