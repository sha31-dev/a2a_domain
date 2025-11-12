from pydantic import (
    ConfigDict,
    Field,
)
from typing import (
    List,
    Optional,
)
from secure_domain.shared.models.resource_model import ResourceModel


class UserModel(ResourceModel):
    model_config = ConfigDict(extra="forbid")

    tenant_id: str = Field(description="ID of the tenant the user belongs to.")

    email: str = Field(description="Email of the user.")

    preferences: Optional[List[str]] = Field(
        default=None,
        description="Preferences / Prompts / Rules set against the user.",
    )
