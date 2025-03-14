# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PaymentSearchPayeesResponse",
    "PaymentSearchPayeesResponseItem",
    "PaymentSearchPayeesResponseItemContactDetails",
    "PaymentSearchPayeesResponseItemContactDetailsAddress",
]


class PaymentSearchPayeesResponseItemContactDetailsAddress(BaseModel):
    address_line1: Optional[str] = FieldInfo(alias="addressLine1", default=None)

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)

    address_line3: Optional[str] = FieldInfo(alias="addressLine3", default=None)

    address_line4: Optional[str] = FieldInfo(alias="addressLine4", default=None)

    country: Optional[str] = None

    locality: Optional[str] = None

    postcode: Optional[str] = None

    region: Optional[str] = None


class PaymentSearchPayeesResponseItemContactDetails(BaseModel):
    address: Optional[PaymentSearchPayeesResponseItemContactDetailsAddress] = None
    """The address string of the payee contact.

    IMPORTANTIf you are paying someone from a USDC wallet by ACH (US_ACH payee
    type), you are required to provide an address
    """

    email: Optional[str] = None
    """The email address of the payee contact"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """The phone number of the payee contact"""

    tax_id: Optional[str] = FieldInfo(alias="taxId", default=None)
    """The tax identification of the payee contact"""


class PaymentSearchPayeesResponseItem(BaseModel):
    name: str
    """The user-assigned name of the payee"""

    organization_id: str = FieldInfo(alias="organizationId")

    type: Literal["US_ACH", "CRYPTO_ADDRESS", "PAYMAN_WALLET", "TEST_RAILS"]
    """The type of payee"""

    id: Optional[str] = None

    contact_details: Optional[PaymentSearchPayeesResponseItemContactDetails] = FieldInfo(
        alias="contactDetails", default=None
    )
    """Contact details for this payee"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    payee_details: Optional[Dict[str, object]] = FieldInfo(alias="payeeDetails", default=None)

    provider_info: Optional[Dict[str, object]] = FieldInfo(alias="providerInfo", default=None)

    replaces_id: Optional[str] = FieldInfo(alias="replacesId", default=None)
    """The ID of the payee this entity replaces"""

    search_hashes: Optional[Dict[str, object]] = FieldInfo(alias="searchHashes", default=None)

    status: Optional[Literal["ACTIVE", "ARCHIVED", "DELETED"]] = None
    """The status of the payee"""

    tags: Optional[List[str]] = None
    """Tags to help categorize the payee"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)


PaymentSearchPayeesResponse: TypeAlias = List[PaymentSearchPayeesResponseItem]
