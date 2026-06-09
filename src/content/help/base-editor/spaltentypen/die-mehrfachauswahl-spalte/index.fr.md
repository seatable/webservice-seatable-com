---
title: 'La colonne de sélection multiple'
date: 2023-03-28
lastmod: '2025-07-15'
categories:
    - 'spalten'
author: 'kgr'
url: '/fr/aide/colonne-selection-multiple'
aliases:
    - '/fr/aide/die-mehrfachauswahl-spalte'
seo:
    title: 'Colonne de sélection multiple SeaTable : options'
    description: 'Découvrez la colonne de sélection multiple : couleurs, tri libre, import/export, couleurs personnalisées, différences avec la sélection simple.'
weight: 8
---

Une colonne de sélection multiple est idéale si vous souhaitez attribuer à vos lignes d'une colonne **plusieurs options** parmi une liste d'options à définir. Les options reçoivent des étiquettes colorées qui vous permettent d'étiqueter vos enregistrements et de rendre vos tableaux plus clairs, par exemple en [filtrant]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) sur des options spécifiques.

![Exemple de tableau avec une colonne de sélection multiple](images/example-table-multiple-select.png)

## Création d'une colonne de sélection multiple

La création d'une colonne de sélection multiple est un jeu d'enfant et se fait en quelques clics. Vous trouverez des informations détaillées sous [Ajouter une colonne]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

1. Cliquez sur le **symbole \[+\]** à droite de la dernière colonne du tableau.
2. Donnez un **nom** à la nouvelle colonne.
3. Sélectionnez **Sélection multiple** comme type de colonne.
4. Confirmez en cliquant sur **Envoyer**.

## Points communs avec la colonne de sélection unique

### Ajouter des options de sélection multiple

L'ajout d'options à une colonne de sélection multiple fonctionne **de la même manière que pour une colonne de sélection unique**. Vous pouvez ajouter de nouvelles options de plusieurs manières. Pour en savoir plus, consultez l'article [sur la colonne de sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}).

### Exporter et importer des options de sélection multiple

Vous pouvez **exporter** et **importer** les options d'une colonne de sélection multiple comme pour une colonne de sélection unique. Pour plus d'informations, consultez l'article sur la colonne de sélection unique.

### Couleurs des options

Actuellement, vous disposez de **24 couleurs** pour mettre en valeur les options, comme pour une colonne à sélection unique.

![Couleurs de la colonne de sélection unique](images/farben-einfachauswahl.png)

Avec un [abonnement Enterprise]({{< relref "help/teamverwaltung/abonnement/abo-pakete" >}}), vous avez également la possibilité de créer [vos propres couleurs]({{< relref "help/base-editor/weitere-optionen/eigene-farben-in-einer-base-hinzufuegen" >}}) pour vos options de sélection multiples.

### Modifier l'ordre des options de sélection multiple

L'ordre des options peut être ajusté de la même manière que pour une colonne de sélection unique. Il est essentiel si vous souhaitez [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) ou [grouper]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) après la colonne de sélection multiple. En effet, SeaTable ne classe pas les options **par ordre alphabétique**, mais s'adapte de manière flexible à **l'ordre des options** que vous définissez par glisser-déposer.

### Définir la valeur par défaut

Contrairement à une colonne de sélection unique, une colonne de sélection multiple **ne vous permet pas** de définir une valeur par défaut.

## Sélection multiple ou lien vers d'autres entrées ?

Si vous souhaitez **enregistrer des informations supplémentaires** pour chaque option de sélection, vous devriez envisager d'utiliser une [colonne de liaison]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) plutôt qu'une colonne de sélection multiple. Pour ce faire, créez des enregistrements complets pour toutes les options dans un tableau séparé, que vous pouvez lier à autant de lignes que vous le souhaitez dans d'autres tableaux.
