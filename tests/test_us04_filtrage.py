import pytest
from src.continent import Continent
from src.pays import Pays

def test_us04_filtrage_petits_pays():
    """Vérifie que le filtre retient les petits et rejette les gros"""
    europe = Continent("Europe")
    
    # Création des données
    gros = Pays("France", 67000000)
    petit1 = Pays("Monaco", 30000)
    petit2 = Pays("Andorre", 70000)
    
    europe.ajouter_pays(gros)
    europe.ajouter_pays(petit1)
    europe.ajouter_pays(petit2)
    
    # Action : Filtrer à moins de 1 million
    resultat = europe.get_pays_population_max(1000000)
    
    # Vérifications
    assert len(resultat) == 2        # Doit en trouver 2
    assert gros not in resultat      # France exclue
    assert petit1 in resultat        # Monaco inclus