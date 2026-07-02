#!/usr/bin/env python3

"""
space_crew.py

Exercise 2 - Space Crew Management

Defines nested Pydantic models for crew members and missions, with
custom cross-field validation for launch safety requirements.
"""

from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        # Rule 1: Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Rule 2: Must have at least one Commander or Captain
        if not any(
            member.rank in [Rank.commander, Rank.captain]
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Rule 3: Long missions need 50% experienced crew (only for
        # missions longer than 365 days)
        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced_crew = sum(
                1 for member in self.crew if member.years_experience >= 5
            )

            if experienced_crew < total_crew * 0.5:
                raise ValueError(
                    "Long missions require at least 50% experienced crew"
                )

        # Rule 4: All crew members must be active — applies to every
        # mission, not just long ones, so this stays outside the
        # duration_days check above.
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Run validation demo for SpaceMission model."""

    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-09-01T06:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=42,
                    specialization="Mission Command",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=29,
                    specialization="Engineering",
                    years_experience=6,
                ),
            ],
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )

    except ValidationError as exc:
        print("Validation error (unexpected):")
        print(exc)

    print("=" * 41)

    try:
        SpaceMission(
            mission_id="M2024_LUNA",
            mission_name="Lunar Survey",
            destination="Moon",
            launch_date="2024-10-01T06:00:00",
            duration_days=30,
            budget_millions=150.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Wilson",
                    rank=Rank.cadet,
                    age=24,
                    specialization="Logistics",
                    years_experience=1,
                ),
            ],
        )

    except ValidationError as exc:
        print("Expected validation error:")
        msg = exc.errors()[0]["msg"]
        print(msg.removeprefix("Value error, "))


if __name__ == "__main__":
    main()
