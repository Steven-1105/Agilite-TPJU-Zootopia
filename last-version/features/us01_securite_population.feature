Feature: US_01 Sécurisation et intégrité des données

En tant que Responsable de la Base de Données
Je veux que le système bloque les populations négatives ET les doublons
Afin de garantir une base saine (pas de zombies, pas de clones)

# Scénario 1 : Le Syndrome du Zombie
Scenario Outline: Rejet des populations négatives
    Given que je veux créer un nouveau pays
    When Kevin saisit un pays de <population nétigatives>
    Then le système refuse la création
    And il lève une erreur contenant "<message>"

    Examples:
    | population | message                                             |
    | -500       | Erreur : La population ne peut pas être négative !  |

# Scénario 2 : Le Syndrome du Clone
Scenario Outline: Rejet des doublons de pays dans un continent
    Given le continent "Europe" contient déjà le pays "France"
    When Kevin tente d'ajouter une nouvelle "France" dans "Europe"
    Then le système refuse l'ajout du doublon
    And il lève une erreur contenant "Doublon détecté"