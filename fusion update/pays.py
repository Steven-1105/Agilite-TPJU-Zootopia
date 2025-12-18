from __future__ import annotations
from typing import List, TYPE_CHECKING

from .continent import Continent

class Pays:
    """
    Classe représentant un District de Zootopia.
    """
    def __init__(self, nom="Tundratown", nb_habitant=10000):
        # Initialisation des attributs de base
        self._nom : str = nom
        self._nb_habitant : int = nb_habitant
        
        # Récupération de l'unique instance de Zootopia (Singleton)
        self._continent : Continent = Continent()
        
        # ACTION DE FUSION : On s'ajoute automatiquement à la liste du continent
        self._continent.add_country(self)

    # Getters et Setters existants (Inchangés pour respecter la consigne)
    def get_nom(self):
        return self._nom

    def set_nom(self, n):
        self._nom = n

    def get_nb_habitant(self):
        return self._nb_habitant

    def set_nb_habitant(self, hab):
        if hab > 0:
            self._nb_habitant = hab

    def __str__(self):
        return f"Le district est {self._nom} et compte {self._nb_habitant} citoyens"

    def nouveaux_habitants(self, nb):
        """Met à jour le nombre d'habitants"""
        if nb > 0:
            self.set_nb_habitant(self.get_nb_habitant() + nb)
            
    def get_continent(self):
        """Retourne la ville (Zootopia) à laquelle appartient le district"""
        return self._continent