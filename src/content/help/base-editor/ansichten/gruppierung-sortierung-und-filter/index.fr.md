---
title: 'Regroupement, tri et filtre'
date: 2022-08-25
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'cdb'
url: '/fr/aide/grouper-trier-filtrer'
aliases:
    - '/fr/aide/gruppierung-sortierung-und-filter'
seo:
    title: 'Grouper, trier et filtrer vos données dans SeaTable'
    description: 'Apprenez à grouper, trier et filtrer vos données avec SeaTable. Organisez vos tableaux et trouvez les informations utiles rapidement et facilement.'
weight: 20
---

SeaTable propose diverses méthodes d'analyse et de préparation des données. **Les filtres, tris et regroupements** sont des outils simples qui vous permettent de structurer vos données en quelques clics et d'obtenir rapidement les informations souhaitées. Utilisés correctement, les filtres, tris et regroupements offrent de nombreuses possibilités d'analyse.

Le filtrage, le tri et le regroupement d'enregistrements s'effectuent à l'aide de **règles**. Une règle se compose toujours d'une instruction et de la colonne à laquelle elle s'applique. Pour les tris et les regroupements, l'instruction, indépendamment du type de colonne, est l'ordre (croissant ou décroissant) dans lequel les enregistrements sont listés. Une instruction de filtrage a d'autres composants qui dépendent du type de colonne.

Cela semble compliqué ? Pas du tout – dans SeaTable, regrouper, trier et filtrer est un jeu d'enfant !

## Regrouper

La fonction de regroupement vous permet de **regrouper les lignes d'un tableau** et d'obtenir des statistiques descriptives simples telles que le nombre de lignes dans un groupe ou la somme et la moyenne de colonnes basées sur des nombres. Le regroupement s'effectue par **valeurs identiques dans la colonne sélectionnée pour le regroupement**. Par exemple, organisez les tâches de votre équipe en regroupant les tâches en attente pour chaque membre de l'équipe à l'aide d'un regroupement sur la colonne des employés.

Si vous souhaitez présenter vos données de manière encore plus précise, utilisez les **regroupements imbriqués**. Vous pouvez sélectionner jusqu'à trois caractéristiques de regroupement pour effectuer des regroupements subordonnés. Par exemple, vous pouvez regrouper les tâches d'abord par responsable, puis par priorité, puis par date. Cela vous ouvre de nouvelles possibilités de structuration des données.

[En savoir plus sur la fonction de regroupement]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})

## Trier

La fonction de tri vous permet d'afficher les entrées non classées d'un tableau **dans un ordre ordonné**.

Créez une règle pour trier les enregistrements par ordre croissant ou décroissant en fonction des valeurs d'une colonne. Si les enregistrements sont volumineux, vous pouvez utiliser **plusieurs règles de tri**. Dans le cas de plusieurs règles de tri, les lignes sont d'abord triées selon la première règle. Les lignes ayant des valeurs identiques selon la première règle de tri sont ensuite triées selon la deuxième règle.

[En savoir plus sur la fonction de tri]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})

## Filtrer

La fonction de filtrage de SeaTable vous permet d'utiliser des règles de filtrage pour **filtrer certains enregistrements d'une table** et n'afficher que les lignes qui répondent à un ou plusieurs critères souhaités. Vous réduisez ainsi le nombre de lignes dans la vue au minimum nécessaire et vous gardez toujours une vue d'ensemble.

Dans le cas des règles de filtrage, contrairement aux règles de regroupement et de tri, l'instruction se compose généralement de deux éléments :
- **Critère de filtre** : Relation entre la colonne filtrée et la valeur du filtre (par exemple, "est", "contient", "est vide")
- **Valeur du filtre** : La valeur sur laquelle le filtre est appliqué (par exemple, "123", "terminé")

Les règles de filtrage peuvent également être combinées avec les deux opérateurs booléens ET et OU. Dans le cas d'une combinaison **ET**, seules les entrées qui remplissent toutes les conditions définies sont affichées. Avec la liaison **OU**, vous pouvez filtrer la vue pour afficher toutes les lignes qui remplissent au moins une des conditions définies. Vous pouvez également utiliser les opérateurs ET et OU ensemble en utilisant les **groupes de filtres**.

[En savoir plus sur la fonction de filtrage]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})

## Verrouillage des paramètres de filtrage, de tri et de regroupement

Les réglages que vous effectuez au moyen de filtres, de regroupements et de tris sont enregistrés dans la vue actuelle. Si vous souhaitez les sauvegarder pour une utilisation future, vous pouvez [verrouiller la vue]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}) afin que personne ne modifie la vue.

{{< warning headline="Note importante" text="Avec les filtres, les regroupements et les tris, vous modifiez uniquement la façon dont les données sont affichées dans votre vue ! La base de données reste inchangée. Par conséquent, si des enregistrements ont disparu, vérifiez si vous êtes dans la bonne vue ou si vous avez masqué des enregistrements à l'aide d'un filtre." />}}

## Différences selon le type de vue

Tous les [types de vue]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) ne permettent pas le regroupement, le tri et le filtrage de la même façon. Obtenez une vue d'ensemble à l'aide de ce tableau :

| Type de vue | Filtrer | Trier | Regrouper |
| ------------------ | ------------------------------ | ------------------------------ | -------------------------- |
| **Tableau** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Kanban** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Calendrier** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Galerie** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Chronologie** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Arbre** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Big Data** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |