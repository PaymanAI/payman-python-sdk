# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PaymentSearchDestinationsResponse",
    "PaymentSearchDestinationsResponseItem",
    "PaymentSearchDestinationsResponseItemContactDetails",
]


class PaymentSearchDestinationsResponseItemContactDetails(BaseModel):
    address: Optional[str] = None
    """The address string of the payment destination contact"""

    contact_type: Optional[Literal["individual", "business"]] = FieldInfo(alias="contactType", default=None)
    """The type of the payment destination contact"""

    email: Optional[str] = None
    """The email address of the payment destination contact"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """The phone number of the payment destination contact"""

    tax_id: Optional[str] = FieldInfo(alias="taxId", default=None)
    """The tax identification of the payment destination contact"""


class PaymentSearchDestinationsResponseItem(BaseModel):
    name: str
    """The user-assigned name of the payment destination"""

    organization_id: str = FieldInfo(alias="organizationId")

    type: Literal["US_ACH", "CRYPTO_ADDRESS"]
    """The type of payment destination"""

    id: Optional[str] = None

    contact_details: Optional[PaymentSearchDestinationsResponseItemContactDetails] = FieldInfo(
        alias="contactDetails", default=None
    )
    """Contact details for this payment destination"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    destination_details: Optional[Dict[str, object]] = FieldInfo(alias="destinationDetails", default=None)

    provider_info: Optional[Dict[str, object]] = FieldInfo(alias="providerInfo", default=None)

    replaces_id: Optional[str] = FieldInfo(alias="replacesId", default=None)
    """The ID of the payment method this entity replaces"""

    search_hashes: Optional[Dict[str, object]] = FieldInfo(alias="searchHashes", default=None)

    status: Optional[Literal["ACTIVE", "ARCHIVED", "DELETED"]] = None
    """The status of the payment destination"""

    tags: Optional[List[str]] = None
    """Tags to help categorize the payment destination"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)


PaymentSearchDestinationsResponse: TypeAlias = List[PaymentSearchDestinationsResponseItem]
