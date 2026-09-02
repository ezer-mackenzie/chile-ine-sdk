"""Pydantic models for INE SIMEL API with optional Pandas / Polars DataFrame export."""

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

    def to_pandas(self) -> Any:
        """Export observations to a pandas DataFrame.

        :raises ImportError: If pandas is not installed.
        :return: pandas DataFrame containing time series observations.
        """
        try:
            import pandas as pd  # type: ignore[import-untyped]
        except ImportError as exc:
            raise ImportError(
                "pandas is required for DataFrame conversion. Install it with: pip install 'chile-ine-sdk[pandas]'"
            ) from exc

        records = [
            {"indicator_id": self.indicator_id, "period": obs.period, "value": obs.value, **obs.dimensions}
            for obs in self.observations
        ]
        return pd.DataFrame(records)

    def to_polars(self) -> Any:
        """Export observations to a polars DataFrame.

        :raises ImportError: If polars is not installed.
        :return: polars DataFrame containing time series observations.
        """
        try:
            import polars as pl  # type: ignore[import-not-found]
        except ImportError as exc:
            raise ImportError(
                "polars is required for DataFrame conversion. Install it with: pip install 'chile-ine-sdk[polars]'"
            ) from exc

        records = [
            {"indicator_id": self.indicator_id, "period": obs.period, "value": obs.value, **obs.dimensions}
            for obs in self.observations
        ]
        return pl.DataFrame(records)
