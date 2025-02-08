# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentGetDepositLinkResponse"]


class PaymentGetDepositLinkResponse(BaseModel):
    checkout_url: str = FieldInfo(alias="checkoutUrl")
    """A URL that you can redirect the user to in order to complete the deposit."""
