#!/usr/bin/env python3

"""
space_station.py

Exercise 0 - Space Station Data Validation

Defines a Pydantic model to validate space station telemetry data
and demonstrates validation for both valid and invalid inputs.
"""

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Represents a space station with validated operational parameters."""

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """Run validation demo for SpaceStation model."""

    print("Space Station Data Validation")
    print("=" * 40)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T08:00:00",
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            "Status: "
            f"{'Operational' if station.is_operational else 'Offline'}"
        )

    except ValidationError as exc:
        print("Validation error (unexpected):")
        print(exc)

    print("=" * 40)

    try:
        SpaceStation(
            station_id="BAD01",
            name="Overcrowded Station",
            crew_size=50,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance="2024-01-15T08:00:00",
        )

    except ValidationError as exc:
        print("Expected validation error:")
        print(exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
