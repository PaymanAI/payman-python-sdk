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
from ..types.wallet_get_wallet_response import WalletGetWalletResponse

__all__ = ["WalletsResource", "AsyncWalletsResource"]


class WalletsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WalletsResourceWithRawResponse:
        return WalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletsResourceWithStreamingResponse:
        return WalletsResourceWithStreamingResponse(self)

    def get_wallet(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletGetWalletResponse:
        """
        Get a wallet by ID

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
            f"/wallets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletGetWalletResponse,
        )


class AsyncWalletsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWalletsResourceWithRawResponse:
        return AsyncWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletsResourceWithStreamingResponse:
        return AsyncWalletsResourceWithStreamingResponse(self)

    async def get_wallet(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WalletGetWalletResponse:
        """
        Get a wallet by ID

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
            f"/wallets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WalletGetWalletResponse,
        )


class WalletsResourceWithRawResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.get_wallet = to_raw_response_wrapper(
            wallets.get_wallet,
        )


class AsyncWalletsResourceWithRawResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.get_wallet = async_to_raw_response_wrapper(
            wallets.get_wallet,
        )


class WalletsResourceWithStreamingResponse:
    def __init__(self, wallets: WalletsResource) -> None:
        self._wallets = wallets

        self.get_wallet = to_streamed_response_wrapper(
            wallets.get_wallet,
        )


class AsyncWalletsResourceWithStreamingResponse:
    def __init__(self, wallets: AsyncWalletsResource) -> None:
        self._wallets = wallets

        self.get_wallet = async_to_streamed_response_wrapper(
            wallets.get_wallet,
        )
