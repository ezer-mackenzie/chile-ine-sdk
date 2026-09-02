# API Reference

## `ine_sdk.INEClient`

Unified synchronous client for INE APIs.

```python
class INEClient:
    def __init__(self, timeout: float = 30.0, max_retries: int = 3): ...
    
    @property
    def classifiers() -> ClassifiersClient: ...
    
    @property
    def simel() -> SIMELClient: ...
```

## `ine_sdk.AsyncINEClient`

Unified asynchronous client for INE APIs.

```python
class AsyncINEClient:
    def __init__(self, timeout: float = 30.0, max_retries: int = 3): ...
    
    @property
    def classifiers() -> AsyncClassifiersClient: ...
    
    @property
    def simel() -> AsyncSIMELClient: ...
```
