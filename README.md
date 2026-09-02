# Chile INE Python SDK (`chile-ine-sdk`)

[![PyPI version](https://img.shields.io/pypi/v/chile-ine-sdk.svg)](https://pypi.org/project/chile-ine-sdk/)
[![Python Versions](https://img.shields.io/pypi/pyversions/chile-ine-sdk.svg)](https://pypi.org/project/chile-ine-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, type-safe, synchronous and asynchronous Python SDK for interacting with the web APIs of the Chilean National Institute of Statistics (**INE** - *Instituto Nacional de Estadísticas*).

This unified SDK provides access to both INE API services:
1. **Classifiers API (`rapps.ine.cl`)**: Machine Learning classification models for CIUO (Occupations) and CAENES (Economic Activities).
2. **SIMEL API (`simel.gob.cl`)**: Labor Market Information System statistics, indicators, dimensions, and time series data.

---

## Features

- ⚡ **Sync & Async Support**: Seamless HTTP execution powered by `httpx`.
- 🔒 **Strong Type Safety**: Full Pydantic v2 schemas and strict MyPy typing.
- 🔁 **Automatic Retries**: Built-in exponential backoff for resilient API calls.
- 📊 **DataFrame Support**: Export statistical series directly to Pandas or Polars.
- 🌐 **Multilingual Docs**: Complete English documentation with Spanish translation support.

---

## Installation

```bash
pip install chile-ine-sdk
```

Optional DataFrame support:
```bash
pip install "chile-ine-sdk[dataframe]"
```

---

## Quickstart

```python
from ine_sdk import INEClient

# Initialize unified INE client
client = INEClient()

# 1. CIUO / CAENES Classification
prediction = client.classifiers.predict(
    text="uber manejar pasajeros",
    classification="ciuo",
    digits=1
)
print("Classification:", prediction)

# 2. SIMEL Labor Market Indicators
indicators = client.simel.list_indicators()
print("Available Indicators:", len(indicators))
```

---

## Documentation

For full documentation, tutorials, and API reference, visit [https://ezer-mackenzie.github.io/chile-ine-sdk/](https://ezer-mackenzie.github.io/chile-ine-sdk/).

---

## License

Distributed under the [MIT License](LICENSE.md).
