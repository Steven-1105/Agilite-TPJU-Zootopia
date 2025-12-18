from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .continent import Continent

class Pays:
    """
    Classe principale du projet représentant un pays.
    Auteurs : Liya _ Nada
    Version : 1.0
    """
    def __init__(self, nom, nb_habitant=66142961, continent= None):
        # [cite_start]Initialisation des attributs nom et habitants [cite: 13]
        self._nom : str = nom

        # BOUCLIER ANTI-ZOMBIES
        if nb_habitant < 0:
            raise ValueError("Erreur : La population ne peut pas être négative !")
        self._nb_habitant : int = nb_habitant
        
        self._continent = continent # On le stocke d'abord
        if continent is not None:
            # On appelle la méthode SUR l'objet continent
            continent.ajouter_pays(self)

    # [cite_start]Getters et Setters [cite: 14]
    def get_nom(self):
        return self._nom

    def set_nom(self, n):
        self._nom = n

    def get_nb_habitant(self):
        return self._nb_habitant

    def set_nb_habitant(self, hab):
        # Le setter doit aussi bloquer les zombies !
        if hab < 0:
            raise ValueError("Erreur : La population ne peut pas être négative !")
        self._nb_habitant = hab

    def set_capitale(self, c):
        self._capitale = c

    def __str__(self):
        """Équivalent du toString() en Java"""
        return f"Mon pays est {self._nom} et je compte {self._nb_habitant} habitants"

    def nouveaux_habitants(self, nb):
        """
        Met à jour le nombre d'habitants si le nombre est positif.
        """
        if nb > 0:
            self.set_nb_habitant(self.get_nb_habitant() + nb)
