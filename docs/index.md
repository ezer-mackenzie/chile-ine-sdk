# Chile INE Python SDK (`chile-ine-sdk`)

Welcome to the documentation for **`chile-ine-sdk`**, the official Python client library for interacting with the Chilean National Institute of Statistics (**INE** - *Instituto Nacional de Estadísticas*).

---

## Overview

The SDK seamlessly unifies access to the two primary API platforms provided by INE:

1. **Classifiers API (`rapps.ine.cl`)**:
   - Automated machine learning prediction for **CIUO-08.CL** (Occupations classification).
   - Automated machine learning prediction for **CAENES** (Economic Activities classification).
   - Model versioning metadata inspection.

2. **SIMEL API (`simel.gob.cl`)**:
   - Labor Market Information System statistics and indicators.
   - Dimensional queries and codelists.
   - Time series datasets exportable to Pandas and Polars DataFrames.

---

## Key Features

- ⚡ **Sync & Async Interfaces**: `INEClient` and `AsyncINEClient`.
- 🔒 **Full Type Annotations**: Powered by Pydantic v2.
- 🔁 **Automatic Retries**: Exponential backoff on request failures.
- 🌐 **Multilingual Docs**: Toggle between English and Spanish.

---

## Getting Started

Check out the [Quickstart Guide](quickstart.md) to install and begin making API calls in minutes.
