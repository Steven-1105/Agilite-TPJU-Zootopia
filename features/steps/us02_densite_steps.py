from behave import given, when, then
from src.pays import Pays

@given('le pays "{nom}" avec {population:d} habitants et {superficie:d} km2')
def step_create_pays_superficie(context, nom, population, superficie):
    # On crée le pays avec les 3 paramètres
    context.pays = Pays(nom, population, superficie)

@when('je demande la densité au système')
def step_calculate_density(context):
    # On appelle la méthode de calcul et on stocke le résultat
    context.resultat_densite = context.pays.calculer_densite()

@then('le résultat retourné doit être {resultat}')
def step_check_result(context, resultat):
    # On convertit nous-mêmes en float ici :
    valeur_attendue = float(resultat)
    
    assert context.resultat_densite == valeur_attendue, f"Attendu {valeur_attendue}, obtenu {context.resultat_densite}"