# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentSendPaymentResponse"]


class PaymentSendPaymentResponse(BaseModel):
    reference: str
    """The Payman reference of the payment"""

    status: Literal["INITIATED", "AWAITING_APPROVAL", "REJECTED"]
    """The status of the payment"""

    external_reference: Optional[str] = FieldInfo(alias="externalReference", default=None)
    """The external reference of the payment if applicable (e.g.

    a blockchain transaction hash)
    """
