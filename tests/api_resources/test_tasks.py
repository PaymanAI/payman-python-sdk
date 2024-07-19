# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from paymanai import Paymanai, AsyncPaymanai

from paymanai.types import TaskCreateTaskResponse, TaskGetTaskResponse, TaskListTasksResponse, TaskUpdateTaskResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types import task_create_task_params
from paymanai.types import task_list_tasks_params
from paymanai.types import task_update_task_params
from paymanai._utils import parse_datetime
from paymanai._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_task(self, client: Paymanai) -> None:
        task = client.tasks.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
        )
        assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

    @parametrize
    def test_method_create_task_with_all_params(self, client: Paymanai) -> None:
        task = client.tasks.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
            category="MARKETING",
            deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            invite_emails=["string", "string", "string"],
            payout_wallet_id="payoutWalletId",
            required_submissions=0,
            submission_policy="OPEN_SUBMISSIONS_ONE_PER_USER",
        )
        assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create_task(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create_task(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_task(self, client: Paymanai) -> None:
        task = client.tasks.get_task(
            "id",
        )
        assert_matches_type(TaskGetTaskResponse, task, path=["response"])

    @parametrize
    def test_raw_response_get_task(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.get_task(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskGetTaskResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_get_task(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.get_task(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskGetTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_task(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.get_task(
                "",
            )

    @parametrize
    def test_method_list_tasks(self, client: Paymanai) -> None:
        task = client.tasks.list_tasks()
        assert_matches_type(TaskListTasksResponse, task, path=["response"])

    @parametrize
    def test_method_list_tasks_with_all_params(self, client: Paymanai) -> None:
        task = client.tasks.list_tasks(
            limit=0,
            page=0,
        )
        assert_matches_type(TaskListTasksResponse, task, path=["response"])

    @parametrize
    def test_raw_response_list_tasks(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.list_tasks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListTasksResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_list_tasks(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.list_tasks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListTasksResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_task(self, client: Paymanai) -> None:
        task = client.tasks.update_task(
            id="id",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )
        assert_matches_type(TaskUpdateTaskResponse, task, path=["response"])

    @parametrize
    def test_raw_response_update_task(self, client: Paymanai) -> None:
        response = client.tasks.with_raw_response.update_task(
            id="id",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskUpdateTaskResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_update_task(self, client: Paymanai) -> None:
        with client.tasks.with_streaming_response.update_task(
            id="id",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskUpdateTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_task(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.with_raw_response.update_task(
                id="",
                description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
                title="Proofread a legal document",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_task(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
        )
        assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

    @parametrize
    async def test_method_create_task_with_all_params(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
            category="MARKETING",
            deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            invite_emails=["string", "string", "string"],
            payout_wallet_id="payoutWalletId",
            required_submissions=0,
            submission_policy="OPEN_SUBMISSIONS_ONE_PER_USER",
        )
        assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create_task(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create_task(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.create_task(
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            payout=0,
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_task(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.get_task(
            "id",
        )
        assert_matches_type(TaskGetTaskResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_get_task(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.get_task(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskGetTaskResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_get_task(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.get_task(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskGetTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_task(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.get_task(
                "",
            )

    @parametrize
    async def test_method_list_tasks(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.list_tasks()
        assert_matches_type(TaskListTasksResponse, task, path=["response"])

    @parametrize
    async def test_method_list_tasks_with_all_params(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.list_tasks(
            limit=0,
            page=0,
        )
        assert_matches_type(TaskListTasksResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_list_tasks(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.list_tasks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListTasksResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_list_tasks(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.list_tasks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListTasksResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_task(self, async_client: AsyncPaymanai) -> None:
        task = await async_client.tasks.update_task(
            id="id",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )
        assert_matches_type(TaskUpdateTaskResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_update_task(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.with_raw_response.update_task(
            id="id",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskUpdateTaskResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_update_task(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.with_streaming_response.update_task(
            id="id",
            description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
            title="Proofread a legal document",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskUpdateTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_task(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.with_raw_response.update_task(
                id="",
                description="Proofread a 10-page legal document for spelling and grammar errors.  Please include a summary of changes or a confirmation that no errors were found.",
                title="Proofread a legal document",
            )
