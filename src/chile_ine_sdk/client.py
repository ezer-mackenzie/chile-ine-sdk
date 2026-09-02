"""Unified main SDK entry point exposing INE Classifiers and SIMEL API clients."""

from typing import Optional
from chile_ine_sdk.classifiers.client import AsyncClassifiersClient, ClassifiersClient
from chile_ine_sdk.config import CLASSIFIERS_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, SIMEL_BASE_URL
from chile_ine_sdk.http import AsyncHTTPClient, HTTPClient
from chile_ine_sdk.simel.client import AsyncSIMELClient, SIMELClient


class INEClient:
    """Unified synchronous client for INE web APIs.

    Provides sub-namespace access to:
    - `client.classifiers`: INE ML Classifiers (CIUO & CAENES) via `rapps.ine.cl`
    - `client.simel`: INE Labor Market System (SIMEL) via `simel.gob.cl`
    """

    def __init__(
        self,
        classifiers_url: str = CLASSIFIERS_BASE_URL,
        simel_url: str = SIMEL_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        self._classifiers_http = HTTPClient(
            base_url=classifiers_url, timeout=timeout, max_retries=max_retries
        )
        self._simel_http = HTTPClient(
            base_url=simel_url, timeout=timeout, max_retries=max_retries
        )

        self.classifiers = ClassifiersClient(self._classifiers_http)
        self.simel = SIMELClient(self._simel_http)

    def close(self) -> None:
        """Close underlying HTTP connections."""
        self._classifiers_http.close()
        self._simel_http.close()

    def __enter__(self) -> "INEClient":
        return self

    def __exit__(self, exc_type: Optional[type], exc_val: Optional[BaseException], exc_tb: Optional[object]) -> None:
        self.close()


class AsyncINEClient:
    """Unified asynchronous client for INE web APIs.

    Provides sub-namespace access to:
    - `client.classifiers`: INE ML Classifiers (CIUO & CAENES) via `rapps.ine.cl`
    - `client.simel`: INE Labor Market System (SIMEL) via `simel.gob.cl`
    """

    def __init__(
        self,
        classifiers_url: str = CLASSIFIERS_BASE_URL,
        simel_url: str = SIMEL_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        self._classifiers_http = AsyncHTTPClient(
            base_url=classifiers_url, timeout=timeout, max_retries=max_retries
        )
        self._simel_http = AsyncHTTPClient(
            base_url=simel_url, timeout=timeout, max_retries=max_retries
        )

        self.classifiers = AsyncClassifiersClient(self._classifiers_http)
        self.simel = AsyncSIMELClient(self._simel_http)

    async def close(self) -> None:
        """Close underlying HTTP connections."""
        await self._classifiers_http.close()
        await self._simel_http.close()

    async def __aenter__(self) -> "AsyncINEClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object],
    ) -> None:
        await self.close()
