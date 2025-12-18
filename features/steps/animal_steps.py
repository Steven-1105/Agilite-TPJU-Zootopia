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
    context.animal.set_habitat(Habitat(habitat_type))

@when('l\'animal se déplace vers son habitat')
def step_move_to(context):
    context.animal.move_to(context.habitat)

@when('l\'animal calcule ses besoins journaliers')
def step_calc_needs(context):
    context.daily_needs = context.animal.calculate_daily_needs()

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
