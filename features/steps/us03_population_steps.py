from behave import given, when, then
from src.continent import Continent
from src.pays import Pays

# On stocke les continents dans un dictionnaire pour les retrouver par leur nom
# ex: {'Europe': objet_continent_europe, 'Asie': objet_continent_asie}
world_map = {}

@given('le continent "{nom_continent}" est créé')
def step_create_continent(context, nom_continent):
    world_map[nom_continent] = Continent(nom_continent)

@given('j\'ajoute le pays "{nom_pays}" avec {pop:d} habitants dans "{nom_continent}"')
def step_add_country(context, nom_pays, pop, nom_continent):
    # 1. On retrouve le continent
    continent_cible = world_map[nom_continent]
    # 2. On crée le pays
    nouveau_pays = Pays(nom_pays, pop)
    # 3. On l'ajoute
    continent_cible.ajouter_pays(nouveau_pays)

@when('je demande la population totale de "{nom_continent}"')
def step_ask_total(context, nom_continent):
    continent_cible = world_map[nom_continent]
    # On stocke le résultat pour le vérifier à l'étape suivante
    context.total_calcule = continent_cible.population_totale()

@then('la population totale doit être {resultat_attendu:d}')
def step_verify_total(context, resultat_attendu):
    assert context.total_calcule == resultat_attendu, \
        f"Erreur de calcul ! Attendu: {resultat_attendu}, Reçu: {context.total_calcule}"