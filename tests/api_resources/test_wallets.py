# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import WalletGetWalletResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_wallet(self, client: Paymanai) -> None:
        wallet = client.wallets.get_wallet(
            "id",
        )
        assert_matches_type(WalletGetWalletResponse, wallet, path=["response"])

    @parametrize
    def test_raw_response_get_wallet(self, client: Paymanai) -> None:
        response = client.wallets.with_raw_response.get_wallet(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletGetWalletResponse, wallet, path=["response"])

    @parametrize
    def test_streaming_response_get_wallet(self, client: Paymanai) -> None:
        with client.wallets.with_streaming_response.get_wallet(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletGetWalletResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_wallet(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wallets.with_raw_response.get_wallet(
                "",
            )


class TestAsyncWallets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_wallet(self, async_client: AsyncPaymanai) -> None:
        wallet = await async_client.wallets.get_wallet(
            "id",
        )
        assert_matches_type(WalletGetWalletResponse, wallet, path=["response"])

    @parametrize
    async def test_raw_response_get_wallet(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.wallets.with_raw_response.get_wallet(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletGetWalletResponse, wallet, path=["response"])

    @parametrize
    async def test_streaming_response_get_wallet(self, async_client: AsyncPaymanai) -> None:
        async with async_client.wallets.with_streaming_response.get_wallet(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletGetWalletResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_wallet(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wallets.with_raw_response.get_wallet(
                "",
            )
