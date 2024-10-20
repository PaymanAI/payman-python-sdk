# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskCreateTaskParams", "VerificationConfiguration"]


class TaskCreateTaskParams(TypedDict, total=False):
    description: Required[str]
    """A detailed description of the task.

    This should include enough information for the user to complete the task to the
    expected standard.
    """

    payout_decimal: Required[Annotated[float, PropertyInfo(alias="payoutDecimal")]]
    """The amount being offered for each approved submission on this task.

    Note the amount is denominated in base units of the currency, so a payout of 100
    in USD would mean the payout would be $1.00.
    """

    title: Required[str]
    """A descriptive title for this task"""

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
    """The task category this task should be shown under.

    Defaults to 'OTHER' if omitted.
    """

    currency: str
    """The currency is only required if a customerId is provided."""

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]

    deadline: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The deadline for this task.

    If this is set, the task will be closed after this time regardless of the number
    of submissions received and approved. If unset, the task will remain open until
    the required number of submissions are received and approved.
    """

    invite_emails: Annotated[List[str], PropertyInfo(alias="inviteEmails")]
    """List of email addresses to invite to complete the task.

    If this is set, only users with these emails will be able to complete the task.
    """

    metadata: Dict[str, str]
    """Agent provided metadata related to this task.

    You may use this to store correlation data.When a task related payload is sent
    to any registered webhook, this metadata will be included
    """

    payout_wallet_id: Annotated[str, PropertyInfo(alias="payoutWalletId")]
    """The ID of the wallet to be used to pay out rewards for this task.

    This wallet must be owned by the organization that owns this task, the agent
    creating the task must have access to the wallet, it must have sufficient funds
    to cover the payouts, and must be in the same currency as the currency of this
    task.
    """

    required_submissions: Annotated[int, PropertyInfo(alias="requiredSubmissions")]
    """The number of approved submissions required before this task is closed.

    E.g. If this is set to 2, the task will be closed after the 2 submission are
    received and approved. Defaults to 1 if omitted (or the number of inviteEmails
    provided if present).
    """

    verification_configuration: Annotated[VerificationConfiguration, PropertyInfo(alias="verificationConfiguration")]
    """The configuration to be applied during task verification.

    The Payman verification enginewill use this to customize the verification of
    this task.
    """


class VerificationConfiguration(TypedDict, total=False):
    custom_prompt: Annotated[str, PropertyInfo(alias="customPrompt")]

    type: Literal["generic", "custom_prompt", "developer_managed", "none"]
