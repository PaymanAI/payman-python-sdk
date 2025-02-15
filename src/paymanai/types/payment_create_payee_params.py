# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PaymentCreatePayeeParams",
    "PaymanAgentPaymentDestinationDescriptor",
    "PaymanAgentPaymentDestinationDescriptorContactDetails",
    "UsachPaymentDestinationDescriptor",
    "UsachPaymentDestinationDescriptorContactDetails",
]


class PaymanAgentPaymentDestinationDescriptor(TypedDict, total=False):
    type: Required[Literal["PAYMAN_AGENT"]]
    """The type of payment destination"""

    contact_details: Annotated[
        PaymanAgentPaymentDestinationDescriptorContactDetails, PropertyInfo(alias="contactDetails")
    ]
    """Contact details for this payment destination"""

    name: str
    """
    The name you wish to associate with this payment destination for future lookups.
    """

    payman_agent: Annotated[str, PropertyInfo(alias="paymanAgent")]
    """The Payman handle or the id of the receiver agent"""

    tags: List[str]
    """Any additional labels you wish to assign to this payment destination"""


class PaymanAgentPaymentDestinationDescriptorContactDetails(TypedDict, total=False):
    address: str
    """The address string of the payment destination contact"""

    email: str
    """The email address of the payment destination contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payment destination contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payment destination contact"""


class UsachPaymentDestinationDescriptor(TypedDict, total=False):
    type: Required[Literal["US_ACH"]]
    """The type of payment destination"""

    account_holder_name: Annotated[str, PropertyInfo(alias="accountHolderName")]
    """The name of the account holder"""

    account_holder_type: Annotated[Literal["individual", "business"], PropertyInfo(alias="accountHolderType")]
    """The type of the account holder"""

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """The bank account number for the account"""

    account_type: Annotated[str, PropertyInfo(alias="accountType")]
    """The type of account it is (checking or savings)"""

    contact_details: Annotated[UsachPaymentDestinationDescriptorContactDetails, PropertyInfo(alias="contactDetails")]
    """Contact details for this payment destination"""

    name: str
    """
    The name you wish to associate with this payment destination for future lookups.
    """

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The routing number of the bank"""

    tags: List[str]
    """Any additional labels you wish to assign to this payment destination"""


class UsachPaymentDestinationDescriptorContactDetails(TypedDict, total=False):
    address: str
    """The address string of the payment destination contact"""

    email: str
    """The email address of the payment destination contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payment destination contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payment destination contact"""


PaymentCreatePayeeParams: TypeAlias = Union[PaymanAgentPaymentDestinationDescriptor, UsachPaymentDestinationDescriptor]
