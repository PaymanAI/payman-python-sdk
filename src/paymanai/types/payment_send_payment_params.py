# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PaymentSendPaymentParams",
    "PaymentDestination",
    "PaymentDestinationCryptoAddressPaymentDestinationDescriptor",
    "PaymentDestinationCryptoAddressPaymentDestinationDescriptorContactDetails",
    "PaymentDestinationUsachPaymentDestinationDescriptor",
    "PaymentDestinationUsachPaymentDestinationDescriptorContactDetails",
]


class PaymentSendPaymentParams(TypedDict, total=False):
    amount_decimal: Required[Annotated[float, PropertyInfo(alias="amountDecimal")]]
    """The amount to generate a checkout link for.

    For example, '10.00' for USD is $10.00 or '1.000000' USDCBASE is 1 USDC.
    """

    customer_email: Annotated[str, PropertyInfo(alias="customerEmail")]
    """An email address to associate with this customer."""

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """The ID of the customer on whose behalf you're transferring funds.

    This can be any unique ID as held within your system. Providing this will limit
    the spendableamounts to what the customer has already deposited (unless
    ignoreCustomerSpendLimits is set to true).
    """

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """A name to associate with this customer."""

    ignore_customer_spend_limits: Annotated[bool, PropertyInfo(alias="ignoreCustomerSpendLimits")]
    """
    By default Payman will limit spending on behalf of a customer to the amount they
    have deposited. If you wish to ignore this limit, set this to true.
    """

    memo: str
    """A note or memo to associate with this payment."""

    metadata: Dict[str, object]

    payment_destination: Annotated[PaymentDestination, PropertyInfo(alias="paymentDestination")]
    """A cryptocurrency address-based payment destination"""

    payment_destination_id: Annotated[str, PropertyInfo(alias="paymentDestinationId")]
    """The id of the payment destination you want to send the funds to.

    This must have been created using the /payments/destinations endpoint or via the
    Payman dashboard before sending. Exactly one of paymentDestination and
    paymentDestinationId must be provided.
    """

    wallet_id: Annotated[str, PropertyInfo(alias="walletId")]
    """The ID of the specific wallet from which to send the funds.

    This is only required if the agent has access to multiple wallets (not the case
    by default).
    """


class PaymentDestinationCryptoAddressPaymentDestinationDescriptorContactDetails(TypedDict, total=False):
    address: str
    """The address string of the payment destination contact"""

    contact_type: Annotated[Literal["individual", "business"], PropertyInfo(alias="contactType")]
    """The type of the payment destination contact"""

    email: str
    """The email address of the payment destination contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payment destination contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payment destination contact"""


class PaymentDestinationCryptoAddressPaymentDestinationDescriptor(TypedDict, total=False):
    type: Required[Literal["CRYPTO_ADDRESS"]]
    """The type of payment destination"""

    address: str
    """The cryptocurrency address to send funds to"""

    contact_details: Annotated[
        PaymentDestinationCryptoAddressPaymentDestinationDescriptorContactDetails, PropertyInfo(alias="contactDetails")
    ]
    """Contact details for this payment destination"""

    currency: str
    """The the blockchain to use for the transaction"""

    name: str
    """
    The name you wish to associate with this payment destination for future lookups.
    """

    tags: List[str]
    """Any additional labels you wish to assign to this payment destination"""


class PaymentDestinationUsachPaymentDestinationDescriptorContactDetails(TypedDict, total=False):
    address: str
    """The address string of the payment destination contact"""

    contact_type: Annotated[Literal["individual", "business"], PropertyInfo(alias="contactType")]
    """The type of the payment destination contact"""

    email: str
    """The email address of the payment destination contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payment destination contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payment destination contact"""


class PaymentDestinationUsachPaymentDestinationDescriptor(TypedDict, total=False):
    type: Required[Literal["US_ACH"]]
    """The type of payment destination"""

    account_holder_name: Annotated[str, PropertyInfo(alias="accountHolderName")]
    """The name of the account holder"""

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """The bank account number for the account"""

    account_type: Annotated[str, PropertyInfo(alias="accountType")]
    """The type of account it is (checking or savings)"""

    contact_details: Annotated[
        PaymentDestinationUsachPaymentDestinationDescriptorContactDetails, PropertyInfo(alias="contactDetails")
    ]
    """Contact details for this payment destination"""

    name: str
    """
    The name you wish to associate with this payment destination for future lookups.
    """

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The routing number of the bank"""

    tags: List[str]
    """Any additional labels you wish to assign to this payment destination"""


PaymentDestination: TypeAlias = Union[
    PaymentDestinationCryptoAddressPaymentDestinationDescriptor, PaymentDestinationUsachPaymentDestinationDescriptor
]
