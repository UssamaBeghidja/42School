#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from ex0.creatures import Flameling   # late import avoids circular
        return Flameling()

    def create_evolved(self) -> Creature:
        from ex0.creatures import Pyrodon
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        from ex0.creatures import Aquabub
        return Aquabub()

    def create_evolved(self) -> Creature:
        from ex0.creatures import Torragon
        return Torragon()
