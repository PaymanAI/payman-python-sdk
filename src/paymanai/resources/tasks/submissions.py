# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.tasks.submission_list_task_submissions_response import SubmissionListTaskSubmissionsResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import List

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.tasks import submission_list_task_submissions_params

__all__ = ["SubmissionsResource", "AsyncSubmissionsResource"]


class SubmissionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubmissionsResourceWithRawResponse:
        return SubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmissionsResourceWithStreamingResponse:
        return SubmissionsResourceWithStreamingResponse(self)

    def list_task_submissions(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        statuses: List[
            Literal[
                "PENDING",
                "APPROVED_REQUIRES_REVIEW",
                "REJECTED_REQUIRES_REVIEW",
                "APPROVED",
                "REJECTED",
                "VERIFICATION_FAILED",
                "DELETED",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubmissionListTaskSubmissionsResponse:
        """
        Get all submissions for a task

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
            f"/tasks/{id}/submissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "statuses": statuses,
                    },
                    submission_list_task_submissions_params.SubmissionListTaskSubmissionsParams,
                ),
            ),
            cast_to=SubmissionListTaskSubmissionsResponse,
        )


class AsyncSubmissionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubmissionsResourceWithRawResponse:
        return AsyncSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmissionsResourceWithStreamingResponse:
        return AsyncSubmissionsResourceWithStreamingResponse(self)

    async def list_task_submissions(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        statuses: List[
            Literal[
                "PENDING",
                "APPROVED_REQUIRES_REVIEW",
                "REJECTED_REQUIRES_REVIEW",
                "APPROVED",
                "REJECTED",
                "VERIFICATION_FAILED",
                "DELETED",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubmissionListTaskSubmissionsResponse:
        """
        Get all submissions for a task

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
            f"/tasks/{id}/submissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "statuses": statuses,
                    },
                    submission_list_task_submissions_params.SubmissionListTaskSubmissionsParams,
                ),
            ),
            cast_to=SubmissionListTaskSubmissionsResponse,
        )


class SubmissionsResourceWithRawResponse:
    def __init__(self, submissions: SubmissionsResource) -> None:
        self._submissions = submissions

        self.list_task_submissions = to_raw_response_wrapper(
            submissions.list_task_submissions,
        )


class AsyncSubmissionsResourceWithRawResponse:
    def __init__(self, submissions: AsyncSubmissionsResource) -> None:
        self._submissions = submissions

        self.list_task_submissions = async_to_raw_response_wrapper(
            submissions.list_task_submissions,
        )


class SubmissionsResourceWithStreamingResponse:
    def __init__(self, submissions: SubmissionsResource) -> None:
        self._submissions = submissions

        self.list_task_submissions = to_streamed_response_wrapper(
            submissions.list_task_submissions,
        )


class AsyncSubmissionsResourceWithStreamingResponse:
    def __init__(self, submissions: AsyncSubmissionsResource) -> None:
        self._submissions = submissions

        self.list_task_submissions = async_to_streamed_response_wrapper(
            submissions.list_task_submissions,
        )
