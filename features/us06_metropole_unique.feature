Feature: US_06 Création de la Métropole Unique (Singleton)
En tant que Maire Lionheart
Je veux garantir l'unicité de la ville
Afin d'éviter le chaos administratif

Scenario: Tentative de création multiple
    Given le continent "Zootopia" est initialisé
    When je tente de créer un autre continent appelé "Atlantis"
    Then les deux références pointent vers le MÊME objet mémoire
    And le nom du deuxième continent est en réalité "Zootopia"
    And la liste des districts est partagée entre les deux