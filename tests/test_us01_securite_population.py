import pytest
from src.pays import Pays
from src.continent import Continent

# ----------------------------------------------------------------
# TEST US-01 : SÉCURITÉ ANTI-ZOMBIES
# ----------------------------------------------------------------

def test_us01_create_pays_negative_population_raises_error():
    with pytest.raises(ValueError) as excinfo:
        Pays("Zombieland", -500)
    assert "Erreur : La population ne peut pas être négative !" in str(excinfo.value)

def test_us01_update_population_negative_raises_error():
    p = Pays("TestLand", 100)
    with pytest.raises(ValueError):
        p.set_nb_habitant(-10)

# ----------------------------------------------------------------
# TEST US-01 : INTÉGRITÉ ANTI-CLONES
# ----------------------------------------------------------------

def test_us01_add_duplicate_pays_raises_error():
    europe = Continent("Europe")
    p1 = Pays("France", 1000)
    europe.ajouter_pays(p1)

    p2_clone = Pays("France", 2000)

    with pytest.raises(ValueError) as excinfo:
        europe.ajouter_pays(p2_clone)
    
    assert "Doublon détecté" in str(excinfo.value)