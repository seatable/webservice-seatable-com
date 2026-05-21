---
title: "Limites de l'importation CSV/Excel"
date: 2022-10-15
lastmod: '2024-05-10'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/fr/aide/limitations-import-csv-excel'
aliases:
    - '/fr/aide/limitationen-beim-csv-excel-import'
seo:
    title: 'Limitations pour import CSV/Excel dans SeaTable en détail'
    description: 'Découvrez toutes les limitations lors de l’import de fichiers CSV ou Excel avec SeaTable Cloud et Serveur. Nombre de lignes, taille de fichier et conseils.'

---

SeaTable dispose d'une fonction d'importation puissante pour vous permettre d'**importer** aussi facilement que possible **des enregistrements à partir de fichiers XLSX ou CSV**. Dans la plupart des cas, l'importation se fait sans difficulté. Si vous essayez d'importer trop d'enregistrements à la fois, SeaTable vous indiquera la limite à ne pas dépasser. Alors que les serveurs SeaTable auto-hébergés vous permettent de choisir librement les **limites de taille de fichier et de nombre de lignes**, SeaTable Cloud vous impose certaines limites.

## Taille de fichier et nombre de lignes maximum pour SeaTable Cloud

Lorsque vous importez des fichiers Excel, SeaTable prend en charge les fichiers d'une taille maximale de **100 Mo** et jusqu'à **50 000 lignes**. En raison de ces limites généreuses, vous ne devriez jamais rencontrer de problèmes liés à la taille des fichiers. Si vous avez un fichier plus grand ou contenant plus de lignes, vous devez le **diviser** en deux **fichiers Excel** et effectuer l'importation en deux étapes.

{{< warning  headline="Limite de mémoire pour les lignes" >}}

Le backend normal de SeaTable peut contenir au maximum 100.000 lignes par tableau. Si vous souhaitez importer un fichier Excel ou CSV contenant plus de 100.000 lignes, vous devez d'abord [activer le Big Data Backend]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) pour pouvoir [importer]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

{{< /warning >}}

## Graphiques et fichiers intégrés

L'importation de graphiques et de fichiers par fichier XLSX n'est **pas** possible. Pour une telle importation, il faut utiliser l'API SeaTable, qui permet d'importer sans difficulté des images et des fichiers.

## Liens vers d'autres enregistrements

Il n'est pas possible d'importer des données dans le type de colonne **Lien vers d'autres enregistrements**. Comme SeaTable est une [base de données relationnelle]({{< relref "posts/relationale-datenbank" >}}), les liens fonctionnent en outre différemment des références croisées dans Excel.

Vous trouverez tout sur l'utilisation de la colonne de lien dans SeaTable [ici]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< warning headline="Remarque" >}}
Après l'importation, vous pouvez également utiliser l'opération de traitement des données [Comparer et lier]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}) pour créer des liens entre des enregistrements spécifiques.
{{< /warning >}}

## Formats de fichiers différents

La fonction d'importation de SeaTable a été testée avec des fichiers de **LibreOffice** et des fichiers actuels de **Microsoft Excel**. Les autres programmes Office (comme ceux de la société Softmaker) ne sont **pas** testés activement, ce qui peut entraîner des résultats d'importation différents. En cas de doute, utilisez Microsoft Excel ou le logiciel gratuit LibreOffice pour obtenir les meilleurs résultats.

{{< warning  headline="Utilisez Excel ou Libre Office" >}}

Si vous rencontrez malgré tout des problèmes lors de l'importation de données, nous vous recommandons de jeter un coup d'œil à l'article [Conseils et astuces pour l'importation de fichiers CSV ou XLSX]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}}). Les pièges typiques y sont décrits.

{{< /warning >}}
