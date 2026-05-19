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

Nous allons maintenant nous pencher sur le formulaire Web. Comme vous avez déjà appris à créer un formulaire web avec SeaTable dans le premier cours en ligne, vous n'avez pas besoin de le faire à nouveau. Le formulaire web est déjà intégré au modèle.

Ouvrez maintenant le formulaire web en mode édition et nous discuterons brièvement des points les plus importants.

## Le formulaire web et la sélection des cours

Le formulaire web est volontairement simple et ne demande que trois valeurs :

- Nom
- Courriel :
- Cours

Les trois champs sont définis comme obligatoires. Les champs **Nom** et **E-mail** ne nécessitent pas d'explication supplémentaire.

La particularité réside dans la sélection des cours : Ici, seuls les cours qui disposent encore de places libres peuvent être sélectionnés. Faites-en vous-même l'expérience : Si vous cliquez sur le champ de sélection, seuls trois cours s'affichent, bien que cinq cours au total soient saisis dans le tableau.

![Formulaire web avec sélection de cours limitée aux cours disponibles](images/lvl2-limited-course-selection.png)

Pourquoi en est-il ainsi ? Nous avons réduit la sélection dans la colonne des liens à la vue `{{< seatable-icon icon="dtable-icon-main-view" >}} Available Courses` qui n'affiche que les cours avec des places disponibles. Ainsi, vous ne voyez dans le formulaire web que les cours qui sont disponibles dans cette vue.

SeaTable tient compte de cette restriction et s'assure que, même dans le formulaire web, seuls les cours qui ne sont pas encore complets sont proposés.

## Article d'aide avec plus d'informations

- [Comment lier des tableaux dans SeaTable]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})
- [Possibilités de configuration d'un formulaire web]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}})
