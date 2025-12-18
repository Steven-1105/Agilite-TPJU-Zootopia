import pytest
from src.pays import Pays
from src.continent import Continent

# ----------------------------------------------------------------
# TEST US-01 : SÉCURITÉ ANTI-ZOMBIES (Population)
# ----------------------------------------------------------------

def test_us01_create_pays_valid_state():
    """Vérifie qu'un pays normal est créé correctement."""
    france = Pays("France", 67000000)
    assert france.get_nom() == "France"
    assert france.get_nb_habitant() == 67000000

def test_us01_create_pays_negative_population_raises_error():
    """Vérifie que la création avec population négative est rejetée (Zombie)."""
    with pytest.raises(ValueError) as excinfo:
        Pays("Zombieland", -500)
    # On vérifie optionnellement que le message est le bon
    assert "Pas de zombies ici" in str(excinfo.value)

def test_us01_update_population_negative_raises_error():
    """Vérifie que la modification vers une population négative est rejetée."""
    p = Pays("TestLand", 100)
    with pytest.raises(ValueError):
        p.set_nb_habitant(-10)

# ----------------------------------------------------------------
# TEST US-01 : INTÉGRITÉ ANTI-CLONES (Doublons)
# ----------------------------------------------------------------

def test_us01_add_pays_to_continent_works():
    """Vérifie l'ajout normal d'un pays."""
    europe = Continent("Europe")
    france = Pays("France", 1000)
    
    europe.ajouter_pays(france)
    
    # On vérifie que le pays est bien dans la liste
    assert france in europe._pays 

def test_us01_add_duplicate_pays_raises_error():
    """Vérifie que l'ajout d'un doublon (même nom) est rejeté."""
    europe = Continent("Europe")
    p1 = Pays("France", 1000)
    europe.ajouter_pays(p1) # Premier ajout OK

    # Tentative de clone (Nouvel objet, mais même nom)
    p2_clone = Pays("France", 2000)

    with pytest.raises(ValueError) as excinfo:
        europe.ajouter_pays(p2_clone)
    
    assert "Doublon détecté" in str(excinfo.value)