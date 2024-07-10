# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tasks import assignment_list_params, assignment_create_params
from ..._base_client import (
    make_request_options,
)
from ...types.tasks.assignment_list_response import AssignmentListResponse
from ...types.tasks.assignment_create_response import AssignmentCreateResponse

__all__ = ["AssignmentsResource", "AsyncAssignmentsResource"]


class AssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssignmentsResourceWithRawResponse:
        return AssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssignmentsResourceWithStreamingResponse:
        return AssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invite_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentCreateResponse:
        """Assign a task to a user by email.

        The user will receive an email prompting them
        to log into the Payman system at which point they will be able to accept the
        invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return self._post(
            f"/tasks/{id}/assignments",
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "invite_email": invite_email,
                },
                assignment_create_params.AssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssignmentCreateResponse,
        )

    def list(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        statuses: List[Literal["IN_REVIEW", "PENDING", "COMPLETED", "EXPIRED", "DELETED", "REJECTED", "ACCEPTED"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentListResponse:
        """
        Get all assignments for a task

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
            f"/tasks/{id}/assignments",
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
                    assignment_list_params.AssignmentListParams,
                ),
            ),
            cast_to=AssignmentListResponse,
        )


class AsyncAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssignmentsResourceWithRawResponse:
        return AsyncAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        return AsyncAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invite_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentCreateResponse:
        """Assign a task to a user by email.

        The user will receive an email prompting them
        to log into the Payman system at which point they will be able to accept the
        invite.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.payman.v1+json", **(extra_headers or {})}
        return await self._post(
            f"/tasks/{id}/assignments",
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "invite_email": invite_email,
                },
                assignment_create_params.AssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssignmentCreateResponse,
        )

    async def list(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        statuses: List[Literal["IN_REVIEW", "PENDING", "COMPLETED", "EXPIRED", "DELETED", "REJECTED", "ACCEPTED"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentListResponse:
        """
        Get all assignments for a task

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
            f"/tasks/{id}/assignments",
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
                    assignment_list_params.AssignmentListParams,
                ),
            ),
            cast_to=AssignmentListResponse,
        )


class AssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.create = to_raw_response_wrapper(
            assignments.create,
        )
        self.list = to_raw_response_wrapper(
            assignments.list,
        )


class AsyncAssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.create = async_to_raw_response_wrapper(
            assignments.create,
        )
        self.list = async_to_raw_response_wrapper(
            assignments.list,
        )


class AssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.create = to_streamed_response_wrapper(
            assignments.create,
        )
        self.list = to_streamed_response_wrapper(
            assignments.list,
        )


class AsyncAssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.create = async_to_streamed_response_wrapper(
            assignments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            assignments.list,
        )
