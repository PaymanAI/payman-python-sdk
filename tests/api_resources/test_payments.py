# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import (
    PaymentCreatePayeeResponse,
    PaymentDeletePayeeResponse,
    PaymentSendPaymentResponse,
    PaymentSearchPayeesResponse,
    PaymentGetDepositLinkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_payee_overload_1(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="PAYMAN_AGENT",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_method_create_payee_with_all_params_overload_1(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="PAYMAN_AGENT",
            contact_details={
                "address": "address",
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            name="name",
            payman_agent="paymanAgent",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create_payee_overload_1(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.create_payee(
            type="PAYMAN_AGENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_payee_overload_1(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.create_payee(
            type="PAYMAN_AGENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_payee_overload_2(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="US_ACH",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_method_create_payee_with_all_params_overload_2(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="US_ACH",
            account_holder_name="accountHolderName",
            account_holder_type="individual",
            account_number="accountNumber",
            account_type="accountType",
            contact_details={
                "address": "address",
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            name="name",
            routing_number="routingNumber",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create_payee_overload_2(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.create_payee(
            type="US_ACH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_payee_overload_2(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.create_payee(
            type="US_ACH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_payee(self, client: Paymanai) -> None:
        payment = client.payments.delete_payee(
            "id",
        )
        assert_matches_type(PaymentDeletePayeeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_delete_payee(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.delete_payee(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentDeletePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_delete_payee(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.delete_payee(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentDeletePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_payee(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.delete_payee(
                "",
            )

    @parametrize
    def test_method_get_deposit_link(self, client: Paymanai) -> None:
        payment = client.payments.get_deposit_link(
            amount_decimal=0,
        )
        assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

    @parametrize
    def test_method_get_deposit_link_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.get_deposit_link(
            amount_decimal=0,
            fee_mode="INCLUDED_IN_AMOUNT",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_get_deposit_link(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.get_deposit_link(
            amount_decimal=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_get_deposit_link(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.get_deposit_link(
            amount_decimal=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_payees(self, client: Paymanai) -> None:
        payment = client.payments.search_payees()
        assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

    @parametrize
    def test_method_search_payees_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.search_payees(
            account_number="accountNumber",
            agent_reference="agentReference",
            contact_email="contactEmail",
            contact_phone_number="contactPhoneNumber",
            contact_tax_id="contactTaxId",
            name="name",
            routing_number="routingNumber",
            type="type",
        )
        assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_search_payees(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.search_payees()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_search_payees(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.search_payees() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_payment(self, client: Paymanai) -> None:
        payment = client.payments.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_method_send_payment_with_all_params(self, client: Paymanai) -> None:
        payment = client.payments.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_send_payment(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_send_payment(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_payee_overload_1(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="PAYMAN_AGENT",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_payee_with_all_params_overload_1(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="PAYMAN_AGENT",
            contact_details={
                "address": "address",
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            name="name",
            payman_agent="paymanAgent",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create_payee_overload_1(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.create_payee(
            type="PAYMAN_AGENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_payee_overload_1(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.create_payee(
            type="PAYMAN_AGENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_payee_overload_2(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="US_ACH",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_payee_with_all_params_overload_2(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="US_ACH",
            account_holder_name="accountHolderName",
            account_holder_type="individual",
            account_number="accountNumber",
            account_type="accountType",
            contact_details={
                "address": "address",
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            name="name",
            routing_number="routingNumber",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create_payee_overload_2(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.create_payee(
            type="US_ACH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_payee_overload_2(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.create_payee(
            type="US_ACH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_payee(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.delete_payee(
            "id",
        )
        assert_matches_type(PaymentDeletePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_delete_payee(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.delete_payee(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentDeletePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_delete_payee(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.delete_payee(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentDeletePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_payee(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.delete_payee(
                "",
            )

    @parametrize
    async def test_method_get_deposit_link(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.get_deposit_link(
            amount_decimal=0,
        )
        assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

    @parametrize
    async def test_method_get_deposit_link_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.get_deposit_link(
            amount_decimal=0,
            fee_mode="INCLUDED_IN_AMOUNT",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_get_deposit_link(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.get_deposit_link(
            amount_decimal=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_get_deposit_link(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.get_deposit_link(
            amount_decimal=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentGetDepositLinkResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_payees(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.search_payees()
        assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

    @parametrize
    async def test_method_search_payees_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.search_payees(
            account_number="accountNumber",
            agent_reference="agentReference",
            contact_email="contactEmail",
            contact_phone_number="contactPhoneNumber",
            contact_tax_id="contactTaxId",
            name="name",
            routing_number="routingNumber",
            type="type",
        )
        assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_search_payees(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.search_payees()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_search_payees(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.search_payees() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSearchPayeesResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_payment(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_method_send_payment_with_all_params(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
            memo="memo",
            metadata={"foo": "bar"},
            wallet_id="walletId",
        )
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_send_payment(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_send_payment(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.send_payment(
            amount_decimal=0,
            payment_destination_id="paymentDestinationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSendPaymentResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
