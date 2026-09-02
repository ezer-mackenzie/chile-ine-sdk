"""Custom exceptions for the Chile INE SDK."""

from typing import Any, Optional


class INEError(Exception):
    """Base exception for all INE SDK errors."""

    pass


class INEAPIError(INEError):
    """Exception raised when an INE API returns an error response."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_body: Optional[Any] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class INEValidationError(INEError):
    """Exception raised when request parameters or payload validation fails."""

    pass


class INERateLimitError(INEAPIError):
    """Exception raised when API requests hit rate limits or timeouts."""

    pass
