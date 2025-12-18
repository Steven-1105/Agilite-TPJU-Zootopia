Feature: US_04 Filtrage des pays vulnérables
En tant que Logisticien d'Urgence
Je veux lister les petits pays d'un continent
Afin d'envoyer une aide ciblée

Scenario: Recherche des micro-états en Europe
    Given le continent "Europe" existe avec les pays suivants:
    | nom     | population |
    | France  | 67000000   |
    | Monaco  | 30000      |
    | Andorre | 70000      |
    When je cherche les pays de moins de 1000000 habitants en "Europe"
    Then je récupère une liste contenant "Monaco" et "Andorre"
    But la liste ne contient pas "France"