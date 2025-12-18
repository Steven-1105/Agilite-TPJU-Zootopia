from behave import given, when, then
from src.continent import Continent

@given('le continent "Zootopia" est déjà fondé')
def step_found_zootopia(context):
    # 1. On s'assure que la place est nette
    Continent.reset_instance()
    # 2. On fonde Zootopia
    context.zootopia = Continent("Zootopia")

@when('je tente de créer un autre continent "Atlantis"')
def step_try_create_atlantis(context):
    try:
        # 3. On essaie l'impossible
        context.atlantis = Continent("Atlantis")
        context.error = None # Oups, ça aurait dû planter
    except Exception as e:
        # 4. On capture l'erreur attendue
        context.error = e

@then('le système bloque la création')
def step_verify_block(context):
    assert context.error is not None, "Le système a failli : il a autorisé un deuxième continent !"


@then('une erreur fatale est levée contenant "{message}"')
def step_verify_fatal_message(context, message):
    print(f"DEBUG - Erreur reçue : {context.error}")
    assert message in str(context.error)