# Quickstart Guide

Get up and running with `chile-ine-sdk` in Python.

## Installation

Install via `pip`:

```bash
pip install chile-ine-sdk
```

For optional DataFrame integrations:

```bash
pip install "chile-ine-sdk[dataframe]"
```

## Basic Usage

```python
from ine_sdk import INEClient

client = INEClient()

# Classify occupation (CIUO)
ciuo_res = client.classifiers.predict(
    text="uber manejar pasajeros",
    classification="ciuo",
    digits=1
)
print("CIUO Prediction:", ciuo_res)

# Classify economic activity (CAENES)
caenes_res = client.classifiers.predict(
    text="produccion uva exportacion",
    classification="caenes",
    digits=2
)
print("CAENES Prediction:", caenes_res)
```

## Asynchronous Usage

```python
import asyncio
from ine_sdk import AsyncINEClient

async def main():
    async with AsyncINEClient() as client:
        res = await client.classifiers.predict(
            text="profesor ensenar clases",
            classification="ciuo",
            digits=1
        )
        print("Async Result:", res)

asyncio.run(main())
```
