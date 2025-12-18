# language: en
@Automatisation
Feature: US_02 Calcul automatique de la densité
En tant que "Michel" (Analyste qui déteste les tâches répétitives)
Je veux que le système calcule la densité automatiquement
Afin de ne jamais avoir à vérifier manuellement une division

Scenario Outline: Vérification automatique du calcul
    Given le pays "<pays>" avec <population> habitants et <superficie> km2
    When je demande la densité au système
    Then le résultat retourné doit être <resultat>

    Examples:
    | pays    | population | superficie | resultat |
    | Monaco  | 39000      | 2          | 19500    |
    | Russie  | 144000000  | 17000000   | 8.47     |
    