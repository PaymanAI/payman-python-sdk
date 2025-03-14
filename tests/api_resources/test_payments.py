# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import PaymentSendPaymentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_send_payment(self, client: Paymanai) -> None:
        payment = client.payments.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_method_send_payment_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_send_payment(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_send_payment(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_send_payment(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_method_send_payment_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_send_payment(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_send_payment(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.send_payment(
            amount_decimal=0,
            payee_id="payeeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
