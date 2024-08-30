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


class TestVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_server_version(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/version").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = client.version.get_server_version()
        assert version.is_closed
        assert version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_server_version(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/version").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        version = client.version.with_raw_response.get_server_version()

        assert version.is_closed is True
        assert version.http_request.headers.get("X-Stainless-Lang") == "python"
        assert version.json() == {"foo": "bar"}
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_server_version(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/version").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.version.with_streaming_response.get_server_version() as version:
            assert not version.is_closed
            assert version.http_request.headers.get("X-Stainless-Lang") == "python"

            assert version.json() == {"foo": "bar"}
            assert cast(Any, version.is_closed) is True
            assert isinstance(version, StreamedBinaryAPIResponse)

        assert cast(Any, version.is_closed) is True


class TestAsyncVersion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_server_version(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/version").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = await async_client.version.get_server_version()
        assert version.is_closed
        assert await version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_server_version(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/version").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        version = await async_client.version.with_raw_response.get_server_version()

        assert version.is_closed is True
        assert version.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await version.json() == {"foo": "bar"}
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_server_version(
        self, async_client: AsyncPaymanai, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/version").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.version.with_streaming_response.get_server_version() as version:
            assert not version.is_closed
            assert version.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await version.json() == {"foo": "bar"}
            assert cast(Any, version.is_closed) is True
            assert isinstance(version, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, version.is_closed) is True
