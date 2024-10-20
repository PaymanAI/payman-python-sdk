# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["TaskGetCategoriesResponse", "TaskGetCategoriesResponseItem"]


class TaskGetCategoriesResponseItem(BaseModel):
    description: Optional[str] = None
    """A longer form description of the item"""

    label: Optional[str] = None
    """A descriptive label of the item"""

    value: Optional[str] = None
    """The value of the item"""


TaskGetCategoriesResponse: TypeAlias = List[TaskGetCategoriesResponseItem]
