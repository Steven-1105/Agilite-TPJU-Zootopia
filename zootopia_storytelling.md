# Zootopia : Une Métropole où la Biologie rencontre la Géographie

![Diagramme Zootopia](/image/image1.jpeg)
*Une fusion architecturale de deux projets en une ville vivante et cohérente.*

---

## 1. Le Contexte : Une Ville à Construire
Notre mission consistait à fusionner deux univers distincts : le monde hiérarchique de la **Géographie** (Continents, Pays) et l'écosystème dynamique de la **Biologie** (Habitats, Animaux). Nous avons choisi l'univers de **Zootopia** comme cadre parfait, car il illustre une société complexe où chaque espèce doit trouver sa place dans un environnement adapté, sous une administration unifiée.

**Objectif :** Créer une méta-structure cohérente permettant aux citoyens-animaux d'évoluer dans des districts géographiques tout en respectant leurs besoins biologiques, avec une contrainte majeure : **modifier le code existant de manière minimale.**

---

## 2. Le Déclencheur : Le Problème des Deux Mondes
Notre principal défi technique était l'incompatibilité entre nos deux systèmes :
-   **Le système "Biologie" (`Habitat`)** parlait le langage des **biotopes** (Désert, Toundra, Forêt).
-   **Le système "Géographie" (`Pays`)** parlait le langage des **districts administratifs** (Sahara Square, Tundratown).

Ces deux mondes devaient communiquer sans que l'un ne modifie profondément le code interne de l'autre.

> *« Comment faire cohabiter le sauvage et l'urbain sans tout casser ? »*

---

## 3. Le Voyage : L'Architecture en Couches de Zootopia

![Diagramme Zootopia](/image/image4.png)
diagramme de classe illustrant les 2 design patterns
### **Niveau 1 : Le Cœur Unique - Le Singleton `Continent`**
Pour garantir l'unicité et la cohérence de la métropole, nous avons instauré **Zootopia comme un Singleton**. Peu importe qui ou quoi l'interroge, il n'existe qu'une seule et unique instance de la ville. C'est la pierre angulaire administrative, le "Continent" qui chapeaute tout.

* Zootopia est une. Son administration centrale est unique et incontestable, garantissant l'ordre à l'échelle de la métropole. 

### **Niveau 2 : Les Districts - La classe `Pays`**
La ville se divise en **districts climatiques emblématiques** (Tundratown, Sahara Square, Rainforest District...). Chacun est une instance de `Pays`. Dès sa création, un district s'enregistre **automatiquement** auprès de la mairie centrale (`Continent`), s'inscrivant dans la cartographie officielle de Zootopia.

### **Niveau 3 : Le Zonage Urbain - L'Adaptateur `HabitatDistrict` (La Clé de Voûte)**
C'est ici que la fusion devient élégante. Pour relier un `Habitat` biologique à un `Pays` géographique **sans modifier leurs codes d'origine**, nous avons créé un **Design Pattern Adaptateur** : `HabitatDistrict`.

*   **Rôle :** Cette classe agit comme un **"permis de zonage"**.
*   **Fonction :** Elle "enveloppe" un `Habitat` (ex: une Banquise) et lui **assigne officiellement un district** (ex: Tundratown). Elle traduit l'espace naturel en zone administrative reconnue.

*Dans la nature, un habitat est libre. À Zootopia, il doit être zoné. Notre adaptateur officialise le biotope, le rattachant juridiquement et logiquement à un district. *

### **Niveau 4 : Les Biotopes Concrets - La classe `Habitat`**
À l'intérieur des districts zonés se trouvent les **habitats réels**, gérés par la classe d'origine `Habitat`. Elle définit le type de milieu (froid, aride...) et garde la **liste des résidents actuels**.
![Diagramme Zootopia](/image/image3.jpg)

### **Niveau 5 : Les Citoyens - La classe `Animal`**
Au bout de la chaîne, les **citoyens** (Judy Hopps, Nick Wilde...). Ils possèdent une **énergie vitale** et des **besoins spécifiques**.
![Diagramme Zootopia](/image/image2.png)
---

## 4. Le Tournant : La Vie en Société Démystifiée
Grâce à cette architecture en couches, des mécanismes sociaux complexes deviennent simples :

*   **Déménagement (`move_to()`)** : Pour s'installer dans un nouvel habitat, un citoyen paie **10 points d'énergie**, symbolisant l'effort d'intégration et de transport.
*   **Survie :** Le système vérifie en permanence si l'énergie du citoyen **couvre les besoins journaliers** (`daily_energy_need`) de l'habitat de son district. Vivre dans la Toundra est plus coûteux en énergie que dans la Forêt Tempérée.
*   **Traçabilité :** On peut désormais remonter toute la chaîne d'appartenance :  
    `Animal` → `HabitatDistrict` (adaptateur) → `Pays` (District) → `Continent` (Zootopia).

---

## 5. La Résolution : Une Ville Cohérente et Vivante
**Résultat tangible :** Nous avons créé un écosystème logiciel où la géographie structure l'espace et la biologie gère la vie. Zootopia est une entité **unifiée, organisée et dynamique**.

**Transformation technique :** L'utilisation du **pattern Adaptateur** a été la révélation. Il a permis une **fusion propre, évolutive et respectueuse du code existant**, évitant un réécriture massive et des couplages indésirables.

[voir les user_stories](USER_STORIES.md)
---

## 6. Conclusion : La Leçon de Zootopia
Ce projet démontre que des systèmes complexes et initialement indépendants peuvent **co-évoluer harmonieusement** grâce à une **architecture pensée et des patterns design appropriés**. Comme dans la ville de Zootopia, où prédateurs et proies apprennent à vivre ensemble, nos composants "Géographie" et "Biologie" ont trouvé un langage commun grâce à un adaptateur bien conçu.

> * En code comme en société, l'intégration ne signifie pas l'assimilation, mais la création d'interfaces intelligentes qui préservent l'identité de chacun. *

**En résumé : Zootopia est plus qu'une ville ; c'est une simulation architecturale où chaque couche de code a sa place et son rôle, contribuant à faire vivre une société virtuelle cohérente.**
