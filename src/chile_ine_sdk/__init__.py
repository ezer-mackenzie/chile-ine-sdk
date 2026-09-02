"""Chile INE Python SDK (`chile_ine_sdk`).

Unified SDK for the Chilean National Institute of Statistics APIs.
"""

from chile_ine_sdk.client import AsyncINEClient, INEClient
from chile_ine_sdk.exceptions import (
    INEAPIError,
    INEError,
    INERateLimitError,
    INEValidationError,
)
from chile_ine_sdk.http import AsyncHTTPClient, HTTPClient

__version__ = "0.1.0"

__all__ = [
    "INEClient",
    "AsyncINEClient",
    "HTTPClient",
    "AsyncHTTPClient",
    "INEError",
    "INEAPIError",
    "INEValidationError",
    "INERateLimitError",
    "__version__",
]
