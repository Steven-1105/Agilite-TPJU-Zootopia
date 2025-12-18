from behave import given, when, then
from src.animal import Animal
from src.habitat import Habitat

@given('un animal "{name}" avec {energy:d} d\'énergie')
def step_create_animal(context, name, energy):
    context.animal = Animal(name=name, energy=energy)

@given('un habitat "{habitat_type}"')
def step_create_habitat(context, habitat_type):
    context.habitat = Habitat(habitat_type)

@given('l\'animal vit dans "{habitat_type}"')
def step_animal_lives_in(context, habitat_type):
    h = Habitat(habitat_type)
    h.add_animal(context.animal)   
    context.habitat = h    


@when('l\'animal se déplace vers son habitat')
def step_move_to(context):
    context.animal.move_to(context.habitat)

@when('l\'animal calcule ses besoins journaliers')
def step_calc_needs(context):
    context.daily_needs = context.animal.calculate_daily_needs()

@when("l'animal mange {amount:d}")
def step_eat(context, amount):
    context.animal.eat(amount)

@when("l'animal vieillit")
def step_grow_old(context):
    context.animal.grow_old()

@when("l'animal vieillit {n:d} fois")
def step_grow_old_n(context, n):
    for _ in range(n):
        context.animal.grow_old()

@when("l'animal tente de se déplacer vers son habitat")
def step_try_move_to(context):
    context.move_ok = context.animal.move_to(context.habitat)

@then("le déplacement est accepté")
def step_move_accepted(context):
    assert context.move_ok is True

@then("le déplacement est refusé")
def step_move_refused(context):
    assert context.move_ok is False

@then("l'animal peut survivre")
def step_can_survive(context):
    assert context.animal.can_survive() is True

@then("l'animal ne peut pas survivre")
def step_cannot_survive(context):
    assert context.animal.can_survive() is False

@then('l\'animal vit dans "{habitat_type}"')
def step_check_habitat(context, habitat_type):
    assert context.animal.habitat is not None
    assert context.animal.habitat.get_type() == habitat_type

@then('l\'énergie de l\'animal est {expected:d}')
def step_check_energy(context, expected):
    assert context.animal.get_energy() == expected

@then('le besoin journalier est {expected:d}')
def step_check_daily_needs(context, expected):
    assert context.daily_needs == expected

@then("l'âge de l'animal est {age:d}")
def step_age_is(context, age):
    assert context.animal.age == age

@then("l'énergie de l'animal est {energy:d}")
def step_energy_is(context, energy):
    assert context.animal.energy == energy
