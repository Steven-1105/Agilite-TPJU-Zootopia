import pytest
from src.pays import Pays

def test_us02_calcul_densite_simple():
    """Test simple : Monaco"""
    monaco = Pays("Monaco", 39000, 2)
    assert monaco.calculer_densite() == 19500

def test_us02_calcul_densite_arrondi():
    """Test complexe : Russie (doit arrondir)"""
    russie = Pays("Russie", 144000000, 17000000)
    # 144 / 17 = 8.4705... -> doit devenir 8.47
    assert russie.calculer_densite() == 8.47

def test_us02_superficie_zero_impossible():
    """Michel ne doit pas diviser par zéro"""
    with pytest.raises(ValueError):
        Pays("Néant", 100, 0)
