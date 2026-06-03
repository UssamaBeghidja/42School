#!/usr/bin/env python3
from abc import ABC, abstractmethod


class HealCapability(ABC):          # does NOT inherit from Creature!
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):      # does NOT inherit from Creature!
    def __init__(self) -> None:
        self.transformed: bool = False  # persistent state!

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
