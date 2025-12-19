# User Stories – Projet Zootopia
## Agilité, BDD et Fusion de Domaines

Ce document décrit l’ensemble des user stories du projet Zootopia.
Chaque user story est associée à des critères d’acceptance validés
par des tests automatisés :
- Tests BDD avec **Behave**
- Tests unitaires avec **Pytest**

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
