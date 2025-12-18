import pytest
from src.continent import Continent

def test_us06_creation_unique_zootopia():
    """
    Vérifie que la première création fonctionne.
    """
    # 1. On nettoie tout avant de commencer (Vital !)
    Continent.reset_instance()
    
    # 2. La première fois, ça doit marcher
    c1 = Continent("Zootopia")
    assert c1.get_nom() == "Zootopia"

def test_us06_blocage_double_creation():
    """
    Vérifie que le système LÈVE UNE ERREUR si on crée un 2ème continent.
    """
    Continent.reset_instance()
    
    # 1. On crée le premier (Zootopia)
    c1 = Continent("Zootopia")
    
    # 2. On essaie de créer le deuxième (Atlantis)
    # Le test réussit SEULEMENT si une Exception est levée
    with pytest.raises(Exception) as info_erreur:
        c2 = Continent("Atlantis")
    
    # 3. On vérifie que le message est bien celui qu'on a défini
    # (Adapté à ta dernière phrase Gherkin)
    message_recu = str(info_erreur.value)
    assert "Zootopia est l'unique continent" in message_recu

def test_us06_reset_fonctionne():
    """
    Vérifie que reset_instance() permet bien de recommencer.
    (Important pour tes autres tests)
    """
    Continent.reset_instance()
    c1 = Continent("Zootopia")
    
    # On détruit le monde
    Continent.reset_instance()
    
    # On doit pouvoir recréer un continent sans erreur maintenant
    try:
        c2 = Continent("NouveauMonde")
        assert c2.get_nom() == "NouveauMonde"
    except Exception:
        pytest.fail("Le reset_instance() n'a pas fonctionné, le Singleton est resté bloqué.")