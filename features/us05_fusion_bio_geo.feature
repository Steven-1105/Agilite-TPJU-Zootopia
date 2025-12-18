Feature: US_05 Fusion Bio + Géo
  En tant que Responsable de l’écosystème
  Je veux relier les habitats à un pays
  Afin de contextualiser la gestion des animaux dans un cadre géographique

  Scenario: Un animal peut vivre dans un HabitatDistrict lié à un pays
    Given le continent "Europe" est créé
    And le pays "France" avec 67000000 habitants dans "Europe"
    And un habitatDistrict "Forest" dans le pays "France"
    And un animal "Wolf" avec 100 d'énergie
    When l'animal se déplace vers l'habitatDistrict
    Then l'animal vit dans "Forest"
    And le district de l'habitatDistrict est "France"
