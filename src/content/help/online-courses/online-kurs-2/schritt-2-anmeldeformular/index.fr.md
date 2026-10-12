---
title: "Étape 2 : Formulaire d'inscription"
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/fr/aide/etape-2-formulaire-d-inscription'
aliases:
    - '/fr/aide/schritt-2-anmeldeformular'
seo:
    title: 'Étape 2 : Formulaire d’inscription dans SeaTable'
    description: 'Apprenez à utiliser le formulaire intégré du cours SeaTable et à afficher uniquement les formations encore disponibles.'
---

Passons au formulaire web. Vous avez appris à en créer un au cours 1 : inutile de recommencer, celui-ci est déjà fourni avec la base.

Ouvrez le formulaire en mode édition : nous allons en voir les points essentiels.

## Le formulaire web et le choix du cours

Le formulaire est volontairement simple et ne demande que trois informations :

- Nom
- E-mail
- Cours

Les trois champs sont obligatoires. Les champs **Nom** et **E-mail** se passent d'explication.

La particularité tient au choix du cours : seuls les cours qui ont encore des places disponibles peuvent être choisis. Vérifiez-le vous-même : cliquez sur le champ, et seuls trois cours s'affichent, alors que le tableau en compte cinq.

![Formulaire web avec sélection de cours limitée aux cours disponibles](images/lvl2-limited-course-selection.png)

Pourquoi ? Parce que la colonne de lien est limitée à la vue `{{< seatable-icon icon="dtable-icon-main-view" >}} Available Courses`, qui n'affiche que les cours ayant encore des places. Le formulaire ne propose donc que les cours visibles dans cette vue.

SeaTable applique cette restriction jusque dans le formulaire web : un cours complet n'y est jamais proposé.

## Article d'aide avec plus d'informations

- [Comment lier des tableaux dans SeaTable]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})
- [Possibilités de configuration d'un formulaire web]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}})
