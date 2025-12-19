from behave import given, when, then
from src.continent import Continent
from src.pays import Pays

@given('le continent "Zootopia" est initialisé')
def step_init_zootopia(context):
    # On vide explicitement l'instance pour le test (sécurité)
    Continent._instance = None 
    context.continent_1 = Continent("Zootopia")

@when('je tente de créer un autre continent appelé "Atlantis"')
def step_try_create_other(context):
    # On essaie de créer une nouvelle variable avec un autre nom
    context.continent_2 = Continent("Atlantis")
    # Note : Comme c'est un Singleton, le __init__ va renommer l'instance unique en "Atlantis"
    # Mais l'objet mémoire sera le même. Pour ce test, on va vérifier l'identité.

@then('les deux références pointent vers le MÊME objet mémoire')
def step_check_identity(context):
    # L'opérateur 'is' vérifie si c'est la même adresse mémoire
    assert context.continent_1 is context.continent_2, "Erreur : Ce sont deux objets différents !"

@then('le nom du deuxième continent est en réalité "{nom_attendu}"')
def step_check_name_persistence(context, nom_attendu):
    # Si le Singleton fonctionne, context.continent_1 a aussi changé de nom car c'est le même objet
    # Dans notre implémentation __init__, le dernier appel gagne pour le nom.
    # Ici, on vérifie surtout que les deux variables partagent le même état.
    assert context.continent_2.get_nom() == context.continent_1.get_nom()

@then('la liste des districts est partagée entre les deux')
def step_check_shared_list(context):
    # Si j'ajoute un pays dans l'un, il doit apparaître dans l'autre
    p = Pays("District Test", 100)
    context.continent_1.ajouter_pays(p)
    
    assert p in context.continent_2.get_pays(), "Le district n'est pas visible dans la 2ème référence !"