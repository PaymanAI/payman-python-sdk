# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AssignmentCreateTaskAssignmentParams"]


class AssignmentCreateTaskAssignmentParams(TypedDict, total=False):
    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    invite_email: Annotated[str, PropertyInfo(alias="inviteEmail")]
