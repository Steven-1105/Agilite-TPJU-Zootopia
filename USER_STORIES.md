# User Stories – Projet Zootopia (Agilité & BDD)

Ce document décrit les besoins fonctionnels du projet Zootopia sous forme de
user stories, ainsi que leurs critères d’acceptance.
Chaque user story est validée par des tests automatisés (BDD avec Behave et
tests unitaires avec Pytest).

---

## US01 – État et évolution d’un animal

En tant que Gardien de l’écosystème  
Je veux créer un animal et suivre l’évolution de son âge et de son énergie  
Afin de m’assurer de sa survie dans le temps.

### Critères d’acceptance
- AC1 : Un animal est créé avec un âge initial égal à 0.
- AC2 : L’âge de l’animal augmente lorsqu’il vieillit.
- AC3 : L’énergie de l’animal diminue lorsqu’il vieillit.
- AC4 : L’état de l’animal est vérifiable via des scénarios BDD.

---

## US02 – Besoins énergétiques journaliers selon l’habitat

En tant que Gardien de l’écosystème  
Je veux calculer les besoins énergétiques journaliers d’un animal selon son habitat  
Afin d’adapter la gestion de son énergie.

### Critères d’acceptance
- AC1 : Chaque type d’habitat possède un besoin énergétique spécifique.
- AC2 : Le calcul des besoins journaliers est automatique.
- AC3 : Si l’énergie est insuffisante, l’animal ne peut pas survivre.
- AC4 : Les règles sont validées par des scénarios BDD.

---

## US03 – Sécurisation et calcul des données de population

En tant que Responsable de la base de données  
Je veux garantir la cohérence des données de population des pays et des continents  
Afin d’éviter les incohérences et les erreurs de calcul.

### Critères d’acceptance
- AC1 : La création d’un pays avec une population négative est refusée.
- AC2 : Les doublons de pays dans un continent sont interdits.
- AC3 : La population totale d’un continent est calculée automatiquement.
- AC4 : Les résultats sont vérifiés par des tests unitaires et BDD.

---

## US04 – Filtrage des pays vulnérables

En tant que Logisticien d’Urgence  
Je veux lister les pays dont la population est inférieure à un seuil donné dans un continent  
Afin d’envoyer une aide ciblée aux zones les plus vulnérables.

### Critères d’acceptance
- AC1 : Le système permet de filtrer les pays d’un continent selon un seuil de population.
- AC2 : Seuls les pays dont la population est inférieure au seuil sont retournés.
- AC3 : Les pays dépassant le seuil sont exclus du résultat.
- AC4 : Le filtrage est validé par des scénarios BDD.

---

## US05 – Fusion des mondes biologique et géographique

En tant que Responsable de l’écosystème  
Je veux relier les habitats des animaux à des pays et des continents  
Afin de contextualiser la gestion biologique dans un cadre géographique cohérent.

### Critères d’acceptance
- AC1 : Un habitat peut être associé à un pays via un adaptateur (HabitatDistrict).
- AC2 : Un animal peut vivre et se déplacer dans un HabitatDistrict comme dans un habitat classique.
- AC3 : À partir d’un HabitatDistrict, il est possible d’identifier le pays associé.
- AC4 : La fusion n’altère pas les comportements existants (non-régression).
- AC5 : La fusion est validée par des tests unitaires et des scénarios BDD.

---

## US06 – Création de la Métropole Unique (Singleton)

En tant que Maire Lionheart  
Je veux garantir l’unicité de la ville (continent) dans le système  
Afin d’éviter les incohérences et le chaos administratif.

### Critères d’acceptance
- AC1 : Il n’existe qu’une seule instance de continent dans le système à un instant donné.
- AC2 : Toute tentative de création d’un nouveau continent retourne la même instance existante.
- AC3 : Le nom du continent reste celui de la première instance créée.
- AC4 : Les données internes du continent (ex. liste des districts/pays) sont partagées entre toutes les références.
- AC5 : L’unicité est vérifiable via des scénarios BDD et des tests unitaires.


## Validation

- Les **tests unitaires** sont réalisés avec **Pytest** afin de valider la logique interne.
- Les **tests fonctionnels (BDD)** sont réalisés avec **Behave** afin de valider les user stories
  et leurs critères d’acceptance.
- L’ensemble des tests est vert après la fusion des deux projets.
