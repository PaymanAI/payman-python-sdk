# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentInitiateCustomerDepositParams"]


class PaymentInitiateCustomerDepositParams(TypedDict, total=False):
    amount_decimal: Required[Annotated[float, PropertyInfo(alias="amountDecimal")]]
    """The amount to generate a checkout link for.

    For example, '10.00' for USD is $10.00 or '1.000000' USDCBASE is 1 USDC.
    """

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The ID of the customer to deposit funds for.

    This can be any unique ID as held within your system.
    """

    customer_email: Annotated[str, PropertyInfo(alias="customerEmail")]
    """An email address to associate with this customer."""

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """A name to associate with this customer."""

    fee_mode: Annotated[Literal["INCLUDED_IN_AMOUNT", "ADD_TO_AMOUNT"], PropertyInfo(alias="feeMode")]
    """Determines whether to add any processing fees to the requested amount.

    If set to INCLUDED_IN_AMOUNT, the customer will be charged the exact amount
    specified, and fees will be deducted from that before the remainder is deposited
    in the wallet. If set to ADD_TO_AMOUNT, the customer will be charged the amount
    specified plus any fees required. Defaults to 'INCLUDED_IN_AMOUNT'.
    """

    memo: str
    """A memo to associate with any transactions created in the Payman ledger."""

    metadata: Dict[str, object]

    wallet_id: Annotated[str, PropertyInfo(alias="walletId")]
    """The ID of the wallet you would like the customer to add funds to.

    Only required if the agent has access to more than one wallet.
    """
