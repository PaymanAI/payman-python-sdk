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
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_payee_overload_1(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="CRYPTO_ADDRESS",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_method_create_payee_with_all_params_overload_1(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="CRYPTO_ADDRESS",
            address="address",
            chain="chain",
            contact_details={
                "address": {
                    "address_line1": "addressLine1",
                    "address_line2": "addressLine2",
                    "address_line3": "addressLine3",
                    "address_line4": "addressLine4",
                    "country": "country",
                    "locality": "locality",
                    "postcode": "postcode",
                    "region": "region",
                },
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            currency="currency",
            name="name",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create_payee_overload_1(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.create_payee(
            type="CRYPTO_ADDRESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_payee_overload_1(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.create_payee(
            type="CRYPTO_ADDRESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_payee_overload_2(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="PAYMAN_WALLET",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_method_create_payee_with_all_params_overload_2(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="PAYMAN_WALLET",
            contact_details={
                "address": {
                    "address_line1": "addressLine1",
                    "address_line2": "addressLine2",
                    "address_line3": "addressLine3",
                    "address_line4": "addressLine4",
                    "country": "country",
                    "locality": "locality",
                    "postcode": "postcode",
                    "region": "region",
                },
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            name="name",
            payman_wallet="paymanWallet",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create_payee_overload_2(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.create_payee(
            type="PAYMAN_WALLET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_payee_overload_2(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.create_payee(
            type="PAYMAN_WALLET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_payee_overload_3(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="TEST_RAILS",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_method_create_payee_with_all_params_overload_3(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="TEST_RAILS",
            name="name",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create_payee_overload_3(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.create_payee(
            type="TEST_RAILS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_payee_overload_3(self, client: Paymanai) -> None:
        with client.payments.with_streaming_response.create_payee(
            type="TEST_RAILS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_payee_overload_4(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="US_ACH",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_method_create_payee_with_all_params_overload_4(self, client: Paymanai) -> None:
        payment = client.payments.create_payee(
            type="US_ACH",
            account_holder_name="accountHolderName",
            account_holder_type="individual",
            account_number="accountNumber",
            account_type="accountType",
            contact_details={
                "address": {
                    "address_line1": "addressLine1",
                    "address_line2": "addressLine2",
                    "address_line3": "addressLine3",
                    "address_line4": "addressLine4",
                    "country": "country",
                    "locality": "locality",
                    "postcode": "postcode",
                    "region": "region",
                },
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
    def test_raw_response_create_payee_overload_4(self, client: Paymanai) -> None:
        response = client.payments.with_raw_response.create_payee(
            type="US_ACH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create_payee_overload_4(self, client: Paymanai) -> None:
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
            crypto_address="cryptoAddress",
            crypto_chain="cryptoChain",
            crypto_currency="cryptoCurrency",
            name="name",
            routing_number="routingNumber",
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
    async def test_method_create_payee_overload_1(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="CRYPTO_ADDRESS",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_payee_with_all_params_overload_1(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="CRYPTO_ADDRESS",
            address="address",
            chain="chain",
            contact_details={
                "address": {
                    "address_line1": "addressLine1",
                    "address_line2": "addressLine2",
                    "address_line3": "addressLine3",
                    "address_line4": "addressLine4",
                    "country": "country",
                    "locality": "locality",
                    "postcode": "postcode",
                    "region": "region",
                },
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            currency="currency",
            name="name",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create_payee_overload_1(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.create_payee(
            type="CRYPTO_ADDRESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_payee_overload_1(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.create_payee(
            type="CRYPTO_ADDRESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_payee_overload_2(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="PAYMAN_WALLET",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_payee_with_all_params_overload_2(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="PAYMAN_WALLET",
            contact_details={
                "address": {
                    "address_line1": "addressLine1",
                    "address_line2": "addressLine2",
                    "address_line3": "addressLine3",
                    "address_line4": "addressLine4",
                    "country": "country",
                    "locality": "locality",
                    "postcode": "postcode",
                    "region": "region",
                },
                "email": "email",
                "phone_number": "phoneNumber",
                "tax_id": "taxId",
            },
            name="name",
            payman_wallet="paymanWallet",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create_payee_overload_2(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.create_payee(
            type="PAYMAN_WALLET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_payee_overload_2(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.create_payee(
            type="PAYMAN_WALLET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_payee_overload_3(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="TEST_RAILS",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_payee_with_all_params_overload_3(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="TEST_RAILS",
            name="name",
            tags=["string"],
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create_payee_overload_3(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.create_payee(
            type="TEST_RAILS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_payee_overload_3(self, async_client: AsyncPaymanai) -> None:
        async with async_client.payments.with_streaming_response.create_payee(
            type="TEST_RAILS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_payee_overload_4(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="US_ACH",
        )
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_payee_with_all_params_overload_4(self, async_client: AsyncPaymanai) -> None:
        payment = await async_client.payments.create_payee(
            type="US_ACH",
            account_holder_name="accountHolderName",
            account_holder_type="individual",
            account_number="accountNumber",
            account_type="accountType",
            contact_details={
                "address": {
                    "address_line1": "addressLine1",
                    "address_line2": "addressLine2",
                    "address_line3": "addressLine3",
                    "address_line4": "addressLine4",
                    "country": "country",
                    "locality": "locality",
                    "postcode": "postcode",
                    "region": "region",
                },
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
    async def test_raw_response_create_payee_overload_4(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.payments.with_raw_response.create_payee(
            type="US_ACH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreatePayeeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create_payee_overload_4(self, async_client: AsyncPaymanai) -> None:
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
            crypto_address="cryptoAddress",
            crypto_chain="cryptoChain",
            crypto_currency="cryptoCurrency",
            name="name",
            routing_number="routingNumber",
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
