# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WalletGetWalletResponse", "Currency"]


class Currency(BaseModel):
    name: str
    """The name of this currency"""

    symbol: str
    """The currency symbol to use"""

    type: Literal["CRYPTOCURRENCY", "FIAT"]

    code: Optional[str] = None
    """The unique short code for this currency"""

    decimal_places: Optional[int] = FieldInfo(alias="decimalPlaces", default=None)
    """The number of decimal places this currency supports."""

    description: Optional[str] = None
    """A longer form description of the item"""

    label: Optional[str] = None
    """A descriptive label of the item"""

    value: Optional[str] = None
    """The value of the item"""


class WalletGetWalletResponse(BaseModel):
    balance_in_escrow: int = FieldInfo(alias="balanceInEscrow")
    """The amount of currency that is currently held in escrow against created tasks."""

    currency: Currency
    """The currency this wallet is denominated in."""

    spendable_balance: int = FieldInfo(alias="spendableBalance")
    """The amount of currency that can be spent from this wallet."""

    unconfirmed_balance: int = FieldInfo(alias="unconfirmedBalance")
    """The amount of currency that is currently unconfirmed (e.g.

    incomplete deposits).
    """

    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    name: Optional[str] = None
    """A descriptive name for this wallet"""

    notes: Optional[str] = None
    """Any additional notes or information about this wallet."""

    total_balance: Optional[int] = FieldInfo(alias="totalBalance", default=None)
    """
    The total balance of this wallet, including spendable balance, balance in
    escrow, and unconfirmed balance.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)
