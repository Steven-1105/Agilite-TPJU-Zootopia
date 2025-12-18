from __future__ import annotations
from typing import List, TYPE_CHECKING

from .pays import Pays

class Continent:
    """
    Représente la capitale d'un pays.
    Auteurs : Liya _ Nada
    Version : 1.0
    """
    def __init__(self, nom="Europe"):
        # [cite_start]Initialisation de l'attribut nom avec une valeur par défaut [cite: 13]
        self._nom : str = nom
        self._pays : List["Pays"] = []

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def ajouter_pays(self, pays):
        if pays in self._pays:
            raise ValueError(f"Doublon détecté : {pays.get_nom()} existe déjà !")
        if pays not in self._pays:
            self._pays.append(pays)