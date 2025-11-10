from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Literal,
    Union,
)
from py_query_builder.types import (
    Condition,
    Expression,
    NestedConditionList,
    Primitive,
    Scalar,
    ScalarList,
)


FieldType = Literal["boolean", "datetime", "list", "number", "object", "string"]
FieldValue = Union[bool, datetime, Dict[str, Any], int, List[Any], str]


DataLabels = Literal[
    "ActionItem",  # Used for structured data containing a single action item.
    "ActionItems",  # Used for structured data containing a list of action items.
    "Approval",  # Used for forms asking for any approvals.
    "Job",  # Used for long running tasks resulted from execution of action item.
    "Parameters",  # Used for parameters submission of an action item.
    "Results",  # Used for results returned immediately after execution of action item.
]

FileLabels = Literal[
    "Exports",  # Used for files with exported structured data.
    "KnowledgeBase",  # Used for files that are part of the knowledge base.
]

FormLabels = Literal[
    "Approval",  # Used for forms asking for any approvals.
    "Parameters",  # Used for forms asking for any missing parameters or parameters verification
    # for action item execution.
]
