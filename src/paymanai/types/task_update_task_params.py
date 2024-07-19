# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["TaskUpdateTaskParams"]


class TaskUpdateTaskParams(TypedDict, total=False):
    description: Required[str]
    """A detailed description of the task.

    This should include enough information for the user to complete the task to the
    expected standard.
    """

    title: Required[str]
    """A descriptive title for this task"""
