#!/usr/bin/env python3

"""
alien_contact.py

Exercise 1 - Alien Contact Validation

This module defines a Pydantic model with advanced business rules
using @model_validator(mode="after") to validate alien contact reports.
"""

from enum import Enum
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enumeration of possible alien contact types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Model representing a validated alien contact report."""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Applies business rules after standard field validation."""

        # Rule 1: Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # Rule 2: Physical contact must be verified
        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError("Physical contact must be verified")

        # Rule 3: Telepathic contact requires at least 3 witnesses
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        # Rule 4: Strong signals must include a message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a message")

        return self


def main() -> None:
    """Run validation demo for AlienContact model."""

    print("Alien Contact Log Validation")
    print("=" * 38)

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-06-01T22:15:00",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as exc:
        print("Validation error (unexpected):")
        print(exc)

    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-06-01T23:00:00",
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=1,
        )

    except ValidationError as exc:
        print("Expected validation error:")
        print(exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
