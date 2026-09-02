# Chile INE Python SDK (`chile-ine-sdk`)

Bienvenido a la documentación de **`chile-ine-sdk`**, la librería cliente en Python para interactuar con las APIs del Instituto Nacional de Estadísticas de Chile (**INE**).

---

## Descripción General

El SDK unifica el acceso a los dos servicios API principales del INE:

1. **API de Clasificadores (`rapps.ine.cl`)**:
   - Predicción mediante Machine Learning para la clasificación **CIUO-08.CL** (Ocupaciones).
   - Predicción mediante Machine Learning para la clasificación **CAENES** (Actividades Económicas).
   - Consulta de metadatos y versiones de modelos.

2. **API SIMEL (`simel.gob.cl`)**:
   - Estadísticas e indicadores del Sistema de Información de Mercado Laboral.
   - Consultas dimensionales y listas de códigos.
   - Series temporales exportables a DataFrames de Pandas y Polars.
