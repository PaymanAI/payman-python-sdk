# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import (
    TaskListResponse,
    TaskCreateResponse,
    TaskUpdateResponse,
    TaskRetrieveResponse,
)
from paymanai._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Paymanai) -> None:
        task = client.tasks.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Paymanai) -> None:
        task = client.tasks.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
            category="MARKETING",
            deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            invite_emails=["string", "string", "string"],
            payout=0,
            payout_wallet_id="string",
            required_submissions=0,
            submission_policy="OPEN_SUBMISSIONS_ONE_PER_USER",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Paymanai) -> None:
        task = client.tasks.retrieve(
            "string",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Paymanai) -> None:
        task = client.tasks.update(
            "string",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.update(
            "string",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.update(
            "string",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskUpdateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.update(
                "",
                description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
                title="Proofread a legal document",
            )

    @parametrize
    def test_method_list(self, client: Paymanai) -> None:
        task = client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Paymanai) -> None:
        task = client.tasks.list(
            limit=0,
            page=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
            category="MARKETING",
            deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            invite_emails=["string", "string", "string"],
            payout=0,
            payout_wallet_id="string",
            required_submissions=0,
            submission_policy="OPEN_SUBMISSIONS_ONE_PER_USER",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.create(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            organization_id="string",
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.retrieve(
            "string",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.update(
            "string",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.update(
            "string",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskUpdateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.update(
            "string",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskUpdateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.update(
                "",
                description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
                title="Proofread a legal document",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.list(
            limit=0,
            page=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True
