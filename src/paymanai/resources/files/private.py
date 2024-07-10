# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.files import private_download_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["PrivateResource", "AsyncPrivateResource"]


class PrivateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrivateResourceWithRawResponse:
        return PrivateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateResourceWithStreamingResponse:
        return PrivateResourceWithStreamingResponse(self)

    def download(
        self,
        *,
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/files/private/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"key": key}, private_download_params.PrivateDownloadParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncPrivateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrivateResourceWithRawResponse:
        return AsyncPrivateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateResourceWithStreamingResponse:
        return AsyncPrivateResourceWithStreamingResponse(self)

    async def download(
        self,
        *,
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/files/private/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"key": key}, private_download_params.PrivateDownloadParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class PrivateResourceWithRawResponse:
    def __init__(self, private: PrivateResource) -> None:
        self._private = private

        self.download = to_custom_raw_response_wrapper(
            private.download,
            BinaryAPIResponse,
        )


class AsyncPrivateResourceWithRawResponse:
    def __init__(self, private: AsyncPrivateResource) -> None:
        self._private = private

        self.download = async_to_custom_raw_response_wrapper(
            private.download,
            AsyncBinaryAPIResponse,
        )


class PrivateResourceWithStreamingResponse:
    def __init__(self, private: PrivateResource) -> None:
        self._private = private

        self.download = to_custom_streamed_response_wrapper(
            private.download,
            StreamedBinaryAPIResponse,
        )


class AsyncPrivateResourceWithStreamingResponse:
    def __init__(self, private: AsyncPrivateResource) -> None:
        self._private = private

        self.download = async_to_custom_streamed_response_wrapper(
            private.download,
            AsyncStreamedBinaryAPIResponse,
        )
