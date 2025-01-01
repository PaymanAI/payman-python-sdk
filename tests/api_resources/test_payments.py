# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import (
    PaymentSendPaymentResponse,
    PaymentSearchDestinationsResponse,
    PaymentInitiateCustomerDepositResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_initiate_customer_deposit(self, client: Paymanai) -> None:
        payment = client.payments.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
        )
        assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

    @parametrize
    def test_method_initiate_customer_deposit_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
            customer_email="customerEmail",
            customer_name="customerName",
            fee_mode="INCLUDED_IN_AMOUNT",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_initiate_customer_deposit(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_initiate_customer_deposit(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_destinations(self, client: Paymanai) -> None:
        payment = client.payments.search_destinations()
        assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

    @parametrize
    def test_method_search_destinations_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.search_destinations(
            account_number="accountNumber",
            contact_email="contactEmail",
            contact_phone_number="contactPhoneNumber",
            contact_tax_id="contactTaxId",
            name="name",
            routing_number="routingNumber",
            type="type",
        )
        assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_search_destinations(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.search_destinations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_search_destinations(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.search_destinations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_payment(self, client: Paymanai) -> None:
        payment = client.payments.send_payment(
            amount_decimal=0,
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_method_send_payment_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.send_payment(
            amount_decimal=0,
            customer_email="customerEmail",
            customer_id="customerId",
            customer_name="customerName",
            ignore_customer_spend_limits=True,
            memo="memo",
            metadata={"foo": "bar"},
            payment_destination={
                "type": "CRYPTO_ADDRESS",
                "address": "address",
                "contact_details": {
                    "address": "address",
                    "contact_type": "individual",
                    "email": "email",
                    "phone_number": "phoneNumber",
                    "tax_id": "taxId",
                },
                "currency": "currency",
                "name": "name",
                "tags": ["string"],
            },
            payment_destination_id="paymentDestinationId",
            wallet_id="walletId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_send_payment(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.send_payment(
            amount_decimal=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_send_payment(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.send_payment(
            amount_decimal=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_initiate_customer_deposit(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
        )
        assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

    @parametrize
    async def test_method_initiate_customer_deposit_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
            customer_email="customerEmail",
            customer_name="customerName",
            fee_mode="INCLUDED_IN_AMOUNT",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_initiate_customer_deposit(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_initiate_customer_deposit(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.initiate_customer_deposit(
            amount_decimal=0,
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentInitiateCustomerDepositResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_destinations(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.search_destinations()
        assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

    @parametrize
    async def test_method_search_destinations_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.search_destinations(
            account_number="accountNumber",
            contact_email="contactEmail",
            contact_phone_number="contactPhoneNumber",
            contact_tax_id="contactTaxId",
            name="name",
            routing_number="routingNumber",
            type="type",
        )
        assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_search_destinations(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.search_destinations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_search_destinations(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.search_destinations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSearchDestinationsResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_payment(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.send_payment(
            amount_decimal=0,
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_method_send_payment_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.send_payment(
            amount_decimal=0,
            customer_email="customerEmail",
            customer_id="customerId",
            customer_name="customerName",
            ignore_customer_spend_limits=True,
            memo="memo",
            metadata={"foo": "bar"},
            payment_destination={
                "type": "CRYPTO_ADDRESS",
                "address": "address",
                "contact_details": {
                    "address": "address",
                    "contact_type": "individual",
                    "email": "email",
                    "phone_number": "phoneNumber",
                    "tax_id": "taxId",
                },
                "currency": "currency",
                "name": "name",
                "tags": ["string"],
            },
            payment_destination_id="paymentDestinationId",
            wallet_id="walletId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_send_payment(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.send_payment(
            amount_decimal=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_send_payment(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.send_payment(
            amount_decimal=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
