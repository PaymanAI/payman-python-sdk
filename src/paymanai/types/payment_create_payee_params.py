# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PaymentCreatePayeeParams",
    "CryptoAddressPayeeDescriptor",
    "CryptoAddressPayeeDescriptorContactDetails",
    "CryptoAddressPayeeDescriptorContactDetailsAddress",
    "PaymanWalletPayeeDescriptor",
    "PaymanWalletPayeeDescriptorContactDetails",
    "PaymanWalletPayeeDescriptorContactDetailsAddress",
    "TsdPayeeDescriptor",
    "UsachPayeeDescriptor",
    "UsachPayeeDescriptorContactDetails",
    "UsachPayeeDescriptorContactDetailsAddress",
]


class CryptoAddressPayeeDescriptor(TypedDict, total=False):
    type: Required[Literal["CRYPTO_ADDRESS"]]
    """The type of payee"""

    address: str
    """The cryptocurrency address to send funds to"""

    chain: str
    """The the blockchain to use for the transaction"""

    contact_details: Annotated[CryptoAddressPayeeDescriptorContactDetails, PropertyInfo(alias="contactDetails")]
    """Contact details for this payee"""

    currency: str
    """The the currency/token to use for the transaction"""

    name: str
    """The name you wish to associate with this payee for future lookups."""

    tags: List[str]
    """Any additional labels you wish to assign to this payee"""


class CryptoAddressPayeeDescriptorContactDetailsAddress(TypedDict, total=False):
    address_line1: Annotated[str, PropertyInfo(alias="addressLine1")]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]

    address_line3: Annotated[str, PropertyInfo(alias="addressLine3")]

    address_line4: Annotated[str, PropertyInfo(alias="addressLine4")]

    country: str

    locality: str

    postcode: str

    region: str


class CryptoAddressPayeeDescriptorContactDetails(TypedDict, total=False):
    address: CryptoAddressPayeeDescriptorContactDetailsAddress
    """The address string of the payee contact.

    IMPORTANTIf you are paying someone from a USDC wallet by ACH (US_ACH payee
    type), you are required to provide an address
    """

    email: str
    """The email address of the payee contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payee contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payee contact"""


class PaymanWalletPayeeDescriptor(TypedDict, total=False):
    type: Required[Literal["PAYMAN_WALLET"]]
    """The type of payee"""

    contact_details: Annotated[PaymanWalletPayeeDescriptorContactDetails, PropertyInfo(alias="contactDetails")]
    """Contact details for this payee"""

    name: str
    """The name you wish to associate with this payee for future lookups."""

    payman_wallet: Annotated[str, PropertyInfo(alias="paymanWallet")]
    """The Payman handle or the id of the receiver wallet"""

    tags: List[str]
    """Any additional labels you wish to assign to this payee"""


class PaymanWalletPayeeDescriptorContactDetailsAddress(TypedDict, total=False):
    address_line1: Annotated[str, PropertyInfo(alias="addressLine1")]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]

    address_line3: Annotated[str, PropertyInfo(alias="addressLine3")]

    address_line4: Annotated[str, PropertyInfo(alias="addressLine4")]

    country: str

    locality: str

    postcode: str

    region: str


class PaymanWalletPayeeDescriptorContactDetails(TypedDict, total=False):
    address: PaymanWalletPayeeDescriptorContactDetailsAddress
    """The address string of the payee contact.

    IMPORTANTIf you are paying someone from a USDC wallet by ACH (US_ACH payee
    type), you are required to provide an address
    """

    email: str
    """The email address of the payee contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payee contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payee contact"""


class TsdPayeeDescriptor(TypedDict, total=False):
    type: Required[Literal["TEST_RAILS"]]
    """The type of payee"""

    name: str
    """The name you wish to associate with this payee for future lookups."""

    tags: List[str]
    """Any additional labels you wish to assign to this payee"""


class UsachPayeeDescriptor(TypedDict, total=False):
    type: Required[Literal["US_ACH"]]
    """The type of payee"""

    account_holder_name: Annotated[str, PropertyInfo(alias="accountHolderName")]
    """The name of the account holder"""

    account_holder_type: Annotated[Literal["individual", "business"], PropertyInfo(alias="accountHolderType")]
    """The type of the account holder"""

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """The bank account number for the account"""

    account_type: Annotated[str, PropertyInfo(alias="accountType")]
    """The type of account it is (checking or savings)"""

    contact_details: Annotated[UsachPayeeDescriptorContactDetails, PropertyInfo(alias="contactDetails")]
    """Contact details for this payee"""

    name: str
    """The name you wish to associate with this payee for future lookups."""

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The routing number of the bank"""

    tags: List[str]
    """Any additional labels you wish to assign to this payee"""


class UsachPayeeDescriptorContactDetailsAddress(TypedDict, total=False):
    address_line1: Annotated[str, PropertyInfo(alias="addressLine1")]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]

    address_line3: Annotated[str, PropertyInfo(alias="addressLine3")]

    address_line4: Annotated[str, PropertyInfo(alias="addressLine4")]

    country: str

    locality: str

    postcode: str

    region: str


class UsachPayeeDescriptorContactDetails(TypedDict, total=False):
    address: UsachPayeeDescriptorContactDetailsAddress
    """The address string of the payee contact.

    IMPORTANTIf you are paying someone from a USDC wallet by ACH (US_ACH payee
    type), you are required to provide an address
    """

    email: str
    """The email address of the payee contact"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the payee contact"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """The tax identification of the payee contact"""


PaymentCreatePayeeParams: TypeAlias = Union[
    CryptoAddressPayeeDescriptor, PaymanWalletPayeeDescriptor, TsdPayeeDescriptor, UsachPayeeDescriptor
]
