from .animal import Animal

class ZootopiaFactory:
    """
    Design Pattern: Factory
    Permet de créer des citoyens de Zootopia sans modifier 
    la classe Animal d'origine.
    """
    
    @staticmethod
    def create_police_officer(name: str) -> Animal:
        # Un officier (ex: Judy) commence avec beaucoup d'énergie
        return Animal(name=name, energy=100, age=24)

    @staticmethod
    def create_civilian(name: str, species_type: str) -> Animal:
        # Un civil standard
        energy_levels = {"Fox": 60, "Rabbit": 50, "Sloth": 20}
        energy = energy_levels.get(species_type, 40)
        return Animal(name=name, energy=energy, age=25)