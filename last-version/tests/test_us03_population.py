import pytest
from src.continent import Continent
from src.pays import Pays

def test_us03_somme_population_simple():
    """Vérifie que 1 pays + 1 pays = somme correcte"""
    europe = Continent("Europe")
    
    # Création des pays
    fr = Pays("France", 100)
    de = Pays("Allemagne", 200)
    
    # Ajout
    europe.ajouter_pays(fr)
    europe.ajouter_pays(de)
    
    # Vérification (100 + 200 = 300)
    assert europe.population_totale() == 300

def test_us03_continent_vide():
    """Vérifie qu'un continent vide a 0 habitant"""
    antarctique = Continent("Antarctique")
    assert antarctique.population_totale() == 0