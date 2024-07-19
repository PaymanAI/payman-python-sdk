# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SubmissionListTaskSubmissionsParams"]


class SubmissionListTaskSubmissionsParams(TypedDict, total=False):
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
