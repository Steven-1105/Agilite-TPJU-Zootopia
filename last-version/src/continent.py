class Continent:
    """
    Représente la capitale d'un pays.
    Auteurs : Liya _ Nada
    Version : 1.0
    """
    def __init__(self, nom="Europe"):
        # [cite_start]Initialisation de l'attribut nom avec une valeur par défaut [cite: 13]
        self._nom = nom

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom