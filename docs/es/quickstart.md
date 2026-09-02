# Guía Rápida

Comienza a utilizar `chile_ine_sdk` en Python en pocos pasos.

## Instalación

Instalar a través de `pip`:

```bash
pip install chile-ine-sdk
```

Para soporte opcional de DataFrames:

```bash
pip install "chile-ine-sdk[dataframe]"
```

## Uso Básico

```python
from chile_ine_sdk import INEClient

client = INEClient()

# Clasificar ocupación (CIUO)
ciuo_res = client.classifiers.predict(
    text="uber manejar pasajeros",
    classification="ciuo",
    digits=1
)
print("Predicción CIUO:", ciuo_res)
```
