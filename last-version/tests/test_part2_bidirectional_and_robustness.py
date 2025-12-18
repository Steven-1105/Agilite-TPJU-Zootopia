from src.animal import Animal
from src.habitat import Habitat


def test_bidirectional_add_animal_sets_animal_habitat():
    h = Habitat("Savanna")
    a = Animal("Lion", 100)
    assert h.add_animal(a) is True
    assert a.get_habitat() is h
    assert a in h.get_animals()


def test_bidirectional_no_duplicate_animals():
    h = Habitat("Forest")
    a = Animal("Panda", 80)
    assert h.add_animal(a) is True
    assert h.add_animal(a) is False
    assert h.get_animals().count(a) == 1


def test_migration_between_habitats_keeps_consistency():
    h1 = Habitat("Savanna")
    h2 = Habitat("Desert")
    a = Animal("Camel", 120)

    assert h1.add_animal(a) is True
    assert a.get_habitat() is h1
    assert a in h1.get_animals()

    assert h2.add_animal(a) is True  # migrate
    assert a.get_habitat() is h2
    assert a in h2.get_animals()
    assert a not in h1.get_animals()


def test_remove_non_existing_animal_is_safe():
    h = Habitat("Savanna")
    a = Animal("Elephant", 100)
    assert h.remove_animal(a) is False


def test_move_to_costs_energy_only_when_moved():
    h = Habitat("Forest")
    a = Animal("Elephant", 100)

    assert a.move_to(h) is True
    assert a.get_energy() == 90

    # already there -> no second cost and no change
    assert a.move_to(h) is False
    assert a.get_energy() == 90


def test_move_to_fails_if_energy_low():
    h = Habitat("Forest")
    a = Animal("Tiny", 5)
    assert a.move_to(h) is False
    assert a.get_habitat() is None
    assert a.get_energy() == 5


def test_leave_habitat_updates_both_sides():
    h = Habitat("Savanna")
    a = Animal("Lion", 100)
    h.add_animal(a)

    assert a.leave_habitat() is True
    assert a.get_habitat() is None
    assert a not in h.get_animals()
