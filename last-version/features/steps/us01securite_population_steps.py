from behave import given, when, then
from src.pays import Pays
from src.continent import Continent

# --- PARTIE 1 : ZOMBIES ---

@given('que je veux créer un nouveau pays')
def step_impl(context):
    # On ne fait rien de spécial ici, on se prépare juste
    pass

@when('Kevin saisit une population de {population:d}')
def step_impl(context, population):
    try:
        # On tente de créer le pays. Si ça échoue, on capture l'erreur.
        context.nouveau_pays = Pays("Testland", population)
        context.error = None # Pas d'erreur
    except ValueError as e:
        context.error = e # On stocke l'erreur pour la vérifier au step suivant

@then('le système refuse la création')
def step_impl(context):
    # Si context.error existe, c'est que la création a été refusée (Succès du test)
    assert context.error is not None, "Le système aurait dû refuser, mais il a accepté !"

@then('il lève une erreur contenant "{message}"')
def step_impl(context, message):
    # On vérifie que le message d'erreur est bien celui attendu
    assert message in str(context.error), f"Message attendu: {message}, Reçu: {context.error}"


# --- PARTIE 2 : CLONES ---

@given('le continent "{nom_cont}" contient déjà le pays "{nom_pays}"')
def step_impl(context, nom_cont, nom_pays):
    context.continent = Continent(nom_cont)
    p1 = Pays(nom_pays, 1000)
    context.continent.ajouter_pays(p1)

@when('Kevin tente d\'ajouter une nouvelle "{nom_pays}" dans "{nom_cont}"')
def step_impl(context, nom_pays, nom_cont):
    try:
        # Kevin essaie de créer un deuxième objet avec le même nom
        p2_clone = Pays(nom_pays, 2000)
        context.continent.ajouter_pays(p2_clone)
        context.error = None
    except ValueError as e:
        context.error = e

@then('le système refuse l\'ajout du doublon')
def step_impl(context):
    assert context.error is not None, "Le système a accepté le doublon !"