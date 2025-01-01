# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentSearchDestinationsParams"]


class PaymentSearchDestinationsParams(TypedDict, total=False):
    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """The US Bank account number to search for."""

    contact_email: Annotated[str, PropertyInfo(alias="contactEmail")]
    """The contact email to search for."""

    contact_phone_number: Annotated[str, PropertyInfo(alias="contactPhoneNumber")]
    """The contact phone number to search for."""

    contact_tax_id: Annotated[str, PropertyInfo(alias="contactTaxId")]
    """The contact tax id to search for."""

    name: str
    """The name of the payment destination to search for.

    This can be a partial, case-insensitive match.
    """

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The US Bank routing number to search for."""

    type: str
    """The type of destination to search for."""
