from behave import given, when, then
from src.continent import Continent
from src.pays import Pays

# Dictionnaire pour stocker nos continents (comme pour l'US-03)
world_map = {}

@given('le continent "{nom_cont}" existe avec les pays suivants:')
def step_create_continent_with_table(context, nom_cont):
    # On force un continent "propre" pour ce scénario
    c = Continent(nom_cont)
    # On lit le tableau ligne par ligne
    for row in context.table:
        nom_pays = row['nom']
        pop = int(row['population'])
        # On utilise ta classe Pays existante    
        p = Pays(nom_pays, pop)
        c.ajouter_pays(p)
    
    # On sauvegarde le continent
    world_map[nom_cont] = c

@when('je cherche les pays de moins de {seuil:d} habitants en "{nom_cont}"')
def step_filter_countries(context, seuil, nom_cont):
    continent = world_map[nom_cont]
    # On appelle la méthode de filtrage et on stocke le résultat
    context.resultat_filtre = continent.get_pays_population_max(seuil)

@then('je récupère une liste contenant "{pays1}" et "{pays2}"')
def step_verify_content(context, pays1, pays2):
    # On extrait juste les noms des objets pays récupérés pour comparer
    noms_recuperes = [p.get_nom() for p in context.resultat_filtre]
    
    assert pays1 in noms_recuperes, f"{pays1} est absent de la liste !"
    assert pays2 in noms_recuperes, f"{pays2} est absent de la liste !"

@then('la liste ne contient pas "{pays_exclu}"')
def step_verify_exclusion(context, pays_exclu):
    noms_recuperes = [p.get_nom() for p in context.resultat_filtre]
    
    assert pays_exclu not in noms_recuperes, f"{pays_exclu} ne devrait pas être là (trop grand) !"