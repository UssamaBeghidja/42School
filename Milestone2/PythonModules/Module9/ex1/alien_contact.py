#!/usr/bin/env python3

from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
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
    def validate_contact_rules(self):
    # Rule 1
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # Rule 2
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")

        # Rule 3
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        # Rule 4
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a message")

        return self
-----------------------------------------------------------------------

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

from pydantic import BaseModel, Field, model_validator


class ContactType(str, Enum):
    """
    Enumeration of possible alien contact types.
    """

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """
    Model representing a validated alien contact report.
    """

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
    def validate_contact_rules(self):
        """
        Applies business rules after standard field validation.
        """

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
        if (
            self.signal_strength > 7.0
            and not self.message_received
        ):
            raise ValueError(
                "Strong signals must include a message"
            )

        return self