# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssignmentCreateParams"]


class AssignmentCreateParams(TypedDict, total=False):
    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    invite_email: Annotated[str, PropertyInfo(alias="inviteEmail")]
