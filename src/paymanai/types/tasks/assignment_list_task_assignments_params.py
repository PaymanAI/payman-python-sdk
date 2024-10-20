# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AssignmentListTaskAssignmentsParams"]


class AssignmentListTaskAssignmentsParams(TypedDict, total=False):
    limit: int
    """The number of items per page"""

    page: int
    """The page number to retrieve (0-indexed)"""

    statuses: Literal["IN_REVIEW", "PENDING", "COMPLETED", "EXPIRED", "DELETED", "REJECTED", "ACCEPTED"]
    """The statuses you want to filter by. Defaults to PENDING, ACCEPTED and COMPLETED"""
