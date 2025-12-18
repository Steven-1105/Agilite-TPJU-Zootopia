from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .animal import Animal


class Habitat:
    """
    Classe représentant un habitat.
    Un habitat peut contenir plusieurs animaux (0..*).
    """

    def __init__(self, habitat_type: str):
        self._type = habitat_type
        self._animals: List["Animal"] = []

    def get_type(self) -> str:
        return self._type

    def get_animals(self) -> list["Animal"]:
        """
        Retourne une copie de la liste des animaux
        afin de préserver l'encapsulation.
        """
        return list(self._animals)

    def add_animal(self, animal: "Animal") -> bool:
        """
        Ajoute un animal à l'habitat en garantissant :
        - absence de doublons
        - cohérence bidirectionnelle Animal ↔ Habitat
        - migration correcte depuis un ancien habitat
        """
        if animal in self._animals:
            return False

        # Si l’animal appartenait à un autre habitat,
        # on le retire d’abord de celui-ci
        old_habitat = animal.get_habitat()
        if old_habitat is not None and old_habitat is not self:
            old_habitat.remove_animal(animal)

        self._animals.append(animal)
        animal._set_habitat_internal(self)
        return True

    def remove_animal(self, animal: "Animal") -> bool:
        """
        Retire un animal de l'habitat.
        L'opération est sûre même si l'animal n'est pas présent.
        """
        if animal not in self._animals:
            return False

        self._animals.remove(animal)

        if animal.get_habitat() is self:
            animal._set_habitat_internal(None)
        return True

    def __str__(self) -> str:
        return self._type
