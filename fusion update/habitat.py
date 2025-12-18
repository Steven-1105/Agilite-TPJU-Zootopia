from __future__ import annotations
from typing import List, TYPE_CHECKING

# Importation pour la fusion avec le projet Géographie
if TYPE_CHECKING:
    from .animal import Animal
    from .pays import Pays # Importation de la classe Pays (District)

class Habitat:
    """
    Classe représentant un habitat (ex: Banquise).
    Un habitat appartient à un Pays (District de Zootopia).
    """

    def __init__(self, habitat_type: str, district: Pays = None):
        # Attributs d'origine conservés
        self._type = habitat_type
        self._animals: List["Animal"] = []
        
        # AJOUT POUR LA FUSION : Lien vers le projet Géographie
        self._district = district

    def get_type(self) -> str:
        return self._type

    def get_district(self) -> Pays:
        """Retourne le district (Pays) où se situe cet habitat."""
        return self._district

    def get_animals(self) -> list["Animal"]:
        return list(self._animals)

    def add_animal(self, animal: "Animal") -> bool:
        """
        Ajoute un animal à l'habitat en garantissant la cohérence.
        """
        if animal in self._animals:
            return False

        old_habitat = animal.get_habitat()
        if old_habitat is not None and old_habitat is not self:
            old_habitat.remove_animal(animal)

        self._animals.append(animal)
        animal._set_habitat_internal(self)
        return True

    def remove_animal(self, animal: "Animal") -> bool:
        """Retire un animal de l'habitat."""
        if animal not in self._animals:
            return False

        self._animals.remove(animal)

        if animal.get_habitat() is self:
            animal._set_habitat_internal(None)
        return True

    def __str__(self) -> str:
        # Storytelling : Affiche l'habitat et son district
        district_nom = self._district.get_nom() if self._district else "Inconnu"
        return f"Habitat {self._type} situé dans le district {district_nom}"