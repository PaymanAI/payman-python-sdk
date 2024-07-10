# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    description: Required[str]
    """A detailed description of the task.

    This should include enough information for the user to complete the task to the
    expected standard.
    """

    title: Required[str]
    """A descriptive title for this task"""
