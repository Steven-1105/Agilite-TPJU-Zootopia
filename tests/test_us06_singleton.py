import pytest
from src.continent import Continent

def test_us06_singleton_identity():
    """
    Vérifie que deux appels renvoient bien la MÊME instance mémoire.
    C'est la définition pure du Singleton.
    """
    # Reset manuel pour être sûr
    Continent._instance = None
    
    c1 = Continent("Zootopia")
    c2 = Continent("Atlantis") 
    
    # TEST ULTIME : Est-ce que c1 et c2 sont le même objet ?
    # Si oui, le Singleton fonctionne.
    assert c1 is c2
    assert id(c1) == id(c2)

def test_us06_soft_reset_behavior():
    """
    Vérifie le comportement 'Soft Singleton' que tu as choisi :
    L'objet reste le même, mais les données sont remises à zéro
    quand on rappelle Continent().
    """
    Continent._instance = None
    c1 = Continent("Zootopia")
    
    # On modifie c1 pour "salir" l'objet
    c1._nom = "Modified"
    
    # On rappelle le constructeur (ce que font tes tests Behave)
    c2 = Continent("Zootopia")
    
    # 1. C'est toujours le même objet (Singleton)
    assert c1 is c2
    
    # 2. MAIS le nom est redevenu "Zootopia" car __init__ a été rappelé
    # C'est ce comportement qui permet à tes tests Behave de fonctionner sans erreurs !
    assert c2.get_nom() == "Zootopia"
    assert c1.get_nom() == "Zootopia" # c1 a aussi changé car c'est le même objet