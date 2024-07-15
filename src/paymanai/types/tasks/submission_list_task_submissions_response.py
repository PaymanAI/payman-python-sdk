# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SubmissionListTaskSubmissionsResponse",
    "Result",
    "ResultDetails",
    "ResultDetailsFeedback",
    "ResultDetailsFileAttachment",
    "ResultSubmittedBy",
    "ResultTask",
    "ResultTaskCurrency",
    "ResultTaskVerificationConfiguration",
]


class ResultDetailsFeedback(BaseModel):
    created_by: str = FieldInfo(alias="createdBy")

    created_on: datetime = FieldInfo(alias="createdOn")

    feedback: str

    type: Literal["SYSTEM_INTERNAL", "USER_COMMENT", "AGENT_COMMENT"]


class ResultDetailsFileAttachment(BaseModel):
    key: str
    """
    The identifying key for this file - supply this to the file download endpoint to
    retrieve this file.
    """

    name: str
    """A display name for the file."""

    size: Optional[int] = None
    """The size of the file in bytes."""


class ResultDetails(BaseModel):
    description: str
    """The user's description of the solution they are submitting"""

    evidence_urls: Optional[List[str]] = FieldInfo(alias="evidenceUrls", default=None)
    """
    A list of URLs to any evidence or supporting documentation the user wants to
    provide to support their submission. These will be external to the Payman
    platform.
    """

    feedback: Optional[List[ResultDetailsFeedback]] = None
    """
    Feedback provided during the verification process after reviewing the submission
    """

    file_attachments: Optional[List[ResultDetailsFileAttachment]] = FieldInfo(alias="fileAttachments", default=None)
    """
    A list of file attachments that the user uploaded directly to the Payman
    platform. To access these files they must be downloaded via the 'Download File
    Attachment' API endpoint.
    """

    notes: Optional[str] = None
    """Any additional notes or comments the user wants to provide"""


class ResultSubmittedBy(BaseModel):
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

    handler: Optional[str] = None


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
    details: ResultDetails
    """
    The details of the submission, including any evidence or notes provided by the
    user
    """

    submitted_by_id: str = FieldInfo(alias="submittedById")
    """The unique identifier for the user that submitted this task"""

    id: Optional[str] = None

    status: Optional[
        Literal[
            "PENDING",
            "APPROVED_REQUIRES_REVIEW",
            "REJECTED_REQUIRES_REVIEW",
            "APPROVED",
            "REJECTED",
            "VERIFICATION_FAILED",
            "DELETED",
        ]
    ] = None
    """The current status of the submission"""

    submitted_by: Optional[ResultSubmittedBy] = FieldInfo(alias="submittedBy", default=None)
    """The user that this task is assigned to"""

    task: Optional[ResultTask] = None


class SubmissionListTaskSubmissionsResponse(BaseModel):
    more: Optional[bool] = None
    """Whether there are more results available"""

    next_page: Optional[int] = FieldInfo(alias="nextPage", default=None)
    """The page number for the next page of results"""

    results: Optional[List[Result]] = None
    """The list of results for the current page"""
