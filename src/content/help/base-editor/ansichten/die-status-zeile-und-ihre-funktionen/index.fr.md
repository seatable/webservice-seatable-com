---
title: "La barre d'état et ses fonctions"
date: 2023-02-21
lastmod: '2023-02-21'
categories:
    - 'ansichtsoptionen'
author: 'nsc2'
url: '/fr/aide/barre-detat-et-ses-fonctions'
aliases:
    - '/fr/aide/die-status-zeile-und-ihre-funktionen'
seo:
    title: 'Barre d’état SeaTable – compter et calculer facilement'
    description: 'Découvrez la barre d’état de SeaTable : comptez les lignes, affichez la somme, la moyenne, le minimum ou maximum de vos colonnes.'
---

La **barre d'état** se trouve en bas de vos tableaux et remplit fondamentalement deux fonctions différentes, qui sont expliquées plus en détail dans cet article :

- **Fonction 1**: Compter les lignes dans une vue
- **Fonction 2**: indication d'une valeur calculée à partir de toutes les entrées (par ex. somme, moyenne, etc.) pour les colonnes basées sur des chiffres

Grâce à la barre d'état, vous avez toujours ces **valeurs statistiques de base** sous les yeux dès que vous avez ouvert un tableau.

## Compter les lignes dans une vue

La barre d'état indique en bas à gauche le nombre de toutes les **lignes** qui se trouvent dans la **vue de tableau** actuellement ouverte. Si vous [filtrez dans une vue]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), la barre d'état ne compte que les entrées de tableau restantes.

![La barre d'état indique toujours le nombre de lignes dans la vue de tableau actuellement ouverte](images/status-cell-function-1.jpg)

En outre, vous pouvez [sélectionner des lignes]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) individuelles – et la barre d'état ne se réfère alors qu'aux entrées sélectionnées.

## Indication d'une valeur calculée à partir de toutes les entrées

Pour les **colonnes basées sur des chiffres**, la barre d'état indique pour chaque colonne une **valeur** calculée à partir de toutes les entrées.

![Valeurs calculées dans les lignes d'état](images/the-status-cell-function-2-1.png)

## Options de calcul

Pour les colonnes basées sur des chiffres, les **options de calcul** suivantes sont disponibles dans la barre d'état :

- Calcul de la **somme** de toutes les entrées de la colonne
- Calcul de la **moyenne** de toutes les entrées de la colonne
- Calcul de la **médiane** à partir de toutes les entrées de la colonne
- Détermination de la **valeur maximale** à partir de toutes les entrées de la colonne
- Détermination de la **valeur minimale** à partir de toutes les entrées de la colonne
- Pas de calcul

![Options de calcul de la barre d'état](images/berechnungsoptionen-status-zeile.png)

## Types de colonnes et formats compatibles

Pour les types de colonnes suivants, la barre d'état indique une valeur calculée :

- [Colonnes de nombres]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
    - Nombre
    - Pourcentage
    - Monnaie
- [Colonnes de durée]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- [Colonnes de classement]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Valeurs numériques dans [les colonnes de formules]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

Pour les types de colonnes suivants, la barre d'état ne donne **pas** de valeur calculée, bien qu'ils contiennent (ou puissent contenir) des chiffres :

- [Colonnes de dates]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Date de création]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) y [Date de dernière modification]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Numéro automatique]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Chiffres dans [les colonnes de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
