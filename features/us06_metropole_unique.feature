Feature: US_06 Unicité de la métropole Zootopia
En tant que Maire Lionheart
Je veux qu'il n'existe qu'un seul continent appelé "Zootopia"
Afin de garantir que personne ne crée de monde parallèle

Scenario: Tentative de création d'un second continent
    Given le continent "Zootopia" est déjà fondé
    When je tente de créer un autre continent "Atlantis"
    Then le système bloque la création
    And une erreur fatale est levée contenant "Zootopia est l'unique continent"