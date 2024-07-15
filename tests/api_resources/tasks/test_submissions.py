# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai.types.tasks import SubmissionListTaskSubmissionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubmissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_task_submissions(self, client: Paymanai) -> None:
        submission = client.tasks.submissions.list_task_submissions(
            id="id",
        )
        assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

    @parametrize
    def test_method_list_task_submissions_with_all_params(self, client: Paymanai) -> None:
        submission = client.tasks.submissions.list_task_submissions(
            id="id",
            limit=0,
            page=0,
            statuses=["PENDING"],
        )
        assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

    @parametrize
    def test_raw_response_list_task_submissions(self, client: Paymanai) -> None:
        response = client.tasks.submissions.with_raw_response.list_task_submissions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

    @parametrize
    def test_streaming_response_list_task_submissions(self, client: Paymanai) -> None:
        with client.tasks.submissions.with_streaming_response.list_task_submissions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_task_submissions(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.submissions.with_raw_response.list_task_submissions(
                id="",
            )


class TestAsyncSubmissions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_task_submissions(self, async_client: AsyncPaymanai) -> None:
        submission = await async_client.tasks.submissions.list_task_submissions(
            id="id",
        )
        assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

    @parametrize
    async def test_method_list_task_submissions_with_all_params(self, async_client: AsyncPaymanai) -> None:
        submission = await async_client.tasks.submissions.list_task_submissions(
            id="id",
            limit=0,
            page=0,
            statuses=["PENDING"],
        )
        assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

    @parametrize
    async def test_raw_response_list_task_submissions(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.submissions.with_raw_response.list_task_submissions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

    @parametrize
    async def test_streaming_response_list_task_submissions(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.submissions.with_streaming_response.list_task_submissions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(SubmissionListTaskSubmissionsResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_task_submissions(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.submissions.with_raw_response.list_task_submissions(
                id="",
            )
