import pytest
from src.animal import Animal

def test_us01_create_animal_has_initial_state():
    tigre = Animal("Tiger", 80)
    assert tigre.get_name() == "Tiger"
    assert tigre.get_energy() == 80
    assert tigre.get_age() == 0
    assert tigre.get_habitat() is None

def test_us01_eat_increases_energy():
    lion = Animal("Lion", 100)
    lion.eat(50)
    assert lion.get_energy() == 150

def test_us01_eat_negative_is_rejected():
    zebra = Animal("Zebra", 60)
    with pytest.raises(ValueError):
        zebra.eat(-10)

def test_us01_grow_old_increases_age_and_decreases_energy():
    a = Animal("Tiger", 80)
    a.grow_old()
    assert a.get_age() == 1
    assert a.get_energy() == 75
