---
title: 'Opérations de traitement des données dans SeaTable'
date: 2023-03-20
lastmod: '2023-04-28'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/fr/aide/operations-traitement-donnees-seatable'
aliases:
    - '/fr/aide/datenverarbeitungsoperationen-in-seatable'
seo:
    title: 'Traitement des données dans SeaTable : opérations sur lignes'
    description: 'Réalisez des calculs et reliez des valeurs entre tableaux dans SeaTable : puissantes opérations de traitement de données à votre portée.'
star: true
weight: 1
---

La fonction de traitement des données est une fonctionnalité utile de SeaTable qui vous permet d'**effectuer des opérations** dans une colonne sur plusieurs lignes. En définissant une opération, vous pouvez soit effectuer divers **calculs mathématiques**, soit établir **des relations entre des valeurs** dans différents tableaux. Les opérations de traitement des données ont un impact particulièrement important dans les ensembles de données volumineux, dans lesquels vous pouvez effectuer un grand nombre de calculs.

## Le sens derrière les opérations de traitement des données

SeaTable pense souvent en termes de lignes. Par exemple, une [formule]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) ne peut mettre en relation que les valeurs d'une ligne et [les liens entre les tableaux]({{< relref "help/base-editor/tabellen/tabellen-miteinander-verlinken" >}}) se font toujours de ligne à ligne.

Par opposition, le traitement des données est une fonction permettant d'effectuer des opérations dans une colonne sur plusieurs lignes. En principe, on distingue deux types d'opérations de traitement des données :

- **Calculs mathématiques** sur toutes les valeurs d'une colonne. Exemple : nombre de visites sur un site web.
- **Mettre en relation des valeurs** lorsqu'elles sont identiques dans deux tableaux. Exemple : attribuer les paiements reçus à une facture.

## Opérations mathématiques et relationnelles

Les **opérations mathématiques** suivantes peuvent actuellement être effectuées à l'aide de la fonction de traitement des données :

- [Calculer les valeurs cumulées]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calculer le classement]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Calculer les changements]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calculer le pourcentage]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})

Les **opérations** suivantes **sur les relations** peuvent actuellement être effectuées à l'aide de la fonction de traitement des données :

- [Comparer et relier]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}})
- [Comparer et copier]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})
- [Transférer le nom d'utilisateur]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})

## Conditions préalables à la définition des opérations

Les deux types d'opérations de traitement des données sont soumis à des **conditions** différentes, qui doivent être remplies pour pouvoir créer une opération correspondante.

- **Les opérations mathématiques** supposent la présence de **deux colonnes de chiffres** dans votre tableau.
- Pour les **opérations sur les liens**, vous avez besoin de types de colonnes bien spécifiques selon le cas d'utilisation, par exemple une [colonne de collaborateurs]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) et une [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) lors du transfert de noms d'utilisateurs.

## Remarques sur l'exécution

Les opérations de traitement des données peuvent actuellement être exécutées [manuellement]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-ausfuehren" >}}) ou [par automatisation]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) l'avenir.

Chaque fois que l'opération de traitement des données est exécutée, les **résultats** sont écrits dans la **colonne des résultats** sans tenir compte des pertes. Si vous ne voulez pas écraser de données, vous devez [créer]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}) pour les résultats.

Contrairement aux **colonnes de formules** qui surveillent en permanence les colonnes impliquées, les **colonnes de résultats** ne s'actualisent _pas_ d'elles-mêmes. Les modifications des valeurs dans la colonne source n'ont _pas_ d'effet sur les valeurs dans la colonne des résultats sans [automatisation]({{< relref "help/base-editor/automationen/beispiel-datenverarbeitungsoperation-per-automation-ausfuehren" >}}) ou nouvelle exécution. C'est pourquoi vous pouvez également écraser manuellement les valeurs calculées ou mises en relation.

## Protection contre les modifications

Afin d'éviter tout malentendu, nous recommandons de ne **pas apporter de modifications manuelles** aux colonnes concernées et de les [verrouiller]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) pour plus de sécurité après l'exécution (nécessite un abonnement Plus ou Enterprise).

![Colonnes de résultats d'actions de traitement de données bloquées pour le traitement ](images/locked-score-columns.jpg)

N'oubliez pas que les valeurs calculées ou mises en relation sont un **instantané** au moment de l'exécution. Si vous n'exécutez pas à nouveau l'opération, les résultats peuvent être obsolètes si les valeurs de la colonne source ont changé entre-temps.
