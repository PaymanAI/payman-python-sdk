# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from paymanai import Paymanai, AsyncPaymanai

from paymanai.types.tasks import CategoryListTaskCategoriesResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_task_categories(self, client: Paymanai) -> None:
        category = client.tasks.categories.list_task_categories()
        assert_matches_type(CategoryListTaskCategoriesResponse, category, path=["response"])

    @parametrize
    def test_raw_response_list_task_categories(self, client: Paymanai) -> None:
        response = client.tasks.categories.with_raw_response.list_task_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListTaskCategoriesResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_list_task_categories(self, client: Paymanai) -> None:
        with client.tasks.categories.with_streaming_response.list_task_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListTaskCategoriesResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_task_categories(self, async_client: AsyncPaymanai) -> None:
        category = await async_client.tasks.categories.list_task_categories()
        assert_matches_type(CategoryListTaskCategoriesResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_list_task_categories(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.categories.with_raw_response.list_task_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListTaskCategoriesResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_list_task_categories(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.categories.with_streaming_response.list_task_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListTaskCategoriesResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True
