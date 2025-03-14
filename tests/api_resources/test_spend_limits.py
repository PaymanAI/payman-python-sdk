# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from paymanai import Paymanai, AsyncPaymanai
from paymanai._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpendLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_spend_limits(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/spend-limits").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        spend_limit = client.spend_limits.get_spend_limits()
        assert spend_limit.is_closed
        assert spend_limit.json() == {"foo": "bar"}
        assert cast(Any, spend_limit.is_closed) is True
        assert isinstance(spend_limit, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_spend_limits(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/spend-limits").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        spend_limit = client.spend_limits.with_raw_response.get_spend_limits()

        assert spend_limit.is_closed is True
        assert spend_limit.http_request.headers.get("X-Stainless-Lang") == "python"
        assert spend_limit.json() == {"foo": "bar"}
        assert isinstance(spend_limit, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_spend_limits(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/spend-limits").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.spend_limits.with_streaming_response.get_spend_limits() as spend_limit:
            assert not spend_limit.is_closed
            assert spend_limit.http_request.headers.get("X-Stainless-Lang") == "python"

            assert spend_limit.json() == {"foo": "bar"}
            assert cast(Any, spend_limit.is_closed) is True
            assert isinstance(spend_limit, StreamedBinaryAPIResponse)

        assert cast(Any, spend_limit.is_closed) is True


class TestAsyncSpendLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_spend_limits(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/spend-limits").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        spend_limit = await async_client.spend_limits.get_spend_limits()
        assert spend_limit.is_closed
        assert await spend_limit.json() == {"foo": "bar"}
        assert cast(Any, spend_limit.is_closed) is True
        assert isinstance(spend_limit, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_spend_limits(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/spend-limits").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        spend_limit = await async_client.spend_limits.with_raw_response.get_spend_limits()

        assert spend_limit.is_closed is True
        assert spend_limit.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await spend_limit.json() == {"foo": "bar"}
        assert isinstance(spend_limit, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_spend_limits(
        self, async_client: AsyncPaymanai, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/spend-limits").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.spend_limits.with_streaming_response.get_spend_limits() as spend_limit:
            assert not spend_limit.is_closed
            assert spend_limit.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await spend_limit.json() == {"foo": "bar"}
            assert cast(Any, spend_limit.is_closed) is True
            assert isinstance(spend_limit, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, spend_limit.is_closed) is True
