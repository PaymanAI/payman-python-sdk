# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AssignmentListTaskAssignmentsParams"]


class AssignmentListTaskAssignmentsParams(TypedDict, total=False):
    limit: int

    page: int

    statuses: List[Literal["IN_REVIEW", "PENDING", "COMPLETED", "EXPIRED", "DELETED", "REJECTED", "ACCEPTED"]]
