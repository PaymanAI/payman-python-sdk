# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import task_list_tasks_params, task_create_task_params, task_update_task_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .assignments import (
    AssignmentsResource,
    AsyncAssignmentsResource,
    AssignmentsResourceWithRawResponse,
    AsyncAssignmentsResourceWithRawResponse,
    AssignmentsResourceWithStreamingResponse,
    AsyncAssignmentsResourceWithStreamingResponse,
)
from .submissions import (
    SubmissionsResource,
    AsyncSubmissionsResource,
    SubmissionsResourceWithRawResponse,
    AsyncSubmissionsResourceWithRawResponse,
    SubmissionsResourceWithStreamingResponse,
    AsyncSubmissionsResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from ...types.task_get_task_response import TaskGetTaskResponse
from ...types.task_list_tasks_response import TaskListTasksResponse
from ...types.task_create_task_response import TaskCreateTaskResponse
from ...types.task_update_task_response import TaskUpdateTaskResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def assignments(self) -> AssignmentsResource:
        return AssignmentsResource(self._client)

    @cached_property
    def submissions(self) -> SubmissionsResource:
        return SubmissionsResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self)

    def create_task(
        self,
        *,
        description: str,
        organization_id: str,
        title: str,
        category: Literal[
            "MARKETING",
            "ENGINEERING",
            "SALES",
            "DATA_ANALYTICS",
            "DESIGN",
            "PRODUCT_MANAGEMENT",
            "LEGAL",
            "MEDICAL",
            "FINANCE",
            "OTHER",
        ]
        | NotGiven = NOT_GIVEN,
        deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invite_emails: List[str] | NotGiven = NOT_GIVEN,
        payout: int | NotGiven = NOT_GIVEN,
        payout_wallet_id: str | NotGiven = NOT_GIVEN,
        required_submissions: int | NotGiven = NOT_GIVEN,
        submission_policy: Literal[
            "OPEN_SUBMISSIONS_ONE_PER_USER",
            "OPEN_SUBMISSIONS_MANY_PER_USER",
            "PRE_ASSIGNED_SUBMISSIONS",
            "OPEN_ASSIGNED_SUBMISSIONS",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateTaskResponse:
        """Creates a new task

        Args:
          description: A detailed description of the task.

        This should include enough information for
              the user to complete the task to the expected standard.

          organization_id: The unique identifier for the organization that owns this task

          title: A descriptive title for this task

          category: The task category this task should be shown under. Defaults to 'OTHER' if
              omitted.

          deadline: The deadline for this task. If this is set, the task will be closed after this
              time regardless of the number of submissions received and approved. If unset,
              the task will remain open until the required number of submissions are received
              and approved.

          invite_emails: List of email addresses to invite to complete the task. If this is set, only
              users with these emails will be able to complete the task.

          payout: The amount being offered for each approved submission on this task. Note the
              amount is denominated in base units of the currency, so a payout of 100 in USD
              would mean the payout would be $1.00. Defaults to 0.

          payout_wallet_id: The ID of the wallet to be used to pay out rewards for this task. This wallet
              must be owned by the organization that owns this task, the agent creating the
              task must have access to the wallet, it must have sufficient funds to cover the
              payouts, and must be in the same currency as the currency of this task.

          required_submissions: The number of approved submissions required before this task is closed. E.g. If
              this is set to 2, the task will be closed after the 2 submission are received
              and approved. Defaults to 1 if omitted (or the number of inviteEmails provided
              if present).

          submission_policy: The policy determining who may submit solutions for this task. Defaults to
              OPEN_SUBMISSIONS_ONE_PER_USER if omitted, or PRE_ASSIGNED_SUBMISSIONS if
              inviteEmails are specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._post(
            "/tasks",
            body=maybe_transform(
                {
                    "description": description,
                    "organization_id": organization_id,
                    "title": title,
                    "category": category,
                    "deadline": deadline,
                    "invite_emails": invite_emails,
                    "payout": payout,
                    "payout_wallet_id": payout_wallet_id,
                    "required_submissions": required_submissions,
                    "submission_policy": submission_policy,
                },
                task_create_task_params.TaskCreateTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateTaskResponse,
        )

    def get_task(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetTaskResponse:
        """
        Get a task by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._get(
            f"/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetTaskResponse,
        )

    def list_tasks(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListTasksResponse:
        """
        Get all tasks for the current organization

        Args:
          limit: The number of items per page

          page: The page number to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._get(
            "/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    task_list_tasks_params.TaskListTasksParams,
                ),
            ),
            cast_to=TaskListTasksResponse,
        )

    def update_task(
        self,
        id: str,
        *,
        description: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskUpdateTaskResponse:
        """
        Updates an existing task.

        Args:
          description: A detailed description of the task. This should include enough information for
              the user to complete the task to the expected standard.

          title: A descriptive title for this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._put(
            f"/tasks/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "title": title,
                },
                task_update_task_params.TaskUpdateTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUpdateTaskResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def assignments(self) -> AsyncAssignmentsResource:
        return AsyncAssignmentsResource(self._client)

    @cached_property
    def submissions(self) -> AsyncSubmissionsResource:
        return AsyncSubmissionsResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create_task(
        self,
        *,
        description: str,
        organization_id: str,
        title: str,
        category: Literal[
            "MARKETING",
            "ENGINEERING",
            "SALES",
            "DATA_ANALYTICS",
            "DESIGN",
            "PRODUCT_MANAGEMENT",
            "LEGAL",
            "MEDICAL",
            "FINANCE",
            "OTHER",
        ]
        | NotGiven = NOT_GIVEN,
        deadline: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invite_emails: List[str] | NotGiven = NOT_GIVEN,
        payout: int | NotGiven = NOT_GIVEN,
        payout_wallet_id: str | NotGiven = NOT_GIVEN,
        required_submissions: int | NotGiven = NOT_GIVEN,
        submission_policy: Literal[
            "OPEN_SUBMISSIONS_ONE_PER_USER",
            "OPEN_SUBMISSIONS_MANY_PER_USER",
            "PRE_ASSIGNED_SUBMISSIONS",
            "OPEN_ASSIGNED_SUBMISSIONS",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateTaskResponse:
        """Creates a new task

        Args:
          description: A detailed description of the task.

        This should include enough information for
              the user to complete the task to the expected standard.

          organization_id: The unique identifier for the organization that owns this task

          title: A descriptive title for this task

          category: The task category this task should be shown under. Defaults to 'OTHER' if
              omitted.

          deadline: The deadline for this task. If this is set, the task will be closed after this
              time regardless of the number of submissions received and approved. If unset,
              the task will remain open until the required number of submissions are received
              and approved.

          invite_emails: List of email addresses to invite to complete the task. If this is set, only
              users with these emails will be able to complete the task.

          payout: The amount being offered for each approved submission on this task. Note the
              amount is denominated in base units of the currency, so a payout of 100 in USD
              would mean the payout would be $1.00. Defaults to 0.

          payout_wallet_id: The ID of the wallet to be used to pay out rewards for this task. This wallet
              must be owned by the organization that owns this task, the agent creating the
              task must have access to the wallet, it must have sufficient funds to cover the
              payouts, and must be in the same currency as the currency of this task.

          required_submissions: The number of approved submissions required before this task is closed. E.g. If
              this is set to 2, the task will be closed after the 2 submission are received
              and approved. Defaults to 1 if omitted (or the number of inviteEmails provided
              if present).

          submission_policy: The policy determining who may submit solutions for this task. Defaults to
              OPEN_SUBMISSIONS_ONE_PER_USER if omitted, or PRE_ASSIGNED_SUBMISSIONS if
              inviteEmails are specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._post(
            "/tasks",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "organization_id": organization_id,
                    "title": title,
                    "category": category,
                    "deadline": deadline,
                    "invite_emails": invite_emails,
                    "payout": payout,
                    "payout_wallet_id": payout_wallet_id,
                    "required_submissions": required_submissions,
                    "submission_policy": submission_policy,
                },
                task_create_task_params.TaskCreateTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateTaskResponse,
        )

    async def get_task(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskGetTaskResponse:
        """
        Get a task by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._get(
            f"/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGetTaskResponse,
        )

    async def list_tasks(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListTasksResponse:
        """
        Get all tasks for the current organization

        Args:
          limit: The number of items per page

          page: The page number to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._get(
            "/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    task_list_tasks_params.TaskListTasksParams,
                ),
            ),
            cast_to=TaskListTasksResponse,
        )

    async def update_task(
        self,
        id: str,
        *,
        description: str,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskUpdateTaskResponse:
        """
        Updates an existing task.

        Args:
          description: A detailed description of the task. This should include enough information for
              the user to complete the task to the expected standard.

          title: A descriptive title for this task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._put(
            f"/tasks/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "title": title,
                },
                task_update_task_params.TaskUpdateTaskParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskUpdateTaskResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create_task = to_raw_response_wrapper(
            tasks.create_task,
        )
        self.get_task = to_raw_response_wrapper(
            tasks.get_task,
        )
        self.list_tasks = to_raw_response_wrapper(
            tasks.list_tasks,
        )
        self.update_task = to_raw_response_wrapper(
            tasks.update_task,
        )

    @cached_property
    def assignments(self) -> AssignmentsResourceWithRawResponse:
        return AssignmentsResourceWithRawResponse(self._tasks.assignments)

    @cached_property
    def submissions(self) -> SubmissionsResourceWithRawResponse:
        return SubmissionsResourceWithRawResponse(self._tasks.submissions)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._tasks.categories)


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create_task = async_to_raw_response_wrapper(
            tasks.create_task,
        )
        self.get_task = async_to_raw_response_wrapper(
            tasks.get_task,
        )
        self.list_tasks = async_to_raw_response_wrapper(
            tasks.list_tasks,
        )
        self.update_task = async_to_raw_response_wrapper(
            tasks.update_task,
        )

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithRawResponse:
        return AsyncAssignmentsResourceWithRawResponse(self._tasks.assignments)

    @cached_property
    def submissions(self) -> AsyncSubmissionsResourceWithRawResponse:
        return AsyncSubmissionsResourceWithRawResponse(self._tasks.submissions)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._tasks.categories)


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create_task = to_streamed_response_wrapper(
            tasks.create_task,
        )
        self.get_task = to_streamed_response_wrapper(
            tasks.get_task,
        )
        self.list_tasks = to_streamed_response_wrapper(
            tasks.list_tasks,
        )
        self.update_task = to_streamed_response_wrapper(
            tasks.update_task,
        )

    @cached_property
    def assignments(self) -> AssignmentsResourceWithStreamingResponse:
        return AssignmentsResourceWithStreamingResponse(self._tasks.assignments)

    @cached_property
    def submissions(self) -> SubmissionsResourceWithStreamingResponse:
        return SubmissionsResourceWithStreamingResponse(self._tasks.submissions)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._tasks.categories)


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create_task = async_to_streamed_response_wrapper(
            tasks.create_task,
        )
        self.get_task = async_to_streamed_response_wrapper(
            tasks.get_task,
        )
        self.list_tasks = async_to_streamed_response_wrapper(
            tasks.list_tasks,
        )
        self.update_task = async_to_streamed_response_wrapper(
            tasks.update_task,
        )

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        return AsyncAssignmentsResourceWithStreamingResponse(self._tasks.assignments)

    @cached_property
    def submissions(self) -> AsyncSubmissionsResourceWithStreamingResponse:
        return AsyncSubmissionsResourceWithStreamingResponse(self._tasks.submissions)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._tasks.categories)
