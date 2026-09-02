"""Synchronous and Asynchronous clients for INE Classifiers API."""

from typing import Any, Dict, List, Union, cast
from chile_ine_sdk.classifiers.models import (
    ClassifierType,
    DigitLevel,
    PredictionRequest,
)
from chile_ine_sdk.http import AsyncHTTPClient, HTTPClient


class ClassifiersClient:
    """Synchronous client for INE Classifiers API (`rapps.ine.cl`)."""

    def __init__(self, http_client: HTTPClient) -> None:
        self._http = http_client

    def predict(
        self,
        text: Union[str, List[str]],
        classification: Union[ClassifierType, str],
        digits: DigitLevel,
        model_version: Union[str, int] = "latest",
    ) -> Dict[str, Any]:
        """Request CIUO or CAENES classification prediction.

        :param text: Input gloss or list of glosses.
        :param classification: Classifier taxonomy ('ciuo' or 'caenes').
        :param digits: Digit detail level (1 or 2).
        :param model_version: Model version ("latest" or integer).
        :return: JSON response from API.
        """
        payload = PredictionRequest(
            text=text,
            classification=ClassifierType(classification),
            digits=digits,
            model_version=model_version,
        )
        res = self._http.request(
            "POST",
            "/predict",
            json=payload.model_dump(mode="json"),
        )
        return cast(Dict[str, Any], res)

    def predict_ciuo(
        self,
        text: Union[str, List[str]],
        digits: DigitLevel = 1,
        model_version: Union[str, int] = "latest",
    ) -> Dict[str, Any]:
        """Convenience method for CIUO (Occupations) classification.

        :param text: Occupation description/tasks gloss.
        :param digits: Digit detail level (1 or 2).
        :param model_version: Model version.
        :return: Classification JSON.
        """
        return self.predict(
            text=text,
            classification=ClassifierType.CIUO,
            digits=digits,
            model_version=model_version,
        )

    def predict_caenes(
        self,
        text: Union[str, List[str]],
        digits: DigitLevel = 1,
        model_version: Union[str, int] = "latest",
    ) -> Dict[str, Any]:
        """Convenience method for CAENES (Economic Activities) classification.

        :param text: Economic activity description gloss.
        :param digits: Digit detail level (1 or 2).
        :param model_version: Model version.
        :return: Classification JSON.
        """
        return self.predict(
            text=text,
            classification=ClassifierType.CAENES,
            digits=digits,
            model_version=model_version,
        )

    def get_model_metadata(self) -> Dict[str, Any]:
        """Obtain metadata for available classification models.

        :return: Model metadata dictionary.
        """
        res = self._http.request("GET", "/get_model_metadata")
        return cast(Dict[str, Any], res)


class AsyncClassifiersClient:
    """Asynchronous client for INE Classifiers API (`rapps.ine.cl`)."""

    def __init__(self, http_client: AsyncHTTPClient) -> None:
        self._http = http_client

    async def predict(
        self,
        text: Union[str, List[str]],
        classification: Union[ClassifierType, str],
        digits: DigitLevel,
        model_version: Union[str, int] = "latest",
    ) -> Dict[str, Any]:
        """Request CIUO or CAENES classification prediction asynchronously.

        :param text: Input gloss or list of glosses.
        :param classification: Classifier taxonomy ('ciuo' or 'caenes').
        :param digits: Digit detail level (1 or 2).
        :param model_version: Model version ("latest" or integer).
        :return: JSON response from API.
        """
        payload = PredictionRequest(
            text=text,
            classification=ClassifierType(classification),
            digits=digits,
            model_version=model_version,
        )
        res = await self._http.request(
            "POST",
            "/predict",
            json=payload.model_dump(mode="json"),
        )
        return cast(Dict[str, Any], res)

    async def predict_ciuo(
        self,
        text: Union[str, List[str]],
        digits: DigitLevel = 1,
        model_version: Union[str, int] = "latest",
    ) -> Dict[str, Any]:
        """Convenience async method for CIUO (Occupations) classification.

        :param text: Occupation description/tasks gloss.
        :param digits: Digit detail level (1 or 2).
        :param model_version: Model version.
        :return: Classification JSON.
        """
        return await self.predict(
            text=text,
            classification=ClassifierType.CIUO,
            digits=digits,
            model_version=model_version,
        )

    async def predict_caenes(
        self,
        text: Union[str, List[str]],
        digits: DigitLevel = 1,
        model_version: Union[str, int] = "latest",
    ) -> Dict[str, Any]:
        """Convenience async method for CAENES (Economic Activities) classification.

        :param text: Economic activity description gloss.
        :param digits: Digit detail level (1 or 2).
        :param model_version: Model version.
        :return: Classification JSON.
        """
        return await self.predict(
            text=text,
            classification=ClassifierType.CAENES,
            digits=digits,
            model_version=model_version,
        )

    async def get_model_metadata(self) -> Dict[str, Any]:
        """Obtain metadata for available classification models asynchronously.

        :return: Model metadata dictionary.
        """
        res = await self._http.request("GET", "/get_model_metadata")
        return cast(Dict[str, Any], res)
