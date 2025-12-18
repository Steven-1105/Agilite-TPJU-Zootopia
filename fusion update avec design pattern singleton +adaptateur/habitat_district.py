from .habitat import Habitat
from .pays import Pays

class HabitatDistrict(Habitat):
    """
    ADAPTATEUR : Cette classe hérite de Habitat (Projet Bio)
    et prend un Pays (Projet Géo) comme argument pour les lier.
    """
    def __init__(self, habitat_type: str, district: Pays):
        # On initialise la classe mère (Habitat) normalement
        super().__init__(habitat_type)
        # On ajoute la liaison avec le projet Géo
        self._district = district

    def get_district(self) -> Pays:
        return self._district

    def __str__(self) -> str:
        return f"{self._type} situé dans le district {self._district.get_nom()}"