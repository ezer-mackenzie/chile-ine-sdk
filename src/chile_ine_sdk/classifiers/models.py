"""Pydantic models for INE Classifiers API (CIUO and CAENES)."""

from enum import StrEnum
from typing import Any, Dict, List, Literal, Union
from pydantic import BaseModel, Field


class ClassifierType(StrEnum):
    """Classifier taxonomy name."""

    CIUO = "ciuo"
    CAENES = "caenes"


DigitLevel = Literal[1, 2]


class PredictionRequest(BaseModel):
    """Payload for classification prediction endpoint."""

    text: Union[str, List[str]] = Field(
        ...,
        description="Text gloss or list of text glosses to classify.",
    )
    classification: ClassifierType = Field(
        ...,
        description="Classifier taxonomy ('ciuo' or 'caenes').",
    )
    digits: DigitLevel = Field(
        ...,
        description="Level of detail (1 or 2 digits).",
    )
    model_version: Union[str, int] = Field(
        default="latest",
        description="Model version to use for prediction.",
    )


class PredictionItem(BaseModel):
    """Individual prediction result."""

    gloss: str = Field(..., description="Input text gloss.")
    code: str = Field(..., description="Predicted code.")
    probability: float = Field(..., description="Model confidence probability.")
    details: Dict[str, Any] = Field(default_factory=dict)


class PredictionResult(BaseModel):
    """Overall response for classification prediction."""

    predictions: List[PredictionItem] = Field(default_factory=list)
    raw_response: Dict[str, Any] = Field(default_factory=dict)
