# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, overload

import httpx

from ..types import (
    payment_create_payee_params,
    payment_send_payment_params,
    payment_search_payees_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
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
from ..types.payment_create_payee_response import PaymentCreatePayeeResponse
from ..types.payment_delete_payee_response import PaymentDeletePayeeResponse
from ..types.payment_send_payment_response import PaymentSendPaymentResponse
from ..types.payment_search_payees_response import PaymentSearchPayeesResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    @overload
    def create_payee(
        self,
        *,
        type: Literal["CRYPTO_ADDRESS"],
        address: str | NotGiven = NOT_GIVEN,
        chain: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.CryptoAddressPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          address: The cryptocurrency address to send funds to

          chain: The the blockchain to use for the transaction

          contact_details: Contact details for this payee

          currency: The the currency/token to use for the transaction

          name: The name you wish to associate with this payee for future lookups.

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_payee(
        self,
        *,
        type: Literal["PAYMAN_WALLET"],
        contact_details: payment_create_payee_params.PaymanWalletPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        payman_wallet: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          contact_details: Contact details for this payee

          name: The name you wish to associate with this payee for future lookups.

          payman_wallet: The Payman handle or the id of the receiver wallet

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_payee(
        self,
        *,
        type: Literal["TEST_RAILS"],
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          name: The name you wish to associate with this payee for future lookups.

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_payee(
        self,
        *,
        type: Literal["US_ACH"],
        account_holder_name: str | NotGiven = NOT_GIVEN,
        account_holder_type: Literal["individual", "business"] | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        account_type: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.UsachPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          account_holder_name: The name of the account holder

          account_holder_type: The type of the account holder

          account_number: The bank account number for the account

          account_type: The type of account it is (checking or savings)

          contact_details: Contact details for this payee

          name: The name you wish to associate with this payee for future lookups.

          routing_number: The routing number of the bank

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    def create_payee(
        self,
        *,
        type: Literal["CRYPTO_ADDRESS"] | Literal["PAYMAN_WALLET"] | Literal["TEST_RAILS"] | Literal["US_ACH"],
        address: str | NotGiven = NOT_GIVEN,
        chain: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.CryptoAddressPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        payman_wallet: str | NotGiven = NOT_GIVEN,
        account_holder_name: str | NotGiven = NOT_GIVEN,
        account_holder_type: Literal["individual", "business"] | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        account_type: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._post(
            "/payments/payees",
            body=maybe_transform(
                {
                    "type": type,
                    "address": address,
                    "chain": chain,
                    "contact_details": contact_details,
                    "currency": currency,
                    "name": name,
                    "tags": tags,
                    "payman_wallet": payman_wallet,
                    "account_holder_name": account_holder_name,
                    "account_holder_type": account_holder_type,
                    "account_number": account_number,
                    "account_type": account_type,
                    "routing_number": routing_number,
                },
                payment_create_payee_params.PaymentCreatePayeeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreatePayeeResponse,
        )

    def delete_payee(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentDeletePayeeResponse:
        """
        Delete a payee (aka payee)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._delete(
            f"/payments/payees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentDeletePayeeResponse,
        )

    def search_payees(
        self,
        *,
        account_number: str | NotGiven = NOT_GIVEN,
        agent_reference: str | NotGiven = NOT_GIVEN,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone_number: str | NotGiven = NOT_GIVEN,
        contact_tax_id: str | NotGiven = NOT_GIVEN,
        crypto_address: str | NotGiven = NOT_GIVEN,
        crypto_chain: str | NotGiven = NOT_GIVEN,
        crypto_currency: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSearchPayeesResponse:
        """Searches existing payee for potential matches.

        Additional confirmation from the
        user is required to verify the correct payee is selected.

        Args:
          account_number: The US Bank account number to search for.

          agent_reference: The Payman agent reference (id or handle) to search for.

          contact_email: The contact email to search for.

          contact_phone_number: The contact phone number to search for.

          contact_tax_id: The contact tax id to search for.

          crypto_address: The crypto address to search for.

          crypto_chain: The crypto chain to search for.

          crypto_currency: The crypto currency to search for.

          name: The name of the payee to search for. This can be a partial, case-insensitive
              match.

          routing_number: The US Bank routing number to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._get(
            "/payments/search-payees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_number": account_number,
                        "agent_reference": agent_reference,
                        "contact_email": contact_email,
                        "contact_phone_number": contact_phone_number,
                        "contact_tax_id": contact_tax_id,
                        "crypto_address": crypto_address,
                        "crypto_chain": crypto_chain,
                        "crypto_currency": crypto_currency,
                        "name": name,
                        "routing_number": routing_number,
                    },
                    payment_search_payees_params.PaymentSearchPayeesParams,
                ),
            ),
            cast_to=PaymentSearchPayeesResponse,
        )

    def send_payment(
        self,
        *,
        amount_decimal: float,
        payee_id: str,
        memo: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSendPaymentResponse:
        """
        Sends funds from an agent controlled wallet to a payee.

        Args:
          amount_decimal: The amount to generate a checkout link for. For example, '10.00' for USD is
              $10.00 or '1.000000' USDCBASE is 1 USDC.

          payee_id: The id of the payee you want to send the funds to. This must have been created
              using the /payments/payees endpoint or via the Payman dashboard before sending.

          memo: A note or memo to associate with this payment.

          wallet_id: The ID of the specific wallet from which to send the funds. This is only
              required if the agent has access to multiple wallets (not the case by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._post(
            "/payments/send-payment",
            body=maybe_transform(
                {
                    "amount_decimal": amount_decimal,
                    "payee_id": payee_id,
                    "memo": memo,
                    "metadata": metadata,
                    "wallet_id": wallet_id,
                },
                payment_send_payment_params.PaymentSendPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSendPaymentResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    @overload
    async def create_payee(
        self,
        *,
        type: Literal["CRYPTO_ADDRESS"],
        address: str | NotGiven = NOT_GIVEN,
        chain: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.CryptoAddressPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          address: The cryptocurrency address to send funds to

          chain: The the blockchain to use for the transaction

          contact_details: Contact details for this payee

          currency: The the currency/token to use for the transaction

          name: The name you wish to associate with this payee for future lookups.

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_payee(
        self,
        *,
        type: Literal["PAYMAN_WALLET"],
        contact_details: payment_create_payee_params.PaymanWalletPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        payman_wallet: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          contact_details: Contact details for this payee

          name: The name you wish to associate with this payee for future lookups.

          payman_wallet: The Payman handle or the id of the receiver wallet

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_payee(
        self,
        *,
        type: Literal["TEST_RAILS"],
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          name: The name you wish to associate with this payee for future lookups.

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_payee(
        self,
        *,
        type: Literal["US_ACH"],
        account_holder_name: str | NotGiven = NOT_GIVEN,
        account_holder_type: Literal["individual", "business"] | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        account_type: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.UsachPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payee) for future payments to be sent to

        Args:
          type: The type of payee

          account_holder_name: The name of the account holder

          account_holder_type: The type of the account holder

          account_number: The bank account number for the account

          account_type: The type of account it is (checking or savings)

          contact_details: Contact details for this payee

          name: The name you wish to associate with this payee for future lookups.

          routing_number: The routing number of the bank

          tags: Any additional labels you wish to assign to this payee

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    async def create_payee(
        self,
        *,
        type: Literal["CRYPTO_ADDRESS"] | Literal["PAYMAN_WALLET"] | Literal["TEST_RAILS"] | Literal["US_ACH"],
        address: str | NotGiven = NOT_GIVEN,
        chain: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.CryptoAddressPayeeDescriptorContactDetails | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        payman_wallet: str | NotGiven = NOT_GIVEN,
        account_holder_name: str | NotGiven = NOT_GIVEN,
        account_holder_type: Literal["individual", "business"] | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        account_type: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._post(
            "/payments/payees",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "address": address,
                    "chain": chain,
                    "contact_details": contact_details,
                    "currency": currency,
                    "name": name,
                    "tags": tags,
                    "payman_wallet": payman_wallet,
                    "account_holder_name": account_holder_name,
                    "account_holder_type": account_holder_type,
                    "account_number": account_number,
                    "account_type": account_type,
                    "routing_number": routing_number,
                },
                payment_create_payee_params.PaymentCreatePayeeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreatePayeeResponse,
        )

    async def delete_payee(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentDeletePayeeResponse:
        """
        Delete a payee (aka payee)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._delete(
            f"/payments/payees/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentDeletePayeeResponse,
        )

    async def search_payees(
        self,
        *,
        account_number: str | NotGiven = NOT_GIVEN,
        agent_reference: str | NotGiven = NOT_GIVEN,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone_number: str | NotGiven = NOT_GIVEN,
        contact_tax_id: str | NotGiven = NOT_GIVEN,
        crypto_address: str | NotGiven = NOT_GIVEN,
        crypto_chain: str | NotGiven = NOT_GIVEN,
        crypto_currency: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSearchPayeesResponse:
        """Searches existing payee for potential matches.

        Additional confirmation from the
        user is required to verify the correct payee is selected.

        Args:
          account_number: The US Bank account number to search for.

          agent_reference: The Payman agent reference (id or handle) to search for.

          contact_email: The contact email to search for.

          contact_phone_number: The contact phone number to search for.

          contact_tax_id: The contact tax id to search for.

          crypto_address: The crypto address to search for.

          crypto_chain: The crypto chain to search for.

          crypto_currency: The crypto currency to search for.

          name: The name of the payee to search for. This can be a partial, case-insensitive
              match.

          routing_number: The US Bank routing number to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._get(
            "/payments/search-payees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_number": account_number,
                        "agent_reference": agent_reference,
                        "contact_email": contact_email,
                        "contact_phone_number": contact_phone_number,
                        "contact_tax_id": contact_tax_id,
                        "crypto_address": crypto_address,
                        "crypto_chain": crypto_chain,
                        "crypto_currency": crypto_currency,
                        "name": name,
                        "routing_number": routing_number,
                    },
                    payment_search_payees_params.PaymentSearchPayeesParams,
                ),
            ),
            cast_to=PaymentSearchPayeesResponse,
        )

    async def send_payment(
        self,
        *,
        amount_decimal: float,
        payee_id: str,
        memo: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSendPaymentResponse:
        """
        Sends funds from an agent controlled wallet to a payee.

        Args:
          amount_decimal: The amount to generate a checkout link for. For example, '10.00' for USD is
              $10.00 or '1.000000' USDCBASE is 1 USDC.

          payee_id: The id of the payee you want to send the funds to. This must have been created
              using the /payments/payees endpoint or via the Payman dashboard before sending.

          memo: A note or memo to associate with this payment.

          wallet_id: The ID of the specific wallet from which to send the funds. This is only
              required if the agent has access to multiple wallets (not the case by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._post(
            "/payments/send-payment",
            body=await async_maybe_transform(
                {
                    "amount_decimal": amount_decimal,
                    "payee_id": payee_id,
                    "memo": memo,
                    "metadata": metadata,
                    "wallet_id": wallet_id,
                },
                payment_send_payment_params.PaymentSendPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSendPaymentResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create_payee = to_raw_response_wrapper(
            payments.create_payee,
        )
        self.delete_payee = to_raw_response_wrapper(
            payments.delete_payee,
        )
        self.search_payees = to_raw_response_wrapper(
            payments.search_payees,
        )
        self.send_payment = to_raw_response_wrapper(
            payments.send_payment,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create_payee = async_to_raw_response_wrapper(
            payments.create_payee,
        )
        self.delete_payee = async_to_raw_response_wrapper(
            payments.delete_payee,
        )
        self.search_payees = async_to_raw_response_wrapper(
            payments.search_payees,
        )
        self.send_payment = async_to_raw_response_wrapper(
            payments.send_payment,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.create_payee = to_streamed_response_wrapper(
            payments.create_payee,
        )
        self.delete_payee = to_streamed_response_wrapper(
            payments.delete_payee,
        )
        self.search_payees = to_streamed_response_wrapper(
            payments.search_payees,
        )
        self.send_payment = to_streamed_response_wrapper(
            payments.send_payment,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.create_payee = async_to_streamed_response_wrapper(
            payments.create_payee,
        )
        self.delete_payee = async_to_streamed_response_wrapper(
            payments.delete_payee,
        )
        self.search_payees = async_to_streamed_response_wrapper(
            payments.search_payees,
        )
        self.send_payment = async_to_streamed_response_wrapper(
            payments.send_payment,
        )
