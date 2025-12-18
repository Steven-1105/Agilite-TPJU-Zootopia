from __future__ import annotations
from typing import List, TYPE_CHECKING

from .continent import Continent

class Pays:
    """
    Classe principale du projet représentant un pays.
    Auteurs : Liya _ Nada
    Version : 1.0
    """
    def __init__(self, nom="France", nb_habitant=66142961):
        # [cite_start]Initialisation des attributs nom et habitants [cite: 13]
        self._nom = nom
        self._nb_habitant = nb_habitant
        # [cite_start]Création automatique d'une instance de Capitale au démarrage [cite: 13]
        self._continent = Continent()

    # [cite_start]Getters et Setters [cite: 14]
    def get_nom(self):
        return self._nom

    def set_nom(self, n):
        self._nom = n

    def get_nb_habitant(self):
        return self._nb_habitant

    def set_nb_habitant(self, hab):
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

    def bonne_capitale(self, nom_c):
        """
        Vérifie si le nom proposé correspond à la capitale du pays.
        """
        return nom_c == self._capitale.get_nom()