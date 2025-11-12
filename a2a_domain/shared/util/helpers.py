from datetime import datetime
from pydantic import (
    BaseModel,
    ConfigDict,
    create_model,
)
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)
from a2a_domain.shared.models import (
    FormModel,
    StructuredDataModel,
)


TYPES_MAPPING: Dict[str, Any] = {
    "boolean": bool,
    "datetime": datetime,
    "list": list,
    "number": Union[int, float],
    "object": dict,
    "string": str,
}


class DynamicBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


def validate_form_submission(data: StructuredDataModel, form: FormModel):
    if form.label != data.label:
        raise ValueError(
            "Validation failed for input [label]. Form label does not match with data label."
        )

    field_definitions: Dict[str, Any] = {}
    for field in form.fields:
        data_type = TYPES_MAPPING.get(field.type, "string")

        if field.required:
            field_definitions.update({field.name: (data_type, ...)})
        else:
            field_definitions.update({field.name: (Optional[data_type], field.default)})

    DynamicFormModel: type[BaseModel] = create_model(  # pylint: disable=all
        "DynamicForm",
        __base__=DynamicBaseModel,
        **field_definitions,
    )

    if isinstance(data.data, dict):
        DynamicFormModel(**data.data)
    else:
        for row in data.data:
            DynamicFormModel(**row)
