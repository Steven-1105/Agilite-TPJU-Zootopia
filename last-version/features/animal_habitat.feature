Feature: US_001 Animal et Habitat

 En tant que Gardien de l'Équilibre
 Je veux veiller sur chaque créature et chaque terre de mon royaume,
 Afin que l'harmonie règne entre le code et la nature

  # --------------------------------------------------
  # US01 — Gérer un animal (état et actions de base)
  # --------------------------------------------------

  Scenario Outline: création et évolution de l’état d’un animal
    Given un animal "<nom>" avec <energie> d'énergie
    When l'animal vieillit
    Then l'âge de l'animal est <age>
    And l'énergie de l'animal est <energie_finale>

    Examples:
      | nom   | energie | age | energie_finale |
      | Lion  | 100     | 1   | 95             |
      | Panda | 20      | 1   | 15             |

  # --------------------------------------------------
  # US02 — Adapter les besoins énergétiques selon l’habitat
  # --------------------------------------------------

  Scenario Outline: calcul des besoins énergétiques journaliers
    Given un animal "<nom>" avec <energie> d'énergie
    And l'animal vit dans "<habitat>"
    When l'animal calcule ses besoins journaliers
    Then le besoin journalier est <besoin>

    Examples:
      | nom   | energie | habitat | besoin |
      | Lion  | 100     | Savanna | 30     |
      | Panda | 80      | Forest  | 25     |
      | Camel | 120     | Desert  | 40     |

  # --------------------------------------------------
  # US03 — Déplacement et survie
  # --------------------------------------------------

  Scenario: déplacement possible si énergie suffisante
    Given un animal "Elephant" avec 100 d'énergie
    And un habitat "Forest"
    When l'animal se déplace vers son habitat
    Then l'animal vit dans "Forest"
    And l'énergie de l'animal est 90

  Scenario: survie impossible si énergie insuffisante
    Given un animal "WeakLion" avec 10 d'énergie
    And l'animal vit dans "Savanna"
    When l'animal calcule ses besoins journaliers
    Then l'animal ne peut pas survivre
