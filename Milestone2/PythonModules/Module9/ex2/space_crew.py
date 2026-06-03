#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


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
    crew: list[CrewMember] = Field(..., min_items=1, max_items=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")

    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not any(
        member.rank in [Rank.commander, Rank.captain]
        for member in self.crew
        ):
            raise ValueError("Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            total_crew = len(self.crew)

            experienced_crew = sum(1 for member in self.crew if member.years_experience >= 5)

            if experienced_crew < total_crew * 0.5:
                raise ValueError(f"Long missions require at least {50%} experienced crew")
            
            if not all(member.is_active for member in self.crew):
                raise ValueError("All crew members must be active")
            return self


-----------------------------------------------
@model_validator(mode="after")
def validate_mission(self):
    # Rule 1
    if not self.mission_id.startswith("M"):
        raise ValueError('Mission ID must start with "M"')

    # Rule 2
    if not any(
        member.rank in [Rank.commander, Rank.captain]
        for member in self.crew
    ):
        raise ValueError(
            "Mission must have at least one Commander or Captain"
        )

    # Rule 3 (only long missions)
    if self.duration_days > 365:
        total_crew = len(self.crew)

        experienced_crew = sum(
            1 for member in self.crew
            if member.years_experience >= 5
        )

        if experienced_crew < total_crew * 0.5:
            raise ValueError(
                "Long missions require at least 50% experienced crew"
            )

    # Rule 4 (always applies)
    if not all(member.is_active for member in self.crew):
        raise ValueError("All crew members must be active")

    return self