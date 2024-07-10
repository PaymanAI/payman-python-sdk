# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["SubmissionListParams"]


class SubmissionListParams(TypedDict, total=False):
    limit: int

    page: int

    statuses: List[
        Literal[
            "PENDING",
            "APPROVED_REQUIRES_REVIEW",
            "REJECTED_REQUIRES_REVIEW",
            "APPROVED",
            "REJECTED",
            "VERIFICATION_FAILED",
            "DELETED",
        ]
    ]
