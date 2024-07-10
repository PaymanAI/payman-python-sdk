# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from paymanai import Paymanai, AsyncPaymanai
from tests.utils import assert_matches_type
from paymanai._utils import parse_datetime
from paymanai.types.tasks import (
    AssignmentListTaskAssignmentsResponse,
    AssignmentCreateTaskAssignmentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_task_assignment(self, client: Paymanai) -> None:
        assignment = client.tasks.assignments.create_task_assignment(
            "string",
        )
        assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

    @parametrize
    def test_method_create_task_assignment_with_all_params(self, client: Paymanai) -> None:
        assignment = client.tasks.assignments.create_task_assignment(
            "string",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            invite_email="string",
        )
        assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

    @parametrize
    def test_raw_response_create_task_assignment(self, client: Paymanai) -> None:
        response = client.tasks.assignments.with_raw_response.create_task_assignment(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = response.parse()
        assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

    @parametrize
    def test_streaming_response_create_task_assignment(self, client: Paymanai) -> None:
        with client.tasks.assignments.with_streaming_response.create_task_assignment(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = response.parse()
            assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_task_assignment(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.assignments.with_raw_response.create_task_assignment(
                "",
            )

    @parametrize
    def test_method_list_task_assignments(self, client: Paymanai) -> None:
        assignment = client.tasks.assignments.list_task_assignments(
            "string",
        )
        assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

    @parametrize
    def test_method_list_task_assignments_with_all_params(self, client: Paymanai) -> None:
        assignment = client.tasks.assignments.list_task_assignments(
            "string",
            limit=0,
            page=0,
            statuses=["IN_REVIEW"],
        )
        assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

    @parametrize
    def test_raw_response_list_task_assignments(self, client: Paymanai) -> None:
        response = client.tasks.assignments.with_raw_response.list_task_assignments(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = response.parse()
        assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

    @parametrize
    def test_streaming_response_list_task_assignments(self, client: Paymanai) -> None:
        with client.tasks.assignments.with_streaming_response.list_task_assignments(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = response.parse()
            assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_task_assignments(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tasks.assignments.with_raw_response.list_task_assignments(
                "",
            )


class TestAsyncAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_task_assignment(self, async_client: AsyncPaymanai) -> None:
        assignment = await async_client.tasks.assignments.create_task_assignment(
            "string",
        )
        assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

    @parametrize
    async def test_method_create_task_assignment_with_all_params(self, async_client: AsyncPaymanai) -> None:
        assignment = await async_client.tasks.assignments.create_task_assignment(
            "string",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            invite_email="string",
        )
        assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

    @parametrize
    async def test_raw_response_create_task_assignment(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.assignments.with_raw_response.create_task_assignment(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = await response.parse()
        assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

    @parametrize
    async def test_streaming_response_create_task_assignment(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.assignments.with_streaming_response.create_task_assignment(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = await response.parse()
            assert_matches_type(AssignmentCreateTaskAssignmentResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_task_assignment(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.assignments.with_raw_response.create_task_assignment(
                "",
            )

    @parametrize
    async def test_method_list_task_assignments(self, async_client: AsyncPaymanai) -> None:
        assignment = await async_client.tasks.assignments.list_task_assignments(
            "string",
        )
        assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

    @parametrize
    async def test_method_list_task_assignments_with_all_params(self, async_client: AsyncPaymanai) -> None:
        assignment = await async_client.tasks.assignments.list_task_assignments(
            "string",
            limit=0,
            page=0,
            statuses=["IN_REVIEW"],
        )
        assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

    @parametrize
    async def test_raw_response_list_task_assignments(self, async_client: AsyncPaymanai) -> None:
        response = await async_client.tasks.assignments.with_raw_response.list_task_assignments(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = await response.parse()
        assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

    @parametrize
    async def test_streaming_response_list_task_assignments(self, async_client: AsyncPaymanai) -> None:
        async with async_client.tasks.assignments.with_streaming_response.list_task_assignments(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = await response.parse()
            assert_matches_type(AssignmentListTaskAssignmentsResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_task_assignments(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tasks.assignments.with_raw_response.list_task_assignments(
                "",
            )
