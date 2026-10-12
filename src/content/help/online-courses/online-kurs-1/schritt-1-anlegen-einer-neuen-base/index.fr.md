---
title: 'Étape 1 : Créer une nouvelle base'
date: 2024-08-30
lastmod: '2024-09-04'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/fr/aide/etape1-creer-base-depenses-seatable'
aliases:
    - '/fr/aide/schritt-1-anlegen-einer-neuen-base'
seo:
    title: 'Étape 1 Cours SeaTable 1 : créer une base de dépenses'
    description: 'Lancez le cours en ligne : créez une nouvelle base SeaTable, adaptez vos colonnes et catégories pour commencer à suivre efficacement toutes vos dépenses.'
---

Dans ce cours, vous allez créer un outil simple pour enregistrer et suivre vos dépenses personnelles ou professionnelles. Une fois terminé, il vous permettra de noter une dépense à tout moment, depuis votre ordinateur comme depuis votre téléphone. Le principe : chaque fois que vous sortez votre porte-monnaie, vous enregistrez la dépense. En échange de cet effort, vous voyez d'un coup d'œil combien vous avez dépensé, et pour quoi.

Commençons par créer la structure qui accueillera ces dépenses : une première base, puis quelques colonnes. Vous verrez, les étapes s'enchaînent presque naturellement.

{{< warning  headline="Un petit conseil pour suivre le cours confortablement"  text="Ouvrez deux fenêtres de navigateur et placez-les côte à côte : le cours dans l'une, SeaTable dans l'autre. Vous suivrez ainsi les étapes bien plus facilement, sans passer sans cesse d'une fenêtre à l'autre." />}}

![](images/level1-browser-window-setup.png)

## Créer une nouvelle base

Depuis la page d'accueil de SeaTable, créez une nouvelle base nommée `Expense Tracking`. Cliquez ensuite dessus pour l'ouvrir dans l'éditeur de base.

## Renommer le premier tableau

Toute nouvelle base contient un tableau nommé `Table 1`, avec une colonne et trois lignes.

- Supprimez les trois lignes.
- Renommez ensuite le tableau en `Expenses`.

{{< warning  headline="Si vous êtes bloqué"  text="SeaTable se prend en main assez intuitivement. Vous supprimez par exemple des lignes comme dans la plupart des logiciels : sélectionnez-les, puis faites un clic droit. Si vous avez besoin d'aide, pensez aux articles listés en bas de chaque page : ils donnent la marche à suivre pour chaque étape du cours." />}}

## Adapter les colonnes et en ajouter

Passons maintenant aux colonnes, pour que la base puisse recevoir les bonnes données.

- Renommez la première colonne `Name` en `Reason`.
- Ajoutez ensuite trois colonnes :

**Colonne 1 :**

> Nom : `Date`
>
> Type de colonne : `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date`
>
> Format : au choix
>
> À la minute près : `Yes`

**Remarque :** au lieu du type `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date`, nous aurions pu choisir `{{< seatable-icon icon="dtable-icon-creation-time" >}} Created time`. Une colonne de date se remplit à la main ; une colonne de ce type se remplit toute seule avec la date du jour, ce qui fait gagner du temps. En revanche, sa valeur ne se modifie pas : impossible, par exemple, de saisir après coup une dépense d'un autre jour.

---

**Colonne 2 :**

> Nom : `Amount`
>
> Type de colonne : `{{< seatable-icon icon="dtable-icon-number" >}} Number`
>
> Format : `Euro`

---

**Colonne 3 :**

> Nom : `Category`
>
> Type de colonne : `{{< seatable-icon icon="dtable-icon-single-election" >}} Single select`

---

{{< warning  headline="26 types de colonnes"  text="Vous n'avez vu qu'une petite partie des types de colonnes. Avec ses 26 types actuels, SeaTable peut stocker à peu près n'importe quelle information : c'est l'une de ses grandes forces." />}}

## Ajouter des options à la sélection unique

Votre colonne de sélection unique n'a pas encore d'options. Créez pour la colonne `Category` les quatre options suivantes :

- Clothing
- Groceries
- Leisure
- Travel

## Petite vérification

Bravo ! Si vous avez suivi les consignes à la lettre, votre base devrait maintenant ressembler à ceci :

![](images/level1-expenses-table.png)

Faisons le point sur ce que vous venez de créer en quelques clics : **une base dans laquelle vous pourrez désormais saisir toutes vos dépenses.**

Et en choisissant les types de colonnes, vous avez fait en sorte que chaque colonne n'accepte que les informations qui lui correspondent.

L'étape 1 est déjà terminée. Faites défiler la page jusqu'en bas et passez à l'**étape 2 : Créer un formulaire**.

## Article d'aide avec plus d'informations

- [Créer une nouvelle base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Comment personnaliser le type de colonne]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}})
- [Suppression d'une ligne]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}})
- [Ajout d’une colonne]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}})
- [Ajouter des options à une colonne de sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Particularités de la première colonne]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}})
- [Personnaliser l'apparence d'une base (icône et couleur)]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}})
