---
title: "Limitations de l'utilisation des données volumineuses"
date: 2023-05-11
lastmod: '2024-12-16'
categories:
    - 'big-data'
author: 'nsc2'
url: '/fr/aide/limites-big-data-seatable'
aliases:
    - '/fr/aide/einschraenkungen-in-der-nutzung-von-big-data'
seo:
    title: 'Big Data SeaTable : limites et conseils essentiels'
    description: 'Explorez les restrictions clés du Big Data dans SeaTable – synchronisation, édition, droits d’accès, opérations et bonnes pratiques pour exploiter vos données.'

---

Une vue normale dans SeaTable permet le travail **collaboratif** **en temps réel** pour **jusqu'à 100 000 lignes**. Le Big Data vous permet de **stocker un** nombre **illimité** de lignes, mais réduit vos possibilités de collaboration. Avant d'utiliser Big Data, n'oubliez pas de jeter un coup d'œil à cet article d'aide pour connaître les restrictions auxquelles vous devez vous attendre lors de l'utilisation de Big Data.

## Limites du Big Data

Le stockage de données volumineuses vous permet de **stocker des lignes de manière** largement **illimitée**, mais il comporte également certaines restrictions. Vous trouverez ci-dessous un aperçu de ces **restrictions**:

- Les modifications apportées à une entrée Big Data ne sont **pas** **synchronisées** **en temps réel** dans le navigateur d'un autre utilisateur. Les modifications ne sont visibles pour les autres utilisateurs qu'après un **rechargement de** la page.
- Vous ne pouvez **pas partager** les vues Big Data, que ce soit individuellement ou dans le cadre [d'autorisations de partage personnalisées]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}).
- Il n'est **pas** possible de créer **de nouvelles lignes** dans un affichage Big Data. Cela doit toujours se faire dans un [affichage normal]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}).
- Dans un affichage Big Data, vous ne pouvez pas [personnaliser]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}).
- Vous ne pouvez **pas modifier**[les entrées liées]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) dans les entrées Big Data. Les liens vers des lignes dans le stockage Big Data ne sont **pas affichés** dans les vues normales - mais le sont dans une vue Big Data.
- La mise en forme conditionnelle[(mise en couleur des lignes]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}).
- [Les opérations de traitement des données]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) ne sont **pas** disponibles dans le cadre des Big Data. La seule exception est la [comparaison et la liaison]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}). Cette opération peut relier des entrées dans la mémoire Big Data à des lignes dans n'importe quel autre tableau, que les lignes soient stockées dans la base ou dans la mémoire Big Data.
- La fonction [Rechercher et remplacer]({{< relref "help/base-editor/tabellen/suchen-und-ersetzen-von-werten-in-seatable" >}}) n'est **pas** disponible.

{{< warning  headline="Nombre de ces limitations du Big Data ne s'appliquent pas à l'application" >}}

La plupart des utilisateurs de l'espace de stockage de données volumineuses ne se sentent pas gênés dans leur travail par ces restrictions. Si toutefois vous êtes concernés, vous pouvez jeter un coup d'œil à l'[application]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Certaines des restrictions mentionnées ne s'y appliquent pas.

{{< /warning >}}
