# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .private import (
    PrivateResource,
    AsyncPrivateResource,
    PrivateResourceWithRawResponse,
    AsyncPrivateResourceWithRawResponse,
    PrivateResourceWithStreamingResponse,
    AsyncPrivateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def private(self) -> PrivateResource:
        return PrivateResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self)


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def private(self) -> AsyncPrivateResource:
        return AsyncPrivateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self)


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

    @cached_property
    def private(self) -> PrivateResourceWithRawResponse:
        return PrivateResourceWithRawResponse(self._files.private)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

    @cached_property
    def private(self) -> AsyncPrivateResourceWithRawResponse:
        return AsyncPrivateResourceWithRawResponse(self._files.private)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

    @cached_property
    def private(self) -> PrivateResourceWithStreamingResponse:
        return PrivateResourceWithStreamingResponse(self._files.private)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

    @cached_property
    def private(self) -> AsyncPrivateResourceWithStreamingResponse:
        return AsyncPrivateResourceWithStreamingResponse(self._files.private)
