from __future__ import annotations
from typing import List, TYPE_CHECKING

from .pays import Pays

class Continent:
    """
    Représente la capitale d'un pays.
    Auteurs : Liya _ Nada
    Version : 1.0
    """
    _instances = {}

    def __new__(cls, nom, reset=False):
        if reset or nom not in cls._instances:
            instance = super().__new__(cls)
            instance._nom = nom
            instance._pays = []
            cls._instances[nom] = instance
        return cls._instances[nom]
    
    
    # L'initialisation est gérée par __new__ pour le Singleton
    def __init__(self, nom="Europe", reset=False):
        # [cite_start]Initialisation de l'attribut nom avec une valeur par défaut [cite: 13]
        self._nom : str = nom
        self._pays : List["Pays"] = []
        if reset or not hasattr(self, "_pays"):
            self._nom = nom
            self._pays = []
    
    
    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def ajouter_pays(self, pays: "Pays"):
        # --- AJOUT US-01 ANTI-CLONE ---
        for p in self._pays:
            if p.get_nom() == pays.get_nom():
                raise ValueError(f"Doublon détecté : {pays.get_nom()} existe déjà !")
        # Si pas de doublon trouvé, on ajoute
        self._pays.append(pays)

    # --- AJOUT US-03 : L'AGRÉGATION ---
    def population_totale(self):
        """
        Interroge chaque pays et fait la somme.
        C'est la méthode "Calculatrice de Michel".
        """
        total = 0
        for p in self._pays:
            # On demande gentiment à chaque pays sa population
            total += p.get_nb_habitant()
        return total
    
    # --- AJOUT US-04 : LE FILTRAGE ---
    def get_pays_population_max(self, seuil_population: int):
        """
        Retourne une nouvelle liste contenant uniquement les pays
        dont la population est STRICTEMENT inférieure au seuil.
        """
        resultat = []
        for p in self._pays:
            if p.get_nb_habitant() < seuil_population:
                resultat.append(p)
        return resultat