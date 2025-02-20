# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from paymanai import Paymanai, AsyncPaymanai
from paymanai._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_agent_by_reference(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/ref").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = client.agents.get_agent_by_reference(
            "ref",
        )
        assert agent.is_closed
        assert agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_agent_by_reference(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/ref").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        agent = client.agents.with_raw_response.get_agent_by_reference(
            "ref",
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert agent.json() == {"foo": "bar"}
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_agent_by_reference(self, client: Paymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/ref").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agents.with_streaming_response.get_agent_by_reference(
            "ref",
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, StreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_agent_by_reference(self, client: Paymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref` but received ''"):
            client.agents.with_raw_response.get_agent_by_reference(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_agent_by_reference(self, async_client: AsyncPaymanai, respx_mock: MockRouter) -> None:
        respx_mock.get("/agents/ref").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = await async_client.agents.get_agent_by_reference(
            "ref",
        )
        assert agent.is_closed
        assert await agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_agent_by_reference(
        self, async_client: AsyncPaymanai, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agents/ref").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        agent = await async_client.agents.with_raw_response.get_agent_by_reference(
            "ref",
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await agent.json() == {"foo": "bar"}
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_agent_by_reference(
        self, async_client: AsyncPaymanai, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/agents/ref").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agents.with_streaming_response.get_agent_by_reference(
            "ref",
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_agent_by_reference(self, async_client: AsyncPaymanai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref` but received ''"):
            await async_client.agents.with_raw_response.get_agent_by_reference(
                "",
            )
