"""Chile INE Python SDK (`chile-ine-sdk`).

Unified SDK for the Chilean National Institute of Statistics APIs.
"""

from ine_sdk.client import AsyncINEClient, INEClient
from ine_sdk.exceptions import (
    INEAPIError,
    INEError,
    INERateLimitError,
    INEValidationError,
)

__version__ = "0.1.0"

__all__ = [
    "INEClient",
    "AsyncINEClient",
    "INEError",
    "INEAPIError",
    "INEValidationError",
    "INERateLimitError",
    "__version__",
]
