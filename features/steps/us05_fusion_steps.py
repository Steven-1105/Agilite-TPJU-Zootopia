from behave import given, when, then
from src.animal import Animal
from src.pays import Pays
from src.continent import Continent
from src.habitat_district import HabitatDistrict
from src.habitat import Habitat

WORLD = {}

@given('le pays "{nom_pays}" avec {pop:d} habitants dans "{nom_cont}"')
def step_add_country(context, nom_pays, pop, nom_cont):
    c = WORLD.get(nom_cont)
    if c is None:
        try:
            c = Continent(nom_cont, reset=True)
        except TypeError:
            c = Continent(nom_cont)
        WORLD[nom_cont] = c

    p = Pays(nom_pays, pop)
    
    if hasattr(c, "ajouter_pays"):
        c.ajouter_pays(p)
    elif hasattr(c, "add_country"):
        c.add_country(p)
    context.pays = p

@given('un habitatDistrict "{habitat_type}" dans le pays "{nom_pays}"')
def step_create_habitat_district(context, habitat_type, nom_pays):
    
    assert hasattr(context, "pays"), "Pays n'est pas initialisé (vérifie l'ordre des Given)."
    assert context.pays.get_nom() == nom_pays
    context.habitat_district = HabitatDistrict(Habitat(habitat_type), context.pays)

@when("l'animal se déplace vers l'habitatDistrict")
def step_move_animal_to_habitat_district(context):
    context.move_ok = context.animal.move_to(context.habitat_district)

@then('le district de l\'habitatDistrict est "{nom_pays}"')
def step_check_district(context, nom_pays):
    assert context.habitat_district.get_district().get_nom() == nom_pays
