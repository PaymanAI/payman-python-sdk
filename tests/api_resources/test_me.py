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


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_me(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/me").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        me = client.me.me()
        assert me.is_closed
        assert me.json() == {"foo": "bar"}
        assert cast(Any, me.is_closed) is True
        assert isinstance(me, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_me(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/me").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        me = client.me.with_raw_response.me()

        assert me.is_closed is True
        assert me.http_request.headers.get("X-Stainless-Lang") == "python"
        assert me.json() == {"foo": "bar"}
        assert isinstance(me, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_me(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/me").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.me.with_streaming_response.me() as me:
            assert not me.is_closed
            assert me.http_request.headers.get("X-Stainless-Lang") == "python"

            assert me.json() == {"foo": "bar"}
            assert cast(Any, me.is_closed) is True
            assert isinstance(me, StreamedBinaryAPIResponse)

        assert cast(Any, me.is_closed) is True


class TestAsyncMe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_me(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/me").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        me = await async_client.me.me()
        assert me.is_closed
        assert await me.json() == {"foo": "bar"}
        assert cast(Any, me.is_closed) is True
        assert isinstance(me, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_me(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/me").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        me = await async_client.me.with_raw_response.me()

        assert me.is_closed is True
        assert me.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await me.json() == {"foo": "bar"}
        assert isinstance(me, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_me(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/me").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.me.with_streaming_response.me() as me:
            assert not me.is_closed
            assert me.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await me.json() == {"foo": "bar"}
            assert cast(Any, me.is_closed) is True
            assert isinstance(me, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, me.is_closed) is True
