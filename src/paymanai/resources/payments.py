# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import payment_initiate_customer_deposit_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_initiate_customer_deposit_response import PaymentInitiateCustomerDepositResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/paymanai-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/paymanai-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    def initiate_customer_deposit(
        self,
        *,
        amount_decimal: float,
        customer_id: str,
        currency_code: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        fee_mode: Literal["INCLUDED_IN_AMOUNT", "ADD_TO_AMOUNT"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentInitiateCustomerDepositResponse:
        """
        Get a deposit url that you can present to the user to let them deposit fundsinto
        a wallet of their own. The wallet will be auto-created and the funds will
        flowinto that wallet once they complete the checkout process.

        Args:
          amount_decimal: The amount to generate a checkout link for. For example, '10.00' for USD is
              $10.00 or '1.000000' USDCBASE is 1 USDC.

          customer_id: The ID of the customer to deposit funds for. This can be any unique ID as held
              within your system.

          currency_code: The currency code for which to generate a URL. Either USD or USDCBASE. If
              omitted the currency will match the agent's default currency.

          email: An email address to associate with this customer.

          fee_mode: Determines whether to add any processing fees to the requested amount. If set to
              INCLUDED_IN_AMOUNT, the customer will be charged the exact amount specified, and
              fees will be deducted from that before the remainder is deposited in the wallet.
              If set to ADD_TO_AMOUNT, the customer will be charged the amount specified plus
              any fees required. Defaults to 'INCLUDED_IN_AMOUNT'.

          metadata: Agent provided metadata related to this deposit. You may use this to store
              correlation data.When a task related payload is sent to any registered webhook,
              this metadata will be included

          name: A name to associate with this customer.

          wallet_id: The wallet into which to deposit the funds. If omitted the funds will be
              deposited into a wallet created for the customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._post(
            "/payments/initiate-customer-deposit",
            body=maybe_transform(
                {
                    "amount_decimal": amount_decimal,
                    "customer_id": customer_id,
                    "currency_code": currency_code,
                    "email": email,
                    "fee_mode": fee_mode,
                    "metadata": metadata,
                    "name": name,
                    "wallet_id": wallet_id,
                },
                payment_initiate_customer_deposit_params.PaymentInitiateCustomerDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentInitiateCustomerDepositResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/paymanai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/paymanai-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    async def initiate_customer_deposit(
        self,
        *,
        amount_decimal: float,
        customer_id: str,
        currency_code: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        fee_mode: Literal["INCLUDED_IN_AMOUNT", "ADD_TO_AMOUNT"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentInitiateCustomerDepositResponse:
        """
        Get a deposit url that you can present to the user to let them deposit fundsinto
        a wallet of their own. The wallet will be auto-created and the funds will
        flowinto that wallet once they complete the checkout process.

        Args:
          amount_decimal: The amount to generate a checkout link for. For example, '10.00' for USD is
              $10.00 or '1.000000' USDCBASE is 1 USDC.

          customer_id: The ID of the customer to deposit funds for. This can be any unique ID as held
              within your system.

          currency_code: The currency code for which to generate a URL. Either USD or USDCBASE. If
              omitted the currency will match the agent's default currency.

          email: An email address to associate with this customer.

          fee_mode: Determines whether to add any processing fees to the requested amount. If set to
              INCLUDED_IN_AMOUNT, the customer will be charged the exact amount specified, and
              fees will be deducted from that before the remainder is deposited in the wallet.
              If set to ADD_TO_AMOUNT, the customer will be charged the amount specified plus
              any fees required. Defaults to 'INCLUDED_IN_AMOUNT'.

          metadata: Agent provided metadata related to this deposit. You may use this to store
              correlation data.When a task related payload is sent to any registered webhook,
              this metadata will be included

          name: A name to associate with this customer.

          wallet_id: The wallet into which to deposit the funds. If omitted the funds will be
              deposited into a wallet created for the customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._post(
            "/payments/initiate-customer-deposit",
            body=await async_maybe_transform(
                {
                    "amount_decimal": amount_decimal,
                    "customer_id": customer_id,
                    "currency_code": currency_code,
                    "email": email,
                    "fee_mode": fee_mode,
                    "metadata": metadata,
                    "name": name,
                    "wallet_id": wallet_id,
                },
                payment_initiate_customer_deposit_params.PaymentInitiateCustomerDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentInitiateCustomerDepositResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.initiate_customer_deposit = to_raw_response_wrapper(
            payments.initiate_customer_deposit,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.initiate_customer_deposit = async_to_raw_response_wrapper(
            payments.initiate_customer_deposit,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.initiate_customer_deposit = to_streamed_response_wrapper(
            payments.initiate_customer_deposit,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.initiate_customer_deposit = async_to_streamed_response_wrapper(
            payments.initiate_customer_deposit,
        )
