---
title: 'La colonne des nombres'
date: 2023-01-08
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/fr/aide/colonne-numerique'
aliases:
    - '/fr/aide/die-zahlen-spalte'
seo:
    title: 'Colonne numérique SeaTable – formats et paramétrages'
    description: 'Gérez chiffres, montants ou pourcentages dans SeaTable. Paramétrez vos colonnes numériques et facilitez l’analyse de vos données.'
weight: 3
---

Dans SeaTable, vous pouvez utiliser la **colonne des nombres** de manière polyvalente pour travailler avec des nombres de toutes sortes (par exemple, le nombre d'objets, pourcentages ou prix dans différentes devises).

## Champ d'application de la colonne des nombres

L'utilisation de **la colonne des nombres** vous permet par exemple de **calculer des valeurs** avec des formules et de créer des **diagrammes et des statistiques**. Cependant, elle ne convient pas pour stocker des chaînes de caractères aussi longues que vous le souhaitez (par exemple, des numéros de compte), car les chiffres supérieurs à 15 sont arrondis. Dans ce cas, vous devez utiliser [la colonne du texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

En outre, SeaTable propose d'autres types de colonnes qui correspondent parfois mieux aux valeurs à stocker :

- Durée et périodes = [colonne de durée]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- Date et points de temps = [colonne de date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- Scores = [colonne de classement]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Numéros de série = [Numéro automatique]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Numéros de téléphone = [colonne des numéros de téléphone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})
- Informations géographiques = [colonne de géopositionnement]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

## Ajouter une colonne des nombres

![Ajouter une colonne des nombres](images/hinzufuegen-einer-zahlenspalte.gif)

1. Cliquez sur le **symbole plus** à droite de la dernière colonne.
2. Donnez un **nom** à la colonne.
3. Sélectionnez **Nombre** comme type de colonne.
4. Choisissez un **format** (par ex. nombre, pourcentage ou devise).
5. En cliquant sur **Autres paramètres**, vous pouvez en outre régler des détails.
6. Ajoutez la colonne en cliquant sur **Envoyer**.

## Paramètres de format

Vous pouvez également modifier et affiner le **format des chiffres** après coup. Pour ce faire, ouvrez d'abord le menu déroulant avec les **options de colonne** en cliquant sur le triangle {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} dans l'en-tête de colonne et cliquez ensuite sur {{< seatable-icon icon="dtable-icon-set-up" color="grey" >}} **Paramètres de format**.

Vous pouvez maintenant choisir un autre **format**, régler les **séparateurs de déc** **imales** et **de milliers** et modifier le nombre de **décimales**.

### Formats disponibles pour la colonne des chiffres

Les formats des nombres suivants sont à votre disposition :

- **Nombre**

    Utilisation d'un nombre simple, par exemple pour le nombre d'objets.

- **Pourcentage**

    Utilisation de pourcentages, par exemple pour la progression dans la réalisation de tâches.

- **Devises (yuan, dollar & euro)**

    Utilisation de différentes devises, par exemple pour les prix des produits.

- **Devise personnalisée**

    Utilisation d'une devise personnalisée, pour laquelle le symbole de la devise peut être saisi individuellement.

## Définir la valeur par défaut et valider la saisie

Vous pouvez [définir]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) pour chaque colonne des nombres, qui sera automatiquement inscrite sur chaque nouvelle ligne que vous ajoutez à votre tableau.

Pour identifier directement les **erreurs** et **les valeurs extrêmes**, vous pouvez en outre **valider** la **saisie**. Pour ce faire, vous définissez une **plage des nombres** dans laquelle les valeurs de la colonne doivent se situer ; les cellules avec une valeur plus élevée ou plus basse sont alors mises en évidence par une couleur.

Vous pouvez effectuer ces réglages lors de la création de la colonne des nombres ou ultérieurement :

1. Ouvrez le menu déroulant avec les **options de colonne** en cliquant sur le triangle {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} dans l'en-tête de la colonne.
2. Cliquez ensuite sur **Personnaliser le type de colonne**.
3. Cliquez sur **Autres paramètres** et activez tout en bas les **curseurs** correspondants.

![Paramètres de format des colonnes de nombres](images/Format-settings-of-number-columns.png)
