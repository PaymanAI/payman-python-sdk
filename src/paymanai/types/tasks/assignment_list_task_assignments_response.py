# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional, Dict

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = [
    "AssignmentListTaskAssignmentsResponse",
    "Result",
    "ResultAssignedTo",
    "ResultTask",
    "ResultTaskCurrency",
    "ResultTaskVerificationConfiguration",
]


class ResultAssignedTo(BaseModel):
    authentication_methods: List[Literal["PASSWORD", "GOOGLE"]] = FieldInfo(alias="authenticationMethods")
    """The authentication methods for this user.

    Note: may not be visible subject to caller's authorization scopes.
    """

    email: str
    """The email address for this user.

    Note: may not be visible subject to caller's authorization scopes.
    """

    first_name: str = FieldInfo(alias="firstName")
    """The first name of this user."""

    kyc_status: Literal["PENDING", "IN_REVIEW", "APPROVED", "REJECTED"] = FieldInfo(alias="kycStatus")
    """The current KYC status of this user account.

    Note: may not be visible subject to caller's authorization scopes.
    """

    last_name: str = FieldInfo(alias="lastName")
    """The last name of this user."""

    status: Literal["ACTIVE", "DELETED", "LOCKED", "PENDING"]
    """The current status of this user account"""

    id: Optional[str] = None

    phone: Optional[str] = None
    """The phone number for this user.

    Note: may not be visible subject to caller's authorization scopes.
    """


class ResultTaskCurrency(BaseModel):
    fractional_unit_name: str = FieldInfo(alias="fractionalUnitName")
    """The name of this currency's fractional unit"""

    name: str
    """The name of this currency"""

    symbol: str
    """The currency symbol to use"""

    type: Literal["CRYPTOCURRENCY", "FIAT"]

    active: Optional[bool] = None

    code: Optional[str] = None
    """The unique short code for this currency"""

    decimal_places: Optional[int] = FieldInfo(alias="decimalPlaces", default=None)
    """The number of decimal places this currency supports."""

    description: Optional[str] = None
    """A longer form description of the item"""

    display_decimal_places: Optional[int] = FieldInfo(alias="displayDecimalPlaces", default=None)
    """The number of decimal places to show when rendering an amount of this currency."""

    label: Optional[str] = None
    """A descriptive label of the item"""

    value: Optional[str] = None
    """The value of the item"""


class ResultTaskVerificationConfiguration(BaseModel):
    custom_prompt: Optional[str] = FieldInfo(alias="customPrompt", default=None)

    type: Optional[Literal["default", "custom_prompt", "none"]] = None


class ResultTask(BaseModel):
    category: Literal[
        "MARKETING",
        "ENGINEERING",
        "SALES",
        "DATA_ANALYTICS",
        "DESIGN",
        "PRODUCT_MANAGEMENT",
        "LEGAL",
        "MEDICAL",
        "FINANCE",
        "OTHER",
    ]
    """The task category this task should be shown under. Defaults to 'Other'."""

    description: str
    """A detailed description of the task.

    This should include enough information for the user to complete the task to the
    expected standard.
    """

    organization_id: str = FieldInfo(alias="organizationId")
    """The unique identifier for the organization that owns this task"""

    payout: int
    """The amount being offered for each approved submission on this task.

    Note the amount is denominated in base units of the currency, so a payout of 100
    in USD would mean the payout would be $1.00
    """

    required_submissions: int = FieldInfo(alias="requiredSubmissions")
    """The number of submissions required before this task is closed.

    If this is set to 1, the task will be closed after the first submission is
    received and approved. Defaults to 1.
    """

    submission_policy: Literal[
        "OPEN_SUBMISSIONS_ONE_PER_USER",
        "OPEN_SUBMISSIONS_MANY_PER_USER",
        "PRE_ASSIGNED_SUBMISSIONS",
        "OPEN_ASSIGNED_SUBMISSIONS",
    ] = FieldInfo(alias="submissionPolicy")
    """The policy determining who may submit solutions for this task."""

    title: str
    """A descriptive title for this task"""

    id: Optional[str] = None

    cancel_reason: Optional[str] = FieldInfo(alias="cancelReason", default=None)
    """In case the task is canceled, this stores the reason why it is canceled"""

    currency: Optional[ResultTaskCurrency] = None
    """The currency in which the payout is denominated."""

    deadline: Optional[datetime] = None
    """The deadline for this task.

    If this is set, the task will be closed after this time regardless of the number
    of submissions received and approved.
    """

    invite_links: Optional[Dict[str, str]] = FieldInfo(alias="inviteLinks", default=None)
    """A map of email address to link containing a link for each inviteEmail.

    This map is only populated immediately in response to the creation of the task
    and will contain the link that was emailedto each invited address. Also note
    that these links will only become valid once the task is published.
    """

    payout_wallet_id: Optional[str] = FieldInfo(alias="payoutWalletId", default=None)
    """The ID of the wallet to be used to pay out rewards for this task.

    This wallet must be owned by the organization that owns this task, the agent
    creating the task must have access to the wallet, it must have sufficient funds
    to cover the payouts, and must be in the same currency as the currency of this
    task.
    """

    review_notes: Optional[str] = FieldInfo(alias="reviewNotes", default=None)
    """Notes from the Payman review process about the task.

    This is used to store any additional information concerning a task's review
    status (e.g. rejection reasons).
    """

    status: Optional[
        Literal[
            "IN_REVIEW_BY_DEVELOPER",
            "IN_REVIEW_BY_AI",
            "IN_REVIEW_BY_SYSTEM_USER",
            "REJECTED",
            "OPEN",
            "STARTED",
            "COMPLETED",
            "CANCELLED",
            "SUSPENDED",
            "EXPIRED",
        ]
    ] = None
    """The current status of this task."""

    verification_configuration: Optional[ResultTaskVerificationConfiguration] = FieldInfo(
        alias="verificationConfiguration", default=None
    )
    """The configuration to be applied during task verification.

    The Payman verification enginewill use this to customize the verification of
    this task.
    """


class Result(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")

    status: Literal["IN_REVIEW", "PENDING", "COMPLETED", "EXPIRED", "DELETED", "REJECTED", "ACCEPTED"]

    task_id: str = FieldInfo(alias="taskId")

    id: Optional[str] = None

    assigned_to: Optional[ResultAssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """The user that this task is assigned to"""

    assigned_to_id: Optional[str] = FieldInfo(alias="assignedToId", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    invite_code: Optional[str] = FieldInfo(alias="inviteCode", default=None)

    invite_email: Optional[str] = FieldInfo(alias="inviteEmail", default=None)

    task: Optional[ResultTask] = None


class AssignmentListTaskAssignmentsResponse(BaseModel):
    more: Optional[bool] = None
    """Whether there are more results available"""

    next_page: Optional[int] = FieldInfo(alias="nextPage", default=None)
    """The page number for the next page of results"""

    results: Optional[List[Result]] = None
    """The list of results for the current page"""
