---
title: 'Traitement des données : comparer et copier'
date: 2023-03-17
lastmod: '2023-11-27'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/fr/aide/comparer-copier-donnees-seatable'
aliases:
    - '/fr/aide/datenverarbeitung-vergleichen-und-kopieren'
seo:
    title: 'Comparer et copier des données dans SeaTable'
    description: 'Copiez des valeurs entre deux tableaux SeaTable dès que certains champs sont identiques – simple et automatisé.'
---

La fonction de traitement des données vous permet d'effectuer diverses opérations sur une colonne. **Comparer et copier** est une opération qui vous permet de copier les valeurs d'une colonne d'un tableau dans la colonne d'un autre tableau, à condition qu'une certaine valeur de comparaison soit identique dans les deux enregistrements.

## Mise en place de l'opération

![Création d'une action de traitement des données](images/create-an-data-processing-action-1.jpg)

1. Ouvrez n'importe quel **tableau** et cliquez sur les **trois points** dans les options d'affichage.
2. Cliquez sur **Traitement des données**, puis sur **Ajouter une opération de traitement des données**.
3. Donnez un **nom** à l'opération et sélectionnez **Comparer et copier**.

![Désignation de l'action de traitement des données et sélection du type d'opération](images/name-operation-and-select-operation-type-exmaple-copy.jpg)

5. Définissez **de quel tableau** proviennent les données et **dans quel tableau** vous souhaitez copier les données.
6. Définissez une ou plusieurs **conditions** dans lesquelles deux colonnes des tableaux comparés doivent avoir une valeur identique pour que l'opération soit exécutée.
7. Sélectionnez une ou plusieurs **colonnes sources** à partir desquelles les valeurs seront copiées dans des **colonnes de résultats** à définir également, pour autant que les conditions de correspondance que vous avez définies soient remplies.

![Définition de l'action de traitement des données](images/name-operation-and-define-columns-example-copy-1.png)

{{< warning  headline="Remarque"  text="En cliquant sur **Ajouter**, vous pouvez sélectionner autant de colonnes que vous le souhaitez pour d'autres **conditions** ou **opérations de copie**." />}}

11. Cliquez sur **Enregistrer** pour sauvegarder l'action et l'exécuter plus tard, ou sur **Exécuter** pour l'exécuter directement.

Lors de la première exécution réussie, une petite icône apparaît dans la marge inférieure gauche. **crochet vert**.  
![Si la première exécution de l'action de traitement des données est réussie, une coche verte apparaît.](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Cas d'utilisation

Un cas concret d'utilisation de cette opération de traitement des données pourrait par exemple se présenter si vous gérez les **données des collaborateurs** de votre équipe dans un tableau et souhaitez créer les **tâches de votre équipe** qui doivent encore être effectuées dans un nouveau tableau. En ajoutant une colonne avec les **noms** des collaborateurs responsables de chaque tâche, vous souhaitez créer une correspondance entre les tableaux.

Ensuite, vous souhaitez que certaines données des collaborateurs, qui existent déjà dans le tableau des collaborateurs, soient copiées dans le tableau des tâches. Par exemple, vous pourriez aussi avoir besoin de l'**adresse e-mail** pour pouvoir contacter directement la personne responsable.

Pour mettre en œuvre cette opération de traitement des données, vous avez besoin de **deux tableaux dans la même base**. Dans le premier tableau, vous gérez les **données des employés**, qui comprennent entre autres les **adresses e-mail** des employés.

![Exemple de tableau pour la gestion des données personnelles des travailleurs](images/example-table-employees-and-personal-data-1.png)

Dans le deuxième tableau, vous saisissez les **tâches ouvertes**, pour lesquelles le collaborateur responsable est saisi dans une autre colonne. En outre, vous créez une nouvelle colonne de type [e-mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}), dans laquelle les adresses e-mail seront copiées ultérieurement.

![Tableau cible avec colonne de résultats avant l'exécution de l'action de traitement des données](images/table-open-tasks-before-data-processing-operation-1.png)

Pour créer l'opération de traitement des données, suivez les étapes décrites ci-dessus. Pour le cas d'application concret, sélectionnez comme **condition** que le nom d'un collaborateur dans la colonne **name** du tableau **employees** doit correspondre au nom dans la colonne **responsible** du tableau **open tasks**. Cette étape est essentielle pour que les données correctes des collaborateurs concernés soient copiées lors de l'opération de traitement des données.

![Définition de la condition de concordance pour l'action de traitement des données](images/define-condition-for-data-operation-compare-and-copy.png)

{{< warning  headline="Remarque importante"  text="Pour cette opération de traitement des données, les colonnes à comparer doivent avoir **le même type de colonne** afin que SeaTable puisse détecter de manière fiable les valeurs identiques." />}}

Dans l'étape suivante, vous pouvez sélectionner un nombre quelconque de colonnes sources dans le tableau **employees**, dont le contenu sera copié dans les colonnes de résultats sélectionnées du tableau **open tasks** lorsque l'opération sera exécutée et que la condition de concordance que vous venez de définir sera remplie.

![Sélection des colonnes du tableau source dont le contenu sera copié dans le tableau cible si la condition de concordance est remplie.](images/select-columns-to-copy.png)

{{< warning  headline="Attention à la perte de données" >}}

Les colonnes source et résultat doivent avoir **le même type de colonne** afin de ne pas perdre de données lors de la copie. Vous pouvez par exemple copier des données d'une [colonne de date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) dans une [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}), mais elles ne conviennent plus pour les [calendriers]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}). Avant d'effectuer l'opération, créez donc une **colonne de résultats** du même type dans le tableau cible pour chaque **colonne source** que vous souhaitez copier.

{{< /warning >}}

Si l'opération est exécutée avec succès, les tableaux **employees** et **open tasks** sont examinées pour voir si les colonnes **name** et **responsible** définies correspondent. Si les **noms** dans les colonnes des deux tableaux correspondent, l'**adresse e-mail** de l'employé correspondant est automatiquement copiée de la colonne **E-mail** définie dans la colonne de résultat **contact**.

![Contenu copié dans le tableau cible après le déclenchement de l'action de traitement des données](images/table-after-data-processing-operation-2.png)

{{< warning  headline="Remarque"  text="Pour faciliter la compréhension, nous avons décidé, dans le cas d'application, de ne copier qu'**une seule colonne** à l'aide de l'opération de traitement des données. Pour augmenter l'impact, il est bien sûr possible de sélectionner un plus grand nombre de colonnes sources et de résultats." />}}

## Types de colonnes non pris en charge

Les types de colonnes suivants ne peuvent **pas** être copiés à l'aide de l'opération _Comparer et copier_ et ne sont donc **pas** disponibles lors de la définition des colonnes source et résultat.

- [Colonne à choix multiples]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})
- [La colonne Créateur]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})
- [La colonne Dernier intervenant]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Bouton]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
