# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SubmissionListTaskSubmissionsParams"]


class SubmissionListTaskSubmissionsParams(TypedDict, total=False):
    limit: int
    """The number of items per page"""

    page: int
    """The page number to retrieve (0-indexed)"""

    statuses: Literal[
        "PENDING",
        "APPROVED_REQUIRES_REVIEW",
        "REJECTED_REQUIRES_REVIEW",
        "APPROVED",
        "REJECTED",
        "VERIFICATION_FAILED",
        "DELETED",
        "CANCELLED",
    ]
    """The statuses you want to filter by. Defaults to PENDING and APPROVED"""
