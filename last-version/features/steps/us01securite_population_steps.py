from behave import given, when, then
from src.pays import Pays
from src.continent import Continent

# --- PARTIE 1 : ZOMBIES ---

@given('que je veux créer un nouveau pays')
def step_impl(context):
    # Contexte initial vide ou préparation si besoin
    pass

# Le feature dit : "Kevin saisit un pays de -500"
@when('Kevin saisit un pays de {population:d}')
def step_impl(context, population):
    try:
        # On tente de créer le pays. 
        # Si la population est négative, le constructeur de Pays doit lever ValueError
        context.nouveau_pays = Pays("Testland", population)
        context.error = None 
    except ValueError as e:
        context.error = e # On capture l'erreur pour la vérifier à l'étape suivante

@then('le système refuse la création')
def step_impl(context):
    # Le test réussit si une erreur a bien été stockée
    assert context.error is not None, "ERREUR : Le système a accepté une population négative !"

@then('il lève une erreur contenant "{message}"')
def step_impl(context, message):
    # On vérifie que le message d'erreur de la classe Pays correspond à celui du Feature
    assert message in str(context.error), f"Message attendu: '{message}', Reçu: '{context.error}'"


# --- PARTIE 2 : CLONES ---

@given('le continent "{nom_cont}" contient déjà le pays "{nom_pays}"')
def step_impl(context, nom_cont, nom_pays):
    context.continent = Continent(nom_cont)
    # Création du premier pays valide
    p1 = Pays(nom_pays, 1000)
    context.continent.ajouter_pays(p1)

@when('Kevin tente d\'ajouter une nouvelle "{nom_pays}" dans "{nom_cont}"')
def step_impl(context, nom_pays, nom_cont):
    try:
        # Kevin tente de créer un objet DIFFERENT (p2) mais avec le MÊME NOM
        p2_clone = Pays(nom_pays, 2000)
        context.continent.ajouter_pays(p2_clone)
        context.error = None
    except ValueError as e:
        context.error = e

@then('le système refuse l\'ajout du doublon')
def step_impl(context):
    assert context.error is not None, "ERREUR : Le système a accepté le doublon !"