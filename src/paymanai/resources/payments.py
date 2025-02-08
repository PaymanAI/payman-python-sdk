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
        contact_details: payment_create_payee_params.CryptoAddressPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
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
        Create a new payee (aka payment destination) for future payments to be sent to

        Args:
          type: The type of payment destination

          address: The cryptocurrency address to send funds to

          contact_details: Contact details for this payment destination

          currency: The the blockchain to use for the transaction

          customer_id: The ID of your customer who owns this payment destination. This is optional
              unless you are using the Account API, in which case it is required.

          name: The name you wish to associate with this payment destination for future lookups.

          tags: Any additional labels you wish to assign to this payment destination

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
        type: Literal["PAYMAN_AGENT"],
        contact_details: payment_create_payee_params.PaymanAgentPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        payman_agent_id: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payment destination) for future payments to be sent to

        Args:
          type: The type of payment destination

          contact_details: Contact details for this payment destination

          name: The name you wish to associate with this payment destination for future lookups.

          payman_agent_id: The Payman unique id assigned to the receiver agent

          tags: Any additional labels you wish to assign to this payment destination

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
        contact_details: payment_create_payee_params.UsachPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
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
        Create a new payee (aka payment destination) for future payments to be sent to

        Args:
          type: The type of payment destination

          account_holder_name: The name of the account holder

          account_holder_type: The type of the account holder

          account_number: The bank account number for the account

          account_type: The type of account it is (checking or savings)

          contact_details: Contact details for this payment destination

          customer_id: The ID of your customer who owns this payment destination. This is optional
              unless you are using the Account API, in which case it is required.

          name: The name you wish to associate with this payment destination for future lookups.

          routing_number: The routing number of the bank

          tags: Any additional labels you wish to assign to this payment destination

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
        type: Literal["CRYPTO_ADDRESS"] | Literal["PAYMAN_AGENT"] | Literal["US_ACH"],
        address: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.CryptoAddressPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        payman_agent_id: str | NotGiven = NOT_GIVEN,
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
            "/payments/destinations",
            body=maybe_transform(
                {
                    "type": type,
                    "address": address,
                    "contact_details": contact_details,
                    "currency": currency,
                    "customer_id": customer_id,
                    "name": name,
                    "tags": tags,
                    "payman_agent_id": payman_agent_id,
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

    def search_payees(
        self,
        *,
        account_number: str | NotGiven = NOT_GIVEN,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone_number: str | NotGiven = NOT_GIVEN,
        contact_tax_id: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSearchPayeesResponse:
        """Searches existing payee for potential matches.

        Additional confirmation from the
        user is required to verify the correct payment destination is selected.

        Args:
          account_number: The US Bank account number to search for.

          contact_email: The contact email to search for.

          contact_phone_number: The contact phone number to search for.

          contact_tax_id: The contact tax id to search for.

          customer_id: The ID of the customer who owns the payment destination. If the Account API is
              enabled, this is required to prevent unauthorized access to payment
              destinations.

          name: The name of the payment destination to search for. This can be a partial,
              case-insensitive match.

          routing_number: The US Bank routing number to search for.

          type: The type of destination to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._get(
            "/payments/search-destinations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_number": account_number,
                        "contact_email": contact_email,
                        "contact_phone_number": contact_phone_number,
                        "contact_tax_id": contact_tax_id,
                        "customer_id": customer_id,
                        "name": name,
                        "routing_number": routing_number,
                        "type": type,
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
        customer_email: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        customer_name: str | NotGiven = NOT_GIVEN,
        ignore_customer_spend_limits: bool | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        payment_destination: payment_send_payment_params.PaymentDestination | NotGiven = NOT_GIVEN,
        payment_destination_id: str | NotGiven = NOT_GIVEN,
        wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSendPaymentResponse:
        """
        Sends funds from an agent controlled wallet to a payment destination.

        Args:
          amount_decimal: The amount to generate a checkout link for. For example, '10.00' for USD is
              $10.00 or '1.000000' USDCBASE is 1 USDC.

          customer_email: An email address to associate with this customer.

          customer_id: The ID of the customer on whose behalf you're transferring funds. This can be
              any unique ID as held within your system. Providing this will limit the
              spendableamounts to what the customer has already deposited (unless
              ignoreCustomerSpendLimits is set to true).Note that if the Account API is
              enabled for your account, this field becomes mandatory to preventaccidental
              unauthorized transfers.

          customer_name: A name to associate with this customer.

          ignore_customer_spend_limits: By default Payman will limit spending on behalf of a customer to the amount they
              have deposited. If you wish to ignore this limit, set this to true. Note, if the
              Account API is enabled for your account, this field may not be used.

          memo: A note or memo to associate with this payment.

          payment_destination: A cryptocurrency address-based payment destination

          payment_destination_id: The id of the payment destination you want to send the funds to. This must have
              been created using the /payments/destinations endpoint or via the Payman
              dashboard before sending. Exactly one of paymentDestination and
              paymentDestinationId must be provided.

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
                    "customer_email": customer_email,
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "ignore_customer_spend_limits": ignore_customer_spend_limits,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_destination": payment_destination,
                    "payment_destination_id": payment_destination_id,
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
        contact_details: payment_create_payee_params.CryptoAddressPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
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
        Create a new payee (aka payment destination) for future payments to be sent to

        Args:
          type: The type of payment destination

          address: The cryptocurrency address to send funds to

          contact_details: Contact details for this payment destination

          currency: The the blockchain to use for the transaction

          customer_id: The ID of your customer who owns this payment destination. This is optional
              unless you are using the Account API, in which case it is required.

          name: The name you wish to associate with this payment destination for future lookups.

          tags: Any additional labels you wish to assign to this payment destination

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
        type: Literal["PAYMAN_AGENT"],
        contact_details: payment_create_payee_params.PaymanAgentPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        payman_agent_id: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreatePayeeResponse:
        """
        Create a new payee (aka payment destination) for future payments to be sent to

        Args:
          type: The type of payment destination

          contact_details: Contact details for this payment destination

          name: The name you wish to associate with this payment destination for future lookups.

          payman_agent_id: The Payman unique id assigned to the receiver agent

          tags: Any additional labels you wish to assign to this payment destination

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
        contact_details: payment_create_payee_params.UsachPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
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
        Create a new payee (aka payment destination) for future payments to be sent to

        Args:
          type: The type of payment destination

          account_holder_name: The name of the account holder

          account_holder_type: The type of the account holder

          account_number: The bank account number for the account

          account_type: The type of account it is (checking or savings)

          contact_details: Contact details for this payment destination

          customer_id: The ID of your customer who owns this payment destination. This is optional
              unless you are using the Account API, in which case it is required.

          name: The name you wish to associate with this payment destination for future lookups.

          routing_number: The routing number of the bank

          tags: Any additional labels you wish to assign to this payment destination

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
        type: Literal["CRYPTO_ADDRESS"] | Literal["PAYMAN_AGENT"] | Literal["US_ACH"],
        address: str | NotGiven = NOT_GIVEN,
        contact_details: payment_create_payee_params.CryptoAddressPaymentDestinationDescriptorContactDetails
        | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        payman_agent_id: str | NotGiven = NOT_GIVEN,
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
            "/payments/destinations",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "address": address,
                    "contact_details": contact_details,
                    "currency": currency,
                    "customer_id": customer_id,
                    "name": name,
                    "tags": tags,
                    "payman_agent_id": payman_agent_id,
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

    async def search_payees(
        self,
        *,
        account_number: str | NotGiven = NOT_GIVEN,
        contact_email: str | NotGiven = NOT_GIVEN,
        contact_phone_number: str | NotGiven = NOT_GIVEN,
        contact_tax_id: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSearchPayeesResponse:
        """Searches existing payee for potential matches.

        Additional confirmation from the
        user is required to verify the correct payment destination is selected.

        Args:
          account_number: The US Bank account number to search for.

          contact_email: The contact email to search for.

          contact_phone_number: The contact phone number to search for.

          contact_tax_id: The contact tax id to search for.

          customer_id: The ID of the customer who owns the payment destination. If the Account API is
              enabled, this is required to prevent unauthorized access to payment
              destinations.

          name: The name of the payment destination to search for. This can be a partial,
              case-insensitive match.

          routing_number: The US Bank routing number to search for.

          type: The type of destination to search for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._get(
            "/payments/search-destinations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_number": account_number,
                        "contact_email": contact_email,
                        "contact_phone_number": contact_phone_number,
                        "contact_tax_id": contact_tax_id,
                        "customer_id": customer_id,
                        "name": name,
                        "routing_number": routing_number,
                        "type": type,
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
        customer_email: str | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        customer_name: str | NotGiven = NOT_GIVEN,
        ignore_customer_spend_limits: bool | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        payment_destination: payment_send_payment_params.PaymentDestination | NotGiven = NOT_GIVEN,
        payment_destination_id: str | NotGiven = NOT_GIVEN,
        wallet_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSendPaymentResponse:
        """
        Sends funds from an agent controlled wallet to a payment destination.

        Args:
          amount_decimal: The amount to generate a checkout link for. For example, '10.00' for USD is
              $10.00 or '1.000000' USDCBASE is 1 USDC.

          customer_email: An email address to associate with this customer.

          customer_id: The ID of the customer on whose behalf you're transferring funds. This can be
              any unique ID as held within your system. Providing this will limit the
              spendableamounts to what the customer has already deposited (unless
              ignoreCustomerSpendLimits is set to true).Note that if the Account API is
              enabled for your account, this field becomes mandatory to preventaccidental
              unauthorized transfers.

          customer_name: A name to associate with this customer.

          ignore_customer_spend_limits: By default Payman will limit spending on behalf of a customer to the amount they
              have deposited. If you wish to ignore this limit, set this to true. Note, if the
              Account API is enabled for your account, this field may not be used.

          memo: A note or memo to associate with this payment.

          payment_destination: A cryptocurrency address-based payment destination

          payment_destination_id: The id of the payment destination you want to send the funds to. This must have
              been created using the /payments/destinations endpoint or via the Payman
              dashboard before sending. Exactly one of paymentDestination and
              paymentDestinationId must be provided.

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
                    "customer_email": customer_email,
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "ignore_customer_spend_limits": ignore_customer_spend_limits,
                    "memo": memo,
                    "metadata": metadata,
                    "payment_destination": payment_destination,
                    "payment_destination_id": payment_destination_id,
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
        self.search_payees = async_to_streamed_response_wrapper(
            payments.search_payees,
        )
        self.send_payment = async_to_streamed_response_wrapper(
            payments.send_payment,
        )
