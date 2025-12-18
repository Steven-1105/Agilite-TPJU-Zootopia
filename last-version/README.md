# TP3 — Scénario agile intégré (Animal / Habitat)

Ce dépôt illustre un **scénario agile intégré** conforme au TP3 du cours *Management de Projet et Agilité*.

L’objectif est de montrer comment des **User Stories** peuvent devenir des **spécifications exécutables**, grâce à une combinaison de **BDD (Cucumber/Behave)**, de **tests automatisés** et d’un **code évolutif**.

---

## 1) Objectifs pédagogiques

- Exprimer les exigences sous forme de **User Stories**.
- Traduire les critères d’acceptation en **scénarios exécutables (Given / When / Then)**.
- Garantir la **stabilité du système** via des tests automatisés.
- Illustrer un **cycle de vie agile complet** : besoin → test → code → exécution → évolution.

---

## 2) Technologies utilisées

- **Langage** : Python 3
- **BDD / Cucumber** : `behave` (syntaxe Gherkin)
- **Tests automatisés** : pytest (tests unitaires)
- **IDE** : VSCode
- **Versionnement** : Git

---

## 3) Structure du projet

```text
.
├── src/
│   ├── animal.py          # Modèle métier Animal
│   └── habitat.py         # Modèle métier Habitat
│
├── tests/                 # Tests unitaires (pytest)
│   ├── test_us01_basic_animal.py
│   ├── test_us02_habitat_daily_needs.py
│   └── test_us03_survival_and_move.py
│
├── features/              # Tests BDD (Cucumber / Behave)
│   ├── animal_habitat.feature
│   └── steps/
│       └── animal_steps.py
│
├── USER_STORIES.md        # User Stories et critères d’acceptation
└── README.md
```

---

## 4) Installation

### Création d’un environnement virtuel

```bash
python -m venv .venv
```

Activation :

- macOS / Linux
```bash
source .venv/bin/activate
```

- Windows (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### Installation des dépendances

```bash
pip install -U pip
pip install pytest behave
```

---

## 5) Exécution des tests

### Tests unitaires (pytest)

```bash
pytest -q
```

### Tests BDD / Cucumber (behave)

```bash
behave
```

Chaque **Scenario** correspond à une User Story ou à un critère d’acceptation.

---

## 6) Traçabilité agile (User Stories → Tests → Code)

- Les **User Stories** sont décrites dans `USER_STORIES.md`.
- Chaque critère d’acceptation est couvert :
  - soit par un test **pytest** (niveau unitaire),
  - soit par un scénario **Cucumber / Behave** (niveau comportemental).

Ainsi, les scénarios `.feature` jouent le rôle de **spécifications exécutables**, lisibles aussi bien par les développeurs que par des acteurs non techniques.

---

## 7) Cycle agile illustré

1. Rédaction des User Stories
2. Définition des scénarios BDD (Given / When / Then)
3. Implémentation du code métier
4. Exécution automatique des tests
5. Validation (barre verte)
6. Évolution ou correction sans régression

---

## 8) Archivage et reproductibilité

Le projet est conçu pour être :

- versionné avec Git,
- exécutable sur toute machine disposant de Python,
- reproductible grâce aux tests automatisés.

Chaque évolution fonctionnelle peut être associée à un commit et, si nécessaire, à un tag de version.

---

## 9) Conclusion

Ce TP met en œuvre les principes clés de l’agilité : **feedback rapide**, **qualité intégrée**, **tests automatisés** et **évolution contrôlée du code**, en s’appuyant sur des User Stories devenues directement exécutables.
