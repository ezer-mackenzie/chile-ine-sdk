# Classifiers API (`client.classifiers`)

The Classifiers API provides machine learning inference for standard Chilean statistical taxonomies: **CIUO-08.CL** (Occupations) and **CAENES** (Economic Activities).

## Predict Endpoint (`POST /predict`)

```python
result = client.classifiers.predict(
    text="enfermero realizar curaciones",
    classification="ciuo",  # 'ciuo' or 'caenes'
    digits=1,               # 1 or 2 digits
    model_version="latest"
)
```

## Model Metadata (`GET /get_model_metadata`)

```python
metadata = client.classifiers.get_model_metadata()
print("Model metadata:", metadata)
```
