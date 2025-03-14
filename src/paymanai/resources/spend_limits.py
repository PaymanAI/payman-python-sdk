# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["SpendLimitsResource", "AsyncSpendLimitsResource"]


class SpendLimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpendLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SpendLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#with_streaming_response
        """
        return SpendLimitsResourceWithStreamingResponse(self)

    def get_spend_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Returns wallet spend limit details of the current agent"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/spend-limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSpendLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpendLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSpendLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#with_streaming_response
        """
        return AsyncSpendLimitsResourceWithStreamingResponse(self)

    async def get_spend_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Returns wallet spend limit details of the current agent"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/spend-limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SpendLimitsResourceWithRawResponse:
    def __init__(self, spend_limits: SpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.get_spend_limits = to_custom_raw_response_wrapper(
            spend_limits.get_spend_limits,
            BinaryAPIResponse,
        )


class AsyncSpendLimitsResourceWithRawResponse:
    def __init__(self, spend_limits: AsyncSpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.get_spend_limits = async_to_custom_raw_response_wrapper(
            spend_limits.get_spend_limits,
            AsyncBinaryAPIResponse,
        )


class SpendLimitsResourceWithStreamingResponse:
    def __init__(self, spend_limits: SpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.get_spend_limits = to_custom_streamed_response_wrapper(
            spend_limits.get_spend_limits,
            StreamedBinaryAPIResponse,
        )


class AsyncSpendLimitsResourceWithStreamingResponse:
    def __init__(self, spend_limits: AsyncSpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.get_spend_limits = async_to_custom_streamed_response_wrapper(
            spend_limits.get_spend_limits,
            AsyncStreamedBinaryAPIResponse,
        )
