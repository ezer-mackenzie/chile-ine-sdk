"""Configuration settings and default endpoints for INE APIs."""

from dataclasses import dataclass

CLASSIFIERS_BASE_URL = "https://rapps.ine.cl:9292"
SIMEL_BASE_URL = "https://www.simel.gob.cl"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3
USER_AGENT = "chile-ine-sdk/0.1.0 (Python)"


@dataclass
class SDKConfig:
    """SDK configuration settings."""

    classifiers_base_url: str = CLASSIFIERS_BASE_URL
    simel_base_url: str = SIMEL_BASE_URL
    timeout: float = DEFAULT_TIMEOUT
    max_retries: int = DEFAULT_MAX_RETRIES
    user_agent: str = USER_AGENT
