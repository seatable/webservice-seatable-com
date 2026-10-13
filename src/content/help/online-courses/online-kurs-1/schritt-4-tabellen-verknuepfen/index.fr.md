---
title: 'Étape 4 : Lier les tableaux'
date: 2024-08-30
lastmod: '2024-09-19'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/fr/aide/etape-4-lier-tables'
aliases:
   - '/fr/aide/schritt-4-tabellen-verknuepfen'
seo:
    title: 'Étape 4 : Relier et gérer vos tableaux SeaTable en toute simplicité'
    description: 'Découvrez comment relier des tableaux dans SeaTable, structurer vos données, automatiser les mises à jour et garantir la cohérence de vos enregistrements.'
---

Dans SeaTable, des colonnes de lien permettent de relier plusieurs tableaux entre eux. Pour découvrir cette fonctionnalité très puissante, vous allez ajouter un second tableau, consacré aux catégories de dépenses, et le relier au premier.

## Petite parenthèse : pourquoi relier les données ?

Relier des enregistrements est l'une des fonctions centrales de SeaTable : c'est ce qui le distingue d'un tableur classique et lui donne la puissance d'une base de données relationnelle. Cela paraît complexe, mais vous allez voir par vous-même que ça ne l'est pas. Relier ses données présente trois grands avantages :

- **plus de clarté** : relier des tableaux donne à vos données une structure claire. Plutôt que de tout regrouper dans un seul tableau, au risque de répéter les mêmes informations, vous rangez les données liées entre elles, comme les dépenses et les catégories, dans des tableaux distincts. Vos données restent cohérentes, sans doublons ;
- **des analyses plus souples** : les tableaux reliés permettent de croiser et d'analyser des données de provenances différentes. Vous pouvez par exemple analyser en un instant toutes les dépenses d'une catégorie ou d'un service ;
- **une gestion plus simple** : une modification apportée dans un tableau se répercute automatiquement dans tous les tableaux qui lui sont reliés. Vos données restent à jour et cohérentes, sans avoir à les modifier à plusieurs endroits.

## Étendre la structure de la base

Pour créer des liens, il faut un second tableau. Créons-le.

1. Dans la même base, créez un second tableau nommé `Categories`.
2. Ce tableau n'a besoin que d'une colonne, `Name`, qui existe déjà : rien à faire de ce côté.
3. Ajoutez à la main quatre lignes dans le tableau `Categories` :

    - `Travel`
    - `Clothing`
    - `Groceries`
    - `Leisure`

    ![Tableau « Categories » avec quatre catégories : Travel, Clothing, Groceries, Leisure](images/level1-categories.png)

4. Revenez au tableau `Expenses`.

5. Ajoutez-y une colonne nommée `Category-Link`, de type `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Link to other records`, qui pointe vers le tableau `Categories`.  
   ![Boîte de dialogue pour créer la colonne de lien « Category-Link » vers le tableau « Categories »](images/level1-create-link-column.png)

## Relier les enregistrements des deux tableaux

Pour relier les enregistrements des deux tableaux, vous avez deux possibilités :

1. À la main : dans une cellule du tableau `Expenses`, cliquez sur le bouton {{< key "+" >}}, puis choisissez la catégorie qui convient. Avec beaucoup de données, cela devient vite fastidieux, et les erreurs arrivent vite.  
   ![Liaison manuelle d’une ligne de dépense à une catégorie via l’icône plus](images/level1-link-rows.png)
2. Automatiquement, grâce aux [opérations de traitement des données]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) de SeaTable.  
   ![Menu « Data Processing » avec sélection d’une opération de traitement de données dans le tableau](images/level1-data-operation.png)

### Relier les enregistrements par une opération de traitement des données

Créez une nouvelle opération de traitement des données nommée `Assign Category`, de type `Auto add link`.

Réglez ensuite les paramètres suivants, pour indiquer à SeaTable comment relier vos données :

- Tableau : `Expenses`
- Autre tableau : `Categories`
- Si colonne : `{{< seatable-icon icon="dtable-icon-single-election" >}} Category`
- colonne : `{{< seatable-icon icon="dtable-icon-single-line-text" >}} Name`

![Opération de traitement « Assign Category » de type « Auto add link » avec champs correspondants](images/level1-auto-add-link.png)

Cliquez sur Exécuter pour lancer l'opération : d'un seul coup, chaque ligne du tableau `Expenses` est reliée à une ligne du tableau `Categories`.

{{< warning  headline="S'il manque des liens"  text="Si certaines lignes restent sans lien après l'opération, vous avez sans doute fait une faute de frappe en saisissant les quatre catégories du tableau `Categories`. Corrigez-la, puis relancez l'opération." />}}

## Supprimer la colonne devenue inutile

Une fois toutes les lignes reliées, vous pouvez supprimer la colonne `Category` du tableau `Expenses` : inutile de stocker deux fois la même information.

## Retour sur le formulaire web

Si vous rouvrez votre formulaire web, vous constaterez que la catégorie de la dépense n'est plus demandée. Pourquoi ?  
En supprimant la colonne `Category`, vous avez aussi supprimé le champ correspondant du formulaire : SeaTable n'a plus de colonne où enregistrer cette donnée.

La leçon à en tirer ? Un grand pouvoir implique de grandes responsabilités. Dans SeaTable, ajouter ou supprimer une colonne prend quelques secondes, et la plupart des modifications de colonnes sont sans risque. Mais avant de supprimer une colonne ou de changer son type, vérifiez rapidement si d'autres éléments en dépendent.

Ajoutez donc au formulaire web la colonne `Category-Link` que vous venez de créer, pour pouvoir de nouveau saisir vos dépenses comme avant. Vous y arriverez sans peine.

## Article d'aide avec plus d'informations

- [Ajouter un tableau à une base]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}})
- [Comment lier des tableaux dans SeaTable]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})
- [Traitement des données Comparer et relier]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}})
