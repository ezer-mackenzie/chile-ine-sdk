"""Pydantic models for INE Classifiers API (CIUO and CAENES)."""

from enum import StrEnum
from typing import Any, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field, field_validator


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

    @field_validator("classification", mode="before")
    @classmethod
    def normalize_classification(cls, v: Any) -> Any:
        if isinstance(v, str):
            return v.lower()
        return v


class PredictionItem(BaseModel):
    """Individual prediction result."""

    gloss: Optional[str] = Field(default=None, description="Input text gloss.")
    code: str = Field(..., description="Predicted code.")
    probability: float = Field(..., description="Model confidence probability.")
    label: Optional[str] = Field(default=None, description="Descriptive category label if available.")
    details: Dict[str, Any] = Field(default_factory=dict)


class PredictionResult(BaseModel):
    """Overall response for classification prediction."""

    predictions: List[PredictionItem] = Field(default_factory=list)
    classification: Optional[ClassifierType] = Field(default=None)
    digits: Optional[DigitLevel] = Field(default=None)
    model_version: Optional[str] = Field(default=None)
    raw_response: Dict[str, Any] = Field(default_factory=dict)
