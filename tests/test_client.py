"""Unit tests for INEClient and AsyncINEClient initialization and prediction mocks."""

import pytest
import respx
from httpx import Response
from ine_sdk import AsyncINEClient, INEClient
from ine_sdk.classifiers import ClassifierType


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
