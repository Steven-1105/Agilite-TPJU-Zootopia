from src.animal import Animal
from src.habitat import Habitat

def test_us02_daily_needs_without_habitat_is_20():
    homeless = Animal("Homeless", 100)
    assert homeless.calculate_daily_needs() == 20

def test_us02_daily_needs_savanna_is_30():
    lion = Animal("Lion", 100)
    lion.set_habitat(Habitat("Savanna"))
    assert lion.calculate_daily_needs() == 30

def test_us02_daily_needs_forest_is_25():
    e = Animal("Elephant", 100)
    e.set_habitat(Habitat("Forest"))
    assert e.calculate_daily_needs() == 25

def test_us02_daily_needs_desert_is_40():
    c = Animal("Camel", 100)
    c.set_habitat(Habitat("Desert"))
    assert c.calculate_daily_needs() == 40
