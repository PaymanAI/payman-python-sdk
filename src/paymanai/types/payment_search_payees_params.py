# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentSearchPayeesParams"]


class PaymentSearchPayeesParams(TypedDict, total=False):
    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """The US Bank account number to search for."""

    agent_reference: Annotated[str, PropertyInfo(alias="agentReference")]
    """The Payman agent reference (id or handle) to search for."""

    contact_email: Annotated[str, PropertyInfo(alias="contactEmail")]
    """The contact email to search for."""

    contact_phone_number: Annotated[str, PropertyInfo(alias="contactPhoneNumber")]
    """The contact phone number to search for."""

    contact_tax_id: Annotated[str, PropertyInfo(alias="contactTaxId")]
    """The contact tax id to search for."""

    crypto_address: Annotated[str, PropertyInfo(alias="cryptoAddress")]
    """The crypto address to search for."""

    crypto_chain: Annotated[str, PropertyInfo(alias="cryptoChain")]
    """The crypto chain to search for."""

    crypto_currency: Annotated[str, PropertyInfo(alias="cryptoCurrency")]
    """The crypto currency to search for."""

    name: str
    """The name of the payee to search for.

    This can be a partial, case-insensitive match.
    """

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The US Bank routing number to search for."""
