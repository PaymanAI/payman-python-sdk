# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["TaskListTasksParams"]


class TaskListTasksParams(TypedDict, total=False):
    limit: int
    """The number of items per page"""

    page: int
    """The page number to retrieve"""
