# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.description_get_api_description_response import DescriptionGetAPIDescriptionResponse

__all__ = ["DescriptionResource", "AsyncDescriptionResource"]


class DescriptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DescriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DescriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DescriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#with_streaming_response
        """
        return DescriptionResourceWithStreamingResponse(self)

    def get_api_description(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DescriptionGetAPIDescriptionResponse:
        return self._get(
            "/description",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DescriptionGetAPIDescriptionResponse,
        )


class AsyncDescriptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDescriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDescriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDescriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/PaymanAI/payman-python-sdk#with_streaming_response
        """
        return AsyncDescriptionResourceWithStreamingResponse(self)

    async def get_api_description(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DescriptionGetAPIDescriptionResponse:
        return await self._get(
            "/description",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DescriptionGetAPIDescriptionResponse,
        )


class DescriptionResourceWithRawResponse:
    def __init__(self, description: DescriptionResource) -> None:
        self._description = description

        self.get_api_description = to_raw_response_wrapper(
            description.get_api_description,
        )


class AsyncDescriptionResourceWithRawResponse:
    def __init__(self, description: AsyncDescriptionResource) -> None:
        self._description = description

        self.get_api_description = async_to_raw_response_wrapper(
            description.get_api_description,
        )


class DescriptionResourceWithStreamingResponse:
    def __init__(self, description: DescriptionResource) -> None:
        self._description = description

        self.get_api_description = to_streamed_response_wrapper(
            description.get_api_description,
        )


class AsyncDescriptionResourceWithStreamingResponse:
    def __init__(self, description: AsyncDescriptionResource) -> None:
        self._description = description

        self.get_api_description = async_to_streamed_response_wrapper(
            description.get_api_description,
        )
