from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from .habitat import Habitat


@dataclass
class Animal:
    """
    Classe représentant un animal dans le système.
    Un animal possède un nom, une énergie, un âge et éventuellement un habitat.
    """

    name: str
    energy: int
    age: int = 0
    habitat: Optional[Habitat] = None

    # ----------------------
    # Accesseurs (getters)
    # ----------------------
    def get_name(self) -> str:
        return self.name

    def get_energy(self) -> int:
        return self.energy

    def get_age(self) -> int:
        return self.age

    def get_habitat(self) -> Optional[Habitat]:
        return self.habitat

    def set_habitat(self, habitat: Optional[Habitat]) -> None:
        """
        Setter public de l'habitat.
        Pour garantir la cohérence bidirectionnelle,
        il est recommandé d'utiliser move_to() ou leave_habitat().
        """
        self.habitat = habitat

    # -------------------------------------------------
    # Méthode interne utilisée uniquement par Habitat
    # pour maintenir la cohérence bidirectionnelle
    # -------------------------------------------------
    def _set_habitat_internal(self, habitat: Optional[Habitat]) -> None:
        self.habitat = habitat

    # ----------------------
    # Comportements métier
    # ----------------------
    def eat(self, amount: int) -> None:
        """
        L'animal mange et augmente son énergie.
        Une quantité négative est interdite.
        """
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.energy += amount

    def grow_old(self) -> None:
        """
        L'animal vieillit :
        - l'âge augmente de 1
        - l'énergie diminue de 5 (sans jamais devenir négative)
        """
        self.age += 1
        self.energy = max(0, self.energy - 5)

    def move_to(self, habitat: Habitat) -> bool:
        """
        Déplace l'animal vers un nouvel habitat.
        Règles :
        - nécessite au moins 10 points d'énergie
        - coûte 10 points d'énergie uniquement si le déplacement est effectif
        - délègue la gestion de la relation à Habitat (cohérence bidirectionnelle)
        """
        if self.energy < 10:
            return False

        if self.habitat is habitat:
            # Déjà dans cet habitat : aucun changement
            return False

        success = habitat.add_animal(self)
        if success:
            self.energy -= 10
        return success

    def leave_habitat(self) -> bool:
        """
        Retire l'animal de son habitat actuel.
        """
        if self.habitat is None:
            return False
        return self.habitat.remove_animal(self)

    def has_habitat(self) -> bool:
        return self.habitat is not None

    def describe(self) -> str:
        """
        Retourne une description textuelle de l'animal.
        """
        return f"{self.name} ({self.energy} energy) {self._habitat_label()}"

    def _habitat_label(self) -> str:
        """
        Méthode extraite (refactoring) pour formater la partie habitat.
        """
        if self.has_habitat():
            return f"lives in {self.habitat.get_type()}"
        return "is homeless"

    # -------------------------------------------------
    # Refactoring : renommage + extraction de méthode
    # -------------------------------------------------
    def daily_energy_need(self) -> int:
        """
        Calcule le besoin énergétique journalier de l'animal.
        Remplace l'ancienne méthode calculate_daily_needs.
        """
        if self.habitat is None:
            return 20
        return self._need_for_habitat_type(self.habitat.get_type())

    # Méthode conservée pour compatibilité
    def calculate_daily_needs(self) -> int:
        return self.daily_energy_need()

    def _need_for_habitat_type(self, habitat_type: str) -> int:
        """
        Méthode extraite qui associe un type d'habitat
        à un besoin énergétique.
        """
        mapping = {
            "Desert": 40,
            "Forest": 25,
            "Savanna": 30,
            "Mountain": 35,
        }
        return mapping.get(habitat_type, 20)

    def can_survive(self) -> bool:
        """
        Indique si l'animal peut survivre dans son habitat actuel.
        """
        return self.energy >= self.daily_energy_need()
