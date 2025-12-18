# USER STORIES — TP3 (Animal / Habitat)

Ce document décrit les **User Stories** du TP3 ainsi que leurs **critères d’acceptation**.
Chaque critère est implémenté et vérifié par des **tests automatisés** (pytest) et/ou des **scénarios BDD exécutables** (Cucumber / Behave).

---

## US01 — Gérer un animal (état et actions de base)

**En tant que** système  
**Je veux** créer et manipuler un animal avec un état cohérent  
**Afin de** pouvoir simuler son comportement de manière fiable

### Critères d’acceptation

- Un animal possède un nom, une énergie et un âge initial égal à 0
- Un animal nouvellement créé n’a pas d’habitat
- L’action `eat(x)` augmente l’énergie si `x > 0`
- L’action `eat(x)` est refusée si `x < 0`
- L’action `growOld()` augmente l’âge de 1
- L’énergie ne peut jamais devenir négative

### Vérification

- Tests unitaires : `test_us01_basic_animal.py`
- Assertions automatiques via pytest

---

## US02 — Adapter les besoins énergétiques selon l’habitat

**En tant que** animal  
**Je veux** calculer mes besoins énergétiques journaliers en fonction de mon habitat  
**Afin de** déterminer si je peux survivre dans mon environnement

### Critères d’acceptation

- Sans habitat, le besoin énergétique journalier est de 20
- Dans un habitat de type `Savanna`, le besoin est de 30
- Dans un habitat de type `Forest`, le besoin est de 25
- Dans un habitat de type `Desert`, le besoin est de 40

### Vérification

- Scénarios BDD : `features/animal_habitat.feature`
- Tests unitaires : `test_us02_habitat_daily_needs.py`

---

## US03 — Déplacement et survie de l’animal

**En tant que** système  
**Je veux** gérer le déplacement d’un animal et vérifier sa capacité de survie  
**Afin de** garantir la cohérence des règles métier

### Critères d’acceptation

- Un animal peut se déplacer vers un habitat si son énergie est suffisante
- Le déplacement vers un habitat coûte 10 points d’énergie
- Si l’énergie est insuffisante, le déplacement est refusé
- Un animal survit si son énergie est supérieure ou égale à ses besoins journaliers

### Vérification

- Scénarios BDD : `features/animal_habitat.feature`
- Tests unitaires : `test_us03_survival_and_move.py`

---

## Remarque pédagogique

Ces User Stories sont volontairement **simples et indépendantes** afin d’illustrer :

- une approche agile itérative,
- la transformation des exigences en **spécifications exécutables**,
- la stabilité du code face aux évolutions futures grâce aux tests automatisés.
