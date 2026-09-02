# SIMEL API (`client.simel`)

The SIMEL API provides access to the Labor Market Information System (*Sistema de Información de Mercado Laboral*).

## Querying Indicators

```python
indicators = client.simel.list_indicators()

data = client.simel.get_indicator_data(
    indicator_id="EMP_01",
    period="2024-Q1"
)
```
