"""Pydantic models for INE SIMEL API."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class Indicator(BaseModel):
    """SIMEL statistical indicator header."""

    id: str = Field(..., description="Indicator unique identifier.")
    name: str = Field(..., description="Indicator description/title.")
    category: Optional[str] = Field(default=None, description="Category / domain.")
    unit: Optional[str] = Field(default=None, description="Unit of measurement.")


class Observation(BaseModel):
    """Individual statistical observation data point."""

    period: str = Field(..., description="Time period (e.g., '2024-Q1', '2024-01').")
    value: Optional[float] = Field(default=None, description="Observed numeric value.")
    dimensions: Dict[str, Any] = Field(
        default_factory=dict, description="Dimensional attributes."
    )


class IndicatorData(BaseModel):
    """Container for indicator statistical time series."""

    indicator_id: str
    observations: List[Observation] = Field(default_factory=list)
