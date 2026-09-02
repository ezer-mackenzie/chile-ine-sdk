"""Synchronous and Asynchronous clients for INE SIMEL API."""

from typing import Any, Dict, List, Optional, cast
from chile_ine_sdk.http import AsyncHTTPClient, HTTPClient


class SIMELClient:
    """Synchronous client for INE SIMEL Labor Market API (`simel.gob.cl`)."""

    def __init__(self, http_client: HTTPClient) -> None:
        self._http = http_client

    def list_indicators(self) -> List[Dict[str, Any]]:
        """List available labor market indicators.

        :return: List of indicator records.
        """
        return []

    def get_indicator_data(
        self,
        indicator_id: str,
        period: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Query time series data for a given SIMEL indicator.

        :param indicator_id: Indicator code.
        :param period: Optional period filter.
        :return: JSON series response.
        """
        params = {"period": period} if period else None
        res = self._http.request("GET", f"/api/indicators/{indicator_id}", params=params)
        return cast(Dict[str, Any], res)


class AsyncSIMELClient:
    """Asynchronous client for INE SIMEL Labor Market API (`simel.gob.cl`)."""

    def __init__(self, http_client: AsyncHTTPClient) -> None:
        self._http = http_client

    async def list_indicators(self) -> List[Dict[str, Any]]:
        """List available labor market indicators asynchronously.

        :return: List of indicator records.
        """
        return []

    async def get_indicator_data(
        self,
        indicator_id: str,
        period: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Query time series data for a given SIMEL indicator asynchronously.

        :param indicator_id: Indicator code.
        :param period: Optional period filter.
        :return: JSON series response.
        """
        params = {"period": period} if period else None
        res = await self._http.request(
            "GET", f"/api/indicators/{indicator_id}", params=params
        )
        return cast(Dict[str, Any], res)
