# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import PaymentInitiateCustomerDepositResponse

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
            currency_code="currencyCode",
            email="email",
            fee_mode="INCLUDED_IN_AMOUNT",
            metadata={"foo": "string"},
            name="name",
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
            currency_code="currencyCode",
            email="email",
            fee_mode="INCLUDED_IN_AMOUNT",
            metadata={"foo": "string"},
            name="name",
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
