from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .pays import Pays

class Continent:
    """
    Représente la ville unique de Zootopia (Singleton).
    """
    _instance = None  # Stocke l'unique instance de la ville

    def __new__(cls, nom="Zootopia"):
        # Si aucune instance n'existe, on la crée
        if cls._instance is None:
            cls._instance = super(Continent, cls).__new__(cls)
            # On initialise les attributs une seule fois ici
            cls._instance._nom = nom
            cls._instance._pays = []
        return cls._instance

    def __init__(self, nom="Zootopia"):
        # L'initialisation est gérée par __new__ pour le Singleton
        pass

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def add_country(self, pays: Pays):
        """Ajoute un district (Pays) à la ville"""
        if pays not in self._pays:
            self._pays.append(pays)