"""HTTP transport abstraction layer for sync and async API execution."""

from typing import Any, Dict, Optional
import httpx

from ine_sdk.config import DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, USER_AGENT
from ine_sdk.exceptions import INEAPIError, INERateLimitError


class HTTPClient:
    """Synchronous HTTP client for INE services."""

    def __init__(
        self,
        base_url: str,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        headers: Optional[Dict[str, str]] = None,
    ) -> None:
        self.base_url = base_url
        req_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
        if headers:
            req_headers.update(headers)
        self.client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers=req_headers,
        )

    def request(
        self,
        method: str,
        path: str,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        try:
            response = self.client.request(method, path, json=json, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 429:
                raise INERateLimitError(
                    "Rate limit exceeded",
                    status_code=429,
                    response_body=exc.response.text,
                ) from exc
            raise INEAPIError(
                f"HTTP {exc.response.status_code}: {exc.response.text}",
                status_code=exc.response.status_code,
                response_body=exc.response.text,
            ) from exc
        except httpx.RequestError as exc:
            raise INEAPIError(f"Network error: {exc}") from exc

    def close(self) -> None:
        self.client.close()


class AsyncHTTPClient:
    """Asynchronous HTTP client for INE services."""

    def __init__(
        self,
        base_url: str,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        headers: Optional[Dict[str, str]] = None,
    ) -> None:
        self.base_url = base_url
        req_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
        if headers:
            req_headers.update(headers)
        self.client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers=req_headers,
        )

    async def request(
        self,
        method: str,
        path: str,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        try:
            response = await self.client.request(method, path, json=json, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 429:
                raise INERateLimitError(
                    "Rate limit exceeded",
                    status_code=429,
                    response_body=exc.response.text,
                ) from exc
            raise INEAPIError(
                f"HTTP {exc.response.status_code}: {exc.response.text}",
                status_code=exc.response.status_code,
                response_body=exc.response.text,
            ) from exc
        except httpx.RequestError as exc:
            raise INEAPIError(f"Network error: {exc}") from exc

    async def close(self) -> None:
        await self.client.aclose()
