# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaskListTasksParams"]


class TaskListTasksParams(TypedDict, total=False):
    limit: int
    """The number of items per page"""

    page: int
    """The page number to retrieve (0-indexed)"""
