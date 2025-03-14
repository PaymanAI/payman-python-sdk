# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
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
from .resources import me, version, balances, payments, spend_limits
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PaymanaiError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Paymanai",
    "AsyncPaymanai",
    "Client",
    "AsyncClient",
]


class Paymanai(SyncAPIClient):
    version: version.VersionResource
    me: me.MeResource
    balances: balances.BalancesResource
    payments: payments.PaymentsResource
    spend_limits: spend_limits.SpendLimitsResource
    with_raw_response: PaymanaiWithRawResponse
    with_streaming_response: PaymanaiWithStreamedResponse

    # client options
    x_payman_api_secret: str

    def __init__(
        self,
        *,
        x_payman_api_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
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
        """Construct a new synchronous Paymanai client instance.

        This automatically infers the `x_payman_api_secret` argument from the `PAYMAN_API_SECRET` environment variable if it is not provided.
        """
        if x_payman_api_secret is None:
            x_payman_api_secret = os.environ.get("PAYMAN_API_SECRET")
        if x_payman_api_secret is None:
            raise PaymanaiError(
                "The x_payman_api_secret client option must be set either by passing x_payman_api_secret to the client or by setting the PAYMAN_API_SECRET environment variable"
            )
        self.x_payman_api_secret = x_payman_api_secret

        if base_url is None:
            base_url = os.environ.get("PAYMANAI_BASE_URL")
        if base_url is None:
            base_url = f"https://agent.payman.ai/api"

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

        self.version = version.VersionResource(self)
        self.me = me.MeResource(self)
        self.balances = balances.BalancesResource(self)
        self.payments = payments.PaymentsResource(self)
        self.spend_limits = spend_limits.SpendLimitsResource(self)
        self.with_raw_response = PaymanaiWithRawResponse(self)
        self.with_streaming_response = PaymanaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        x_payman_api_secret = self.x_payman_api_secret
        return {"x-payman-api-secret": x_payman_api_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "Accept": "application/vnd.payman.v1+json",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_payman_api_secret: str | None = None,
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
            x_payman_api_secret=x_payman_api_secret or self.x_payman_api_secret,
            base_url=base_url or self.base_url,
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
    version: version.AsyncVersionResource
    me: me.AsyncMeResource
    balances: balances.AsyncBalancesResource
    payments: payments.AsyncPaymentsResource
    spend_limits: spend_limits.AsyncSpendLimitsResource
    with_raw_response: AsyncPaymanaiWithRawResponse
    with_streaming_response: AsyncPaymanaiWithStreamedResponse

    # client options
    x_payman_api_secret: str

    def __init__(
        self,
        *,
        x_payman_api_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
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
        """Construct a new async AsyncPaymanai client instance.

        This automatically infers the `x_payman_api_secret` argument from the `PAYMAN_API_SECRET` environment variable if it is not provided.
        """
        if x_payman_api_secret is None:
            x_payman_api_secret = os.environ.get("PAYMAN_API_SECRET")
        if x_payman_api_secret is None:
            raise PaymanaiError(
                "The x_payman_api_secret client option must be set either by passing x_payman_api_secret to the client or by setting the PAYMAN_API_SECRET environment variable"
            )
        self.x_payman_api_secret = x_payman_api_secret

        if base_url is None:
            base_url = os.environ.get("PAYMANAI_BASE_URL")
        if base_url is None:
            base_url = f"https://agent.payman.ai/api"

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

        self.version = version.AsyncVersionResource(self)
        self.me = me.AsyncMeResource(self)
        self.balances = balances.AsyncBalancesResource(self)
        self.payments = payments.AsyncPaymentsResource(self)
        self.spend_limits = spend_limits.AsyncSpendLimitsResource(self)
        self.with_raw_response = AsyncPaymanaiWithRawResponse(self)
        self.with_streaming_response = AsyncPaymanaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        x_payman_api_secret = self.x_payman_api_secret
        return {"x-payman-api-secret": x_payman_api_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "Accept": "application/vnd.payman.v1+json",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_payman_api_secret: str | None = None,
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
            x_payman_api_secret=x_payman_api_secret or self.x_payman_api_secret,
            base_url=base_url or self.base_url,
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
        self.version = version.VersionResourceWithRawResponse(client.version)
        self.me = me.MeResourceWithRawResponse(client.me)
        self.balances = balances.BalancesResourceWithRawResponse(client.balances)
        self.payments = payments.PaymentsResourceWithRawResponse(client.payments)
        self.spend_limits = spend_limits.SpendLimitsResourceWithRawResponse(client.spend_limits)


class AsyncPaymanaiWithRawResponse:
    def __init__(self, client: AsyncPaymanai) -> None:
        self.version = version.AsyncVersionResourceWithRawResponse(client.version)
        self.me = me.AsyncMeResourceWithRawResponse(client.me)
        self.balances = balances.AsyncBalancesResourceWithRawResponse(client.balances)
        self.payments = payments.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.spend_limits = spend_limits.AsyncSpendLimitsResourceWithRawResponse(client.spend_limits)


class PaymanaiWithStreamedResponse:
    def __init__(self, client: Paymanai) -> None:
        self.version = version.VersionResourceWithStreamingResponse(client.version)
        self.me = me.MeResourceWithStreamingResponse(client.me)
        self.balances = balances.BalancesResourceWithStreamingResponse(client.balances)
        self.payments = payments.PaymentsResourceWithStreamingResponse(client.payments)
        self.spend_limits = spend_limits.SpendLimitsResourceWithStreamingResponse(client.spend_limits)


class AsyncPaymanaiWithStreamedResponse:
    def __init__(self, client: AsyncPaymanai) -> None:
        self.version = version.AsyncVersionResourceWithStreamingResponse(client.version)
        self.me = me.AsyncMeResourceWithStreamingResponse(client.me)
        self.balances = balances.AsyncBalancesResourceWithStreamingResponse(client.balances)
        self.payments = payments.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.spend_limits = spend_limits.AsyncSpendLimitsResourceWithStreamingResponse(client.spend_limits)


Client = Paymanai

AsyncClient = AsyncPaymanai
