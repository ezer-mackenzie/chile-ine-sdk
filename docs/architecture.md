# Architecture & SDK Design

`chile-ine-sdk` is architected as a modular, decoupled Python SDK supporting both of INE's distinct web API services:

```
                  ┌──────────────────────┐
                  │      INEClient       │
                  │   (or AsyncClient)   │
                  └──────────┬───────────┘
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
 ┌─────────────────────┐           ┌─────────────────────┐
 │  client.classifiers │           │    client.simel     │
 └──────────┬──────────┘           └──────────┬──────────┘
            │                                 │
            ▼                                 ▼
 ┌─────────────────────┐           ┌─────────────────────┐
 │  rapps.ine.cl:9292  │           │    simel.gob.cl     │
 └─────────────────────┘           └─────────────────────┘
```

## Transport Layer (`_http.py`)

All HTTP interactions are driven by `httpx`, supporting connection pooling, keep-alive headers, automated exponential backoff retries, and unified exception mapping.
