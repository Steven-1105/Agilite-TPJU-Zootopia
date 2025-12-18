from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any

if TYPE_CHECKING:
    from .habitat import Habitat
    from .pays import Pays
    from .animal import Animal


class HabitatDistrict:
    """Adapter (Pattern Adaptateur)

    Objectif : relier un Habitat (biologie) à un Pays (géographie) sans casser
    le code existant.

    - On *enveloppe* (composition) un Habitat.
    - On lui associe officiellement un district (Pays).

    Cette classe expose la *même interface utile* qu'un Habitat pour que les
    animaux puissent continuer à l'utiliser (duck typing) :
      - get_type(), get_animals(), add_animal(), remove_animal()
    """

    def __init__(self, habitat: "Habitat", district: "Pays"):
        self._habitat: Habitat = habitat
        self._district: Pays = district

        # Optionnel : si l'Habitat fusionné possède déjà un champ _district,
        # on le synchronise pour garder une traçabilité cohérente.
        if hasattr(self._habitat, "_district"):
            setattr(self._habitat, "_district", district)

    # --- Partie "Habitat" (délégation) ---
    def get_type(self) -> str:
        return self._habitat.get_type()

    def get_animals(self) -> list["Animal"]:
        return self._habitat.get_animals()

    def add_animal(self, animal: "Animal") -> bool:
        return self._habitat.add_animal(animal)

    def remove_animal(self, animal: "Animal") -> bool:
        return self._habitat.remove_animal(animal)

    # --- Partie "District" (géographie) ---
    def get_district(self) -> "Pays":
        return self._district

    def set_district(self, district: "Pays") -> None:
        self._district = district
        if hasattr(self._habitat, "_district"):
            setattr(self._habitat, "_district", district)

    # --- Accès à l'objet Habitat original si besoin ---
    def unwrap(self) -> "Habitat":
        """Retourne l'Habitat d'origine (utile pour debug/tests)."""
        return self._habitat

    def __str__(self) -> str:
        district_nom = (
            self._district.get_nom() if hasattr(self._district, "get_nom") else str(self._district)
        )
        return f"HabitatDistrict({self.get_type()} -> {district_nom})"
