from src.animal import Animal
from src.pays import Pays
from src.continent import Continent
from src.habitat_district import HabitatDistrict
from src.habitat import Habitat

def test_us05_animal_can_move_to_habitat_district_and_link_to_country():
    try:
        europe = Continent("Europe", reset=True)
    except TypeError:
        europe = Continent("Europe")

    france = Pays("France", 67000000)
    if hasattr(europe, "ajouter_pays"):
        europe.ajouter_pays(france)
    elif hasattr(europe, "add_country"):
        europe.add_country(france)

    hd = HabitatDistrict(Habitat("Forest"), france)
    wolf = Animal("Wolf", 100)

    ok = wolf.move_to(hd)
    assert ok is True
    assert wolf.habitat.get_type() == "Forest"
    assert hd.get_district().get_nom() == "France"
