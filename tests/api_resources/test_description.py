# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import DescriptionGetAPIDescriptionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDescription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_api_description(self, client: Paymanai) -> None:
        description = client.description.get_api_description()
        assert_matches_type(DescriptionGetAPIDescriptionResponse, description, path=["response"])

    @parametrize
    def test_raw_response_get_api_description(self, client: Paymanai) -> None:
        response = client.description.with_raw_response.get_api_description()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = response.parse()
        assert_matches_type(DescriptionGetAPIDescriptionResponse, description, path=["response"])

    @parametrize
    def test_streaming_response_get_api_description(self, client: Paymanai) -> None:
        with client.description.with_streaming_response.get_api_description() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = response.parse()
            assert_matches_type(DescriptionGetAPIDescriptionResponse, description, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDescription:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_api_description(self, async_client: AsyncPaymanai) -> None:
        description = await async_client.description.get_api_description()
        assert_matches_type(DescriptionGetAPIDescriptionResponse, description, path=["response"])

    @parametrize
    async def test_raw_response_get_api_description(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.description.with_raw_response.get_api_description()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        description = await response.parse()
        assert_matches_type(DescriptionGetAPIDescriptionResponse, description, path=["response"])

    @parametrize
    async def test_streaming_response_get_api_description(self, async_client: AsyncPaymanai) -> None:
        async with async_client.description.with_streaming_response.get_api_description() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            description = await response.parse()
            assert_matches_type(DescriptionGetAPIDescriptionResponse, description, path=["response"])

        assert cast(Any, response.is_closed) is True
