# User Stories – Projet Zootopia
## Agilité, BDD et Fusion de Domaines

Ce document décrit l’ensemble des user stories du projet Zootopia.
Chaque user story est associée à des critères d’acceptance validés
par des tests automatisés :
- Tests BDD avec **Behave**
- Tests unitaires avec **Pytest**

---

## US_001 – Animal et Habitat

En tant que Gardien de l’Équilibre  
Je veux créer des animaux, suivre leur évolution et leur interaction avec un habitat  
Afin d’assurer la survie et l’harmonie de l’écosystème.

### Critères d’acceptance
- AC1 : Un animal est créé avec un âge initial égal à 0.
- AC2 : L’âge de l’animal augmente lorsqu’il vieillit.
- AC3 : L’énergie de l’animal diminue avec le temps.
- AC4 : Les besoins énergétiques journaliers dépendent de l’habitat.
- AC5 : Un animal peut se déplacer dans un habitat si son énergie est suffisante.
- AC6 : Un animal ne peut pas survivre si son énergie est insuffisante.

---

## US_01 – Sécurisation et intégrité des données de population

En tant que Responsable de la Base de Données  
Je veux que le système bloque les populations négatives et les doublons  
Afin de garantir la cohérence et la fiabilité des données.

### Critères d’acceptance
- AC1 : La création d’un pays avec une population négative est refusée.
- AC2 : Une erreur explicite est levée en cas de population invalide.
- AC3 : Un pays ne peut pas être ajouté deux fois dans un même continent.
- AC4 : L’intégrité des données est vérifiée automatiquement par des tests.

---

## US_02 – Calcul automatique de la densité

En tant qu’Analyste (Michel)  
Je veux que le système calcule automatiquement la densité de population d’un pays  
Afin d’éviter les calculs manuels et les erreurs humaines.

### Critères d’acceptance
- AC1 : La densité est calculée à partir de la population et de la superficie.
- AC2 : Le calcul est automatique et fiable.
- AC3 : Le résultat retourné correspond à la valeur attendue.
- AC4 : Le calcul est validé par des scénarios BDD.

---

## US_03 – Calcul de la population totale d’un continent

En tant qu’Analyste Flémard (Michel)  
Je veux connaître la population totale d’un continent  
Afin de ne pas additionner les populations des pays à la main.

### Critères d’acceptance
- AC1 : Un continent peut contenir plusieurs pays.
- AC2 : La population totale du continent correspond à la somme des populations des pays.
- AC3 : Le calcul est automatique.
- AC4 : Le résultat est validé par des tests BDD.

---

## US_04 – Filtrage des pays vulnérables

En tant que Logisticien d’Urgence  
Je veux lister les pays dont la population est inférieure à un seuil donné  
Afin d’envoyer une aide ciblée aux pays les plus vulnérables.

### Critères d’acceptance
- AC1 : Le système permet de définir un seuil de population.
- AC2 : Seuls les pays dont la population est inférieure au seuil sont retournés.
- AC3 : Les pays dépassant le seuil sont exclus du résultat.
- AC4 : Le filtrage est validé par des scénarios BDD.

---

## US_05 – Fusion des domaines biologique et géographique

En tant que Responsable de l’écosystème  
Je veux relier les habitats des animaux à un pays  
Afin de contextualiser la gestion biologique dans un cadre géographique cohérent.

### Critères d’acceptance
- AC1 : Un habitat peut être associé à un pays via un adaptateur.
- AC2 : Un animal peut vivre et se déplacer dans un HabitatDistrict.
- AC3 : Le pays associé à un HabitatDistrict est identifiable.
- AC4 : Les fonctionnalités existantes ne sont pas modifiées (non-régression).
- AC5 : La fusion est validée par des tests BDD et unitaires.

---

## US_06 – Création de la Métropole Unique (Singleton)

En tant que Maire Lionheart  
Je veux garantir l’unicité de la ville (continent)  
Afin d’éviter le chaos administratif et les incohérences de données.

### Critères d’acceptance
- AC1 : Il n’existe qu’une seule instance de continent en mémoire.
- AC2 : Toute tentative de création d’un nouveau continent retourne la même instance.
- AC3 : Le nom du continent reste celui de la première instance créée.
- AC4 : Les données internes (ex. districts/pays) sont partagées entre les références.
- AC5 : L’unicité est vérifiée par des scénarios BDD et des tests unitaires.

---

## Validation globale

- **7 features**, **14 scénarios** et **60 steps** validés avec Behave.
- Les tests unitaires Pytest confirment la robustesse de la logique interne.
- Le projet respecte les principes de l’agilité, de la testabilité et de la non-régression.
