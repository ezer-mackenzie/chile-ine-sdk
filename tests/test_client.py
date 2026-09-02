"""Unit tests for INEClient, AsyncINEClient, ClassifiersClient, SIMELClient and HTTPClient."""

import pytest
import respx
from chile_ine_sdk import AsyncINEClient, HTTPClient, INEClient
from chile_ine_sdk.classifiers import ClassifierType
from chile_ine_sdk.simel.models import IndicatorData, Observation
from httpx import Response


def test_ine_client_initialization() -> None:
    client = INEClient()
    assert client.classifiers is not None
    assert client.simel is not None
    client.close()


@pytest.mark.asyncio
async def test_async_ine_client_initialization() -> None:
    async with AsyncINEClient() as client:
        assert client.classifiers is not None
        assert client.simel is not None


def test_http_client_custom_headers() -> None:
    http = HTTPClient(base_url="https://rapps.ine.cl:9292", headers={"X-Custom": "test"})
    assert http.client.headers["X-Custom"] == "test"
    http.close()


@respx.mock
def test_classifiers_predict_sync() -> None:
    respx.post("https://rapps.ine.cl:9292/predict").mock(
        return_value=Response(
            200,
            json={
                "predictions": [
                    {
                        "gloss": "uber manejar pasajeros",
                        "code": "8322",
                        "probability": 0.95,
                    }
                ]
            },
        )
    )

    with INEClient() as client:
        result = client.classifiers.predict(
            text="uber manejar pasajeros",
            classification=ClassifierType.CIUO,
            digits=1,
        )
        assert "predictions" in result
        assert result["predictions"][0]["code"] == "8322"


@respx.mock
def test_classifiers_predict_ciuo_and_caenes_helpers() -> None:
    respx.post("https://rapps.ine.cl:9292/predict").mock(
        return_value=Response(
            200,
            json={
                "predictions": [
                    {
                        "gloss": "produccion uva exportacion",
                        "code": "0111",
                        "probability": 0.99,
                    }
                ]
            },
        )
    )

    with INEClient() as client:
        ciuo = client.classifiers.predict_ciuo("chofer colectivo", digits=1)
        assert ciuo["predictions"][0]["code"] == "0111"

        caenes = client.classifiers.predict_caenes("cultivo uva", digits=2)
        assert caenes["predictions"][0]["code"] == "0111"


@respx.mock
@pytest.mark.asyncio
async def test_classifiers_predict_async() -> None:
    respx.post("https://rapps.ine.cl:9292/predict").mock(
        return_value=Response(
            200,
            json={
                "predictions": [
                    {
                        "gloss": "enfermero realizar curaciones",
                        "code": "2221",
                        "probability": 0.98,
                    }
                ]
            },
        )
    )

    async with AsyncINEClient() as client:
        result = await client.classifiers.predict(
            text="enfermero realizar curaciones",
            classification="ciuo",
            digits=1,
        )
        assert "predictions" in result
        assert result["predictions"][0]["code"] == "2221"


@respx.mock
def test_get_model_metadata() -> None:
    respx.get("https://rapps.ine.cl:9292/get_model_metadata").mock(
        return_value=Response(
            200,
            json={"model_version": "latest", "architectures": ["bert-base-spanish"]},
        )
    )

    with INEClient() as client:
        meta = client.classifiers.get_model_metadata()
        assert meta["model_version"] == "latest"


def test_indicator_data_dataframe_export_without_deps() -> None:
    data = IndicatorData(
        indicator_id="IND_01",
        observations=[Observation(period="2024-Q1", value=7.8)],
    )

    # pandas import error check if not installed or present
    try:
        df = data.to_pandas()
        assert df is not None
    except ImportError as e:
        assert "pandas is required" in str(e)
