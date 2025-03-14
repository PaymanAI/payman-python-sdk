# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentSendPaymentParams"]


class PaymentSendPaymentParams(TypedDict, total=False):
    amount_decimal: Required[Annotated[float, PropertyInfo(alias="amountDecimal")]]
    """The amount to generate a checkout link for.

    For example, '10.00' for USD is $10.00 or '1.000000' USDCBASE is 1 USDC.
    """

    payee_id: Required[Annotated[str, PropertyInfo(alias="payeeId")]]
    """The id of the payee you want to send the funds to.

    This must have been created using the /payments/payees endpoint or via the
    Payman dashboard before sending.
    """

    memo: str
    """A note or memo to associate with this payment."""

    metadata: Dict[str, object]

    wallet_id: Annotated[str, PropertyInfo(alias="walletId")]
    """The ID of the specific wallet from which to send the funds.

    This is only required if the agent has access to multiple wallets (not the case
    by default).
    """
