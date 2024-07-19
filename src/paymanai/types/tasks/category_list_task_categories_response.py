# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["CategoryListTaskCategoriesResponse", "CategoryListTaskCategoriesResponseItem"]


class CategoryListTaskCategoriesResponseItem(BaseModel):
    description: Optional[str] = None
    """A longer form description of the item"""

    label: Optional[str] = None
    """A descriptive label of the item"""

    value: Optional[str] = None
    """The value of the item"""


CategoryListTaskCategoriesResponse = List[CategoryListTaskCategoriesResponseItem]
