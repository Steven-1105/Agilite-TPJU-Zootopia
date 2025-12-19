# Projet Zootopia – Agilité & BDD

## Contexte
Le projet Zootopia vise à modéliser un écosystème mêlant un domaine biologique (Animal / Habitat) et un domaine géographique (Pays / Continent), en respectant les principes de l’agilité, de la non-régression et des tests automatisés.

![Diagramme Zootopia](/image/image1.jpeg)

---

## Objectifs
- Implémenter des user stories claires et testables
- Valider les comportements métier via des tests BDD (Behave)
- Garantir la robustesse du code via des tests unitaires (Pytest)
- Fusionner deux domaines indépendants sans régression

---

## User Stories (vue d’ensemble)
- **US_001** – Animal et Habitat
- **US_01** – Sécurisation et intégrité des données
- **US_02** – Calcul automatique de la densité
- **US_03** – Population continentale
- **US_04** – Filtrage des pays vulnérables
- **US_05** – Fusion Bio + Géo (Adapter)
- **US_06** – Métropole unique (Singleton)

(Le détail des user stories et des critères d’acceptance est disponible dans [User Stories](USER_STORIES.md).)

---

## Choix architecturaux
- **Adapter (`HabitatDistrict`)** : permet de relier un habitat à un pays sans
  modifier les classes existantes.
- **Singleton (`Continent`)** : garantit l’unicité des continents et la cohérence
  des données partagées.

---

## Tests et validation
Le projet est validé par :
- **Tests fonctionnels BDD (Behave)** : validation des user stories
- **Tests unitaires (Pytest)** : validation de la logique interne

### Résultats
- 7 features validées
- 14 scénarios exécutés
- 60 steps exécutés
- Aucun échec

