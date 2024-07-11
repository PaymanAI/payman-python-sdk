# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PaymanaiError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Paymanai",
    "AsyncPaymanai",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "sandbox": "https://sandbox-agent.payman.ai/api",
    "production": "https://agent.payman.ai/api",
}


class Paymanai(SyncAPIClient):
    tasks: resources.TasksResource
    wallets: resources.WalletsResource
    version: resources.VersionResource
    files: resources.FilesResource
    with_raw_response: PaymanaiWithRawResponse
    with_streaming_response: PaymanaiWithStreamedResponse

    # client options
    x_payman_agent_id: str
    x_payman_api_secret: str

    _environment: Literal["sandbox", "production"] | NotGiven

    def __init__(
        self,
        *,
        x_payman_agent_id: str | None = None,
        x_payman_api_secret: str | None = None,
        environment: Literal["sandbox", "production"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous paymanai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `x_payman_agent_id` from `PAYMAN_AGENT_ID`
        - `x_payman_api_secret` from `PAYMAN_API_SECRET`
        """
        if x_payman_agent_id is None:
            x_payman_agent_id = os.environ.get("PAYMAN_AGENT_ID")
        if x_payman_agent_id is None:
            raise PaymanaiError(
                "The x_payman_agent_id client option must be set either by passing x_payman_agent_id to the client or by setting the PAYMAN_AGENT_ID environment variable"
            )
        self.x_payman_agent_id = x_payman_agent_id

        if x_payman_api_secret is None:
            x_payman_api_secret = os.environ.get("PAYMAN_API_SECRET")
        if x_payman_api_secret is None:
            raise PaymanaiError(
                "The x_payman_api_secret client option must be set either by passing x_payman_api_secret to the client or by setting the PAYMAN_API_SECRET environment variable"
            )
        self.x_payman_api_secret = x_payman_api_secret

        self._environment = environment

        base_url_env = os.environ.get("PAYMANAI_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PAYMANAI_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "sandbox"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.tasks = resources.TasksResource(self)
        self.wallets = resources.WalletsResource(self)
        self.version = resources.VersionResource(self)
        self.files = resources.FilesResource(self)
        self.with_raw_response = PaymanaiWithRawResponse(self)
        self.with_streaming_response = PaymanaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._x_payman_agent_id:
            return self._x_payman_agent_id
        if self._x_payman_api_secret:
            return self._x_payman_api_secret
        return {}

    @property
    def _x_payman_agent_id(self) -> dict[str, str]:
        x_payman_agent_id = self.x_payman_agent_id
        return {"x-payman-agent-id": x_payman_agent_id}

    @property
    def _x_payman_api_secret(self) -> dict[str, str]:
        x_payman_api_secret = self.x_payman_api_secret
        return {"x-payman-api-secret": x_payman_api_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_payman_agent_id: str | None = None,
        x_payman_api_secret: str | None = None,
        environment: Literal["sandbox", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            x_payman_agent_id=x_payman_agent_id or self.x_payman_agent_id,
            x_payman_api_secret=x_payman_api_secret or self.x_payman_api_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPaymanai(AsyncAPIClient):
    tasks: resources.AsyncTasksResource
    wallets: resources.AsyncWalletsResource
    version: resources.AsyncVersionResource
    files: resources.AsyncFilesResource
    with_raw_response: AsyncPaymanaiWithRawResponse
    with_streaming_response: AsyncPaymanaiWithStreamedResponse

    # client options
    x_payman_agent_id: str
    x_payman_api_secret: str

    _environment: Literal["sandbox", "production"] | NotGiven

    def __init__(
        self,
        *,
        x_payman_agent_id: str | None = None,
        x_payman_api_secret: str | None = None,
        environment: Literal["sandbox", "production"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async paymanai client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `x_payman_agent_id` from `PAYMAN_AGENT_ID`
        - `x_payman_api_secret` from `PAYMAN_API_SECRET`
        """
        if x_payman_agent_id is None:
            x_payman_agent_id = os.environ.get("PAYMAN_AGENT_ID")
        if x_payman_agent_id is None:
            raise PaymanaiError(
                "The x_payman_agent_id client option must be set either by passing x_payman_agent_id to the client or by setting the PAYMAN_AGENT_ID environment variable"
            )
        self.x_payman_agent_id = x_payman_agent_id

        if x_payman_api_secret is None:
            x_payman_api_secret = os.environ.get("PAYMAN_API_SECRET")
        if x_payman_api_secret is None:
            raise PaymanaiError(
                "The x_payman_api_secret client option must be set either by passing x_payman_api_secret to the client or by setting the PAYMAN_API_SECRET environment variable"
            )
        self.x_payman_api_secret = x_payman_api_secret

        self._environment = environment

        base_url_env = os.environ.get("PAYMANAI_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PAYMANAI_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "sandbox"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.tasks = resources.AsyncTasksResource(self)
        self.wallets = resources.AsyncWalletsResource(self)
        self.version = resources.AsyncVersionResource(self)
        self.files = resources.AsyncFilesResource(self)
        self.with_raw_response = AsyncPaymanaiWithRawResponse(self)
        self.with_streaming_response = AsyncPaymanaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self._x_payman_agent_id:
            return self._x_payman_agent_id
        if self._x_payman_api_secret:
            return self._x_payman_api_secret
        return {}

    @property
    def _x_payman_agent_id(self) -> dict[str, str]:
        x_payman_agent_id = self.x_payman_agent_id
        return {"x-payman-agent-id": x_payman_agent_id}

    @property
    def _x_payman_api_secret(self) -> dict[str, str]:
        x_payman_api_secret = self.x_payman_api_secret
        return {"x-payman-api-secret": x_payman_api_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_payman_agent_id: str | None = None,
        x_payman_api_secret: str | None = None,
        environment: Literal["sandbox", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            x_payman_agent_id=x_payman_agent_id or self.x_payman_agent_id,
            x_payman_api_secret=x_payman_api_secret or self.x_payman_api_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PaymanaiWithRawResponse:
    def __init__(self, client: Paymanai) -> None:
        self.tasks = resources.TasksResourceWithRawResponse(client.tasks)
        self.wallets = resources.WalletsResourceWithRawResponse(client.wallets)
        self.version = resources.VersionResourceWithRawResponse(client.version)
        self.files = resources.FilesResourceWithRawResponse(client.files)


class AsyncPaymanaiWithRawResponse:
    def __init__(self, client: AsyncPaymanai) -> None:
        self.tasks = resources.AsyncTasksResourceWithRawResponse(client.tasks)
        self.wallets = resources.AsyncWalletsResourceWithRawResponse(client.wallets)
        self.version = resources.AsyncVersionResourceWithRawResponse(client.version)
        self.files = resources.AsyncFilesResourceWithRawResponse(client.files)


class PaymanaiWithStreamedResponse:
    def __init__(self, client: Paymanai) -> None:
        self.tasks = resources.TasksResourceWithStreamingResponse(client.tasks)
        self.wallets = resources.WalletsResourceWithStreamingResponse(client.wallets)
        self.version = resources.VersionResourceWithStreamingResponse(client.version)
        self.files = resources.FilesResourceWithStreamingResponse(client.files)


class AsyncPaymanaiWithStreamedResponse:
    def __init__(self, client: AsyncPaymanai) -> None:
        self.tasks = resources.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.wallets = resources.AsyncWalletsResourceWithStreamingResponse(client.wallets)
        self.version = resources.AsyncVersionResourceWithStreamingResponse(client.version)
        self.files = resources.AsyncFilesResourceWithStreamingResponse(client.files)


Client = Paymanai

AsyncClient = AsyncPaymanai
