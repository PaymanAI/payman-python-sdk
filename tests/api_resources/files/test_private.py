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


class TestPrivate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/private/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        private = client.files.private.download(
            key="string",
        )
        assert private.is_closed
        assert private.json() == {"foo": "bar"}
        assert cast(Any, private.is_closed) is True
        assert isinstance(private, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/private/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        private = client.files.private.with_raw_response.download(
            key="string",
        )

        assert private.is_closed is True
        assert private.http_request.headers.get("X-Stainless-Lang") == "python"
        assert private.json() == {"foo": "bar"}
        assert isinstance(private, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/private/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.files.private.with_streaming_response.download(
            key="string",
        ) as private:
            assert not private.is_closed
            assert private.http_request.headers.get("X-Stainless-Lang") == "python"

            assert private.json() == {"foo": "bar"}
            assert cast(Any, private.is_closed) is True
            assert isinstance(private, StreamedBinaryAPIResponse)

        assert cast(Any, private.is_closed) is True


class TestAsyncPrivate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/private/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        private = await async_client.files.private.download(
            key="string",
        )
        assert private.is_closed
        assert await private.json() == {"foo": "bar"}
        assert cast(Any, private.is_closed) is True
        assert isinstance(private, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/private/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        private = await async_client.files.private.with_raw_response.download(
            key="string",
        )

        assert private.is_closed is True
        assert private.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await private.json() == {"foo": "bar"}
        assert isinstance(private, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/private/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.files.private.with_streaming_response.download(
            key="string",
        ) as private:
            assert not private.is_closed
            assert private.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await private.json() == {"foo": "bar"}
            assert cast(Any, private.is_closed) is True
            assert isinstance(private, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, private.is_closed) is True
