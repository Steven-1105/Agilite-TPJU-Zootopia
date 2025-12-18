Feature: US_03 Calcul de population continentale
En tant qu'Analyste Flémard (Michel)
Je veux connaître la population totale d'un continent
Afin de ne pas additionner les pays à la main (et risquer une erreur)

Scenario: Somme des populations de l'Europe
    Given le continent "Europe" est créé
    And j'ajoute le pays "France" avec 67000000 habitants dans "Europe"
    And j'ajoute le pays "Allemagne" avec 83000000 habitants dans "Europe"
    When je demande la population totale de "Europe"
    Then la population totale doit être 150000000