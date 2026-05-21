---
title: 'Exporter une base en tant que fichier DTABLE'
date: 2023-01-11
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'kgr'
url: '/fr/aide/exporter-base-formulaire-dtable'
aliases:
    - '/fr/aide/speichern-einer-base-als-dtable-datei'
seo:
    title: 'Exporter une base SeaTable au format DTABLE : guide pratique et précautions'
    description: 'Exportez votre base SeaTable en fichier DTABLE pour sauvegardes ou transferts : contenu complet, sans historique, attention à la taille.'
---

Vous pouvez à tout moment exporter une base en tant que fichier DTABLE et enregistrer ainsi une sauvegarde complète sur votre appareil. L'article suivant vous explique comment cela fonctionne et ce à quoi vous devez faire attention.

## Comment exporter une base

![Exporter la base](images/Base-exportieren.png)

1. Allez sur la **page d'accueil** de SeaTable.
2. Placez le curseur de la souris sur le nom de la **base** que vous souhaitez exporter et cliquez sur l'**icône à trois points** qui apparaît à l'extrême droite.
3. Sélectionnez l'option de menu **Exporter**.

[Export de la base](images/export-base.png)

4. Décidez si vous souhaitez inclure les **Assets** (p. ex. les images et les fichiers) et la dernière **sauvegarde de Big Data** dans le fichier d'exportation en activant ou en désactivant les curseurs.
5. Confirmez avec **Exporter**.

Selon les paramètres du navigateur, soit le **téléchargement** démarre automatiquement, soit il vous est demandé où vous souhaitez enregistrer le fichier d'exportation. Choisissez le cas échéant un **emplacement** approprié et confirmez votre choix.

Dès que votre fichier avec l'extension **.dtable** apparaît à l'emplacement indiqué, l'exportation de la base est terminée.

{{< warning  headline="Remarque" >}}

Soyez prêt à ce que le **fichier DTABLE** soit très **volumineux** si vous avez fait un usage intensif des colonnes de fichiers et d'images dans la base exportée. Le nuage SeaTable permet d'exporter des bases d'une **taille maximale de 100 Mo**. Grâce au [gestionnaire de fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}), vous pouvez **supprimer les pièces jointes** des bases qui dépassent cette limite de taille afin de permettre l'exportation.

{{< /warning >}}

## Que stocke un fichier DTABLE ?

Le fichier DTABLE exporté contient l'état actuel de votre base, y compris tous les

- Tableaux et vues,
- Lignes, colonnes et valeurs,
- Images et fichiers,
- Formulaires web,
- Statistiques,
- Scripts,
- Plugins et
- Apps.

{{< warning  headline="Attention"  text="Cependant, un fichier DTABLE n'enregistre **pas** l'historique de la base. Les snapshots, les commentaires, le contenu supprimé dans la corbeille et le journal ne sont pas inclus dans le fichier d'exportation. Les données du Big Data Backend ne sont pas non plus exportées dans le fichier DTABLE." />}}

## Restaurer une base à partir d'un fichier DTABLE

Vous pouvez à tout moment **réimporter** un fichier DTABLE comme nouvelle base dans SeaTable. Pour en savoir plus, consultez l'article [Créer une base à partir d'un fichier DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}}).
