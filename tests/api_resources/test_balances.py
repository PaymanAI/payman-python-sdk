# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import BalanceGetSpendableBalanceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_spendable_balance(self, client: Paymanai) -> None:
        balance = client.balances.get_spendable_balance(
            "currency",
        )
        assert_matches_type(BalanceGetSpendableBalanceResponse, balance, path=["response"])

    @parametrize
    def test_raw_response_get_spendable_balance(self, client: Paymanai) -> None:
        response = client.balances.with_raw_response.get_spendable_balance(
            "currency",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceGetSpendableBalanceResponse, balance, path=["response"])

    @parametrize
    def test_streaming_response_get_spendable_balance(self, client: Paymanai) -> None:
        with client.balances.with_streaming_response.get_spendable_balance(
            "currency",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceGetSpendableBalanceResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_spendable_balance(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency` but received ''"):
            client.balances.with_raw_response.get_spendable_balance(
                "",
            )


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_spendable_balance(self, async_client: AsyncPaymanai) -> None:
        balance = await async_client.balances.get_spendable_balance(
            "currency",
        )
        assert_matches_type(BalanceGetSpendableBalanceResponse, balance, path=["response"])

    @parametrize
    async def test_raw_response_get_spendable_balance(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.balances.with_raw_response.get_spendable_balance(
            "currency",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceGetSpendableBalanceResponse, balance, path=["response"])

    @parametrize
    async def test_streaming_response_get_spendable_balance(self, async_client: AsyncPaymanai) -> None:
        async with async_client.balances.with_streaming_response.get_spendable_balance(
            "currency",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceGetSpendableBalanceResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_spendable_balance(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency` but received ''"):
            await async_client.balances.with_raw_response.get_spendable_balance(
                "",
            )
