from src.animal import Animal
from src.habitat import Habitat

def test_us03_can_survive_true_when_energy_enough():
    lion = Animal("Lion", 100)
    lion.set_habitat(Habitat("Savanna"))
    assert lion.can_survive() is True

def test_us03_can_survive_false_when_energy_too_low():
    weak = Animal("WeakLion", 10)
    weak.set_habitat(Habitat("Savanna"))  # needs = 30
    assert weak.can_survive() is False

def test_us03_move_to_costs_energy_and_sets_habitat():
    elephant = Animal("Elephant", 100)
    forest = Habitat("Forest")
    elephant.move_to(forest)
    assert elephant.get_habitat() == forest
    assert elephant.get_energy() == 90

def test_us03_move_to_fails_if_not_enough_energy():
    a = Animal("Tiny", 5)
    desert = Habitat("Desert")
    a.move_to(desert)
    assert a.get_habitat() is None
    assert a.get_energy() == 5
