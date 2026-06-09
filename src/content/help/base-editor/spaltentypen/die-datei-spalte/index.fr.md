---
title: 'La colonne des fichiers'
date: 2022-11-16
lastmod: '2024-08-02'
categories:
    - 'dateien-und-bilder'
author: 'vge'
url: '/fr/aide/colonne-fichiers-seatable'
aliases:
    - '/fr/aide/die-datei-spalte'
seo:
    title: 'Colonne de fichiers SeaTable – organiser et partager'
    description: 'Utilisez la colonne de fichiers SeaTable pour télécharger, partager, renommer, supprimer et gérer tous vos documents depuis vos tableaux.'
weight: 10
---

Dans une **colonne de fichiers**, vous pouvez enregistrer un ou plusieurs fichiers et compléter ainsi la ligne correspondante par des documents.

## Comment créer une colonne de fichiers

![Créer une colonne.](images/Wie-man-eine-Spalte-anlegt.gif)

1. Cliquez sur le **symbole \[+\]** à droite de la dernière colonne de votre tableau.
2. Donnez un **nom** à la colonne dans le champ supérieur.
3. Sélectionnez le type de colonne **Fichier** dans le menu déroulant.

## Téléchargement de nouveaux fichiers

Vous pouvez **télécharger des fichiers** dans la colonne des fichiers en cliquant avec la souris sur une **cellule** et en sélectionnant le **symbole plus** qui apparaît. Dans la nouvelle fenêtre qui s'ouvre, vous pouvez **glisser-déposer** des fichiers ou cliquer avec la souris pour télécharger des fichiers depuis votre appareil.

![Téléchargement de pièces jointes dans une colonne de fichiers](images/upload-files-into-file-column.gif)

{{< warning  headline="Remarque"  text="SeaTable prend en charge les fichiers individuels d'une taille maximale de **200 Mo**. Vous pouvez télécharger **n'importe quel type de fichier** dans une colonne de fichiers, mais seuls certains documents Office et images peuvent être affichés et modifiés directement dans SeaTable." />}}

### Téléchargement de plusieurs nouveaux fichiers en même temps

![Télécharger plusieurs pièces jointes en même temps](images/upload-multiple-files-into-file-column.gif)

1. Cliquez dans la **cellule** d'une colonne de fichier.
2. Cliquez sur le **symbole plus** qui apparaît.
3. Une nouvelle fenêtre s'ouvre. Ici, vous pouvez télécharger des fichiers de votre appareil par **glisser-déposer** ou par **clic**.
4. Sélectionnez plusieurs fichiers en même temps en marquant tous les documents que vous souhaitez télécharger et en les téléchargeant ensemble.

{{< warning  headline="Connecté au gestionnaire de fichiers" >}}

Les fichiers que vous téléchargez localement dans une colonne de fichiers sont enregistrés dans un **dossier système** auquel vous pouvez accéder via le [gestionnaire de fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) de votre base.

{{< /warning >}}

## Ajouter des fichiers existants

Outre les nouveaux fichiers que vous téléchargez localement dans la cellule d'une colonne de fichiers, vous pouvez également ajouter des fichiers existants, qui peuvent provenir de **trois sources**:

- **Dernièrement téléchargé**: Vous trouverez ici les derniers fichiers téléchargés qui sont enregistrés dans le [gestionnaire de fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) de la base.
- **Mes dossiers**: vous avez ici accès à des fichiers dans vos propres dossiers, que vous pouvez créer et remplir dans la [gestion des fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).
- **Seafile**: Vous pouvez sélectionner ici les fichiers des [bibliothèques Seafile]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}) qui sont rattachées à votre base.

![Ajouter des fichiers existants à une colonne de fichiers](images/Add-existing-files-to-a-file-column.png)

1. Cliquez dans la **cellule** d'une colonne de fichiers et ensuite sur le **symbole plus** qui apparaît.
2. Une nouvelle fenêtre s'ouvre. Dans la navigation à gauche, sélectionnez la **source** à partir de laquelle vous souhaitez ajouter un fichier.
3. Cliquez dans la **structure des dossiers** jusqu'au fichier souhaité.
4. Sélectionnez le **fichier** et insérez-le dans la cellule en cliquant sur **Envoyer**.

## Téléchargement de fichiers

![Téléchargement de fichiers.](images/Herunterladen-von-Dateien.gif)

1. Dans la colonne Fichier, **double-cliquez** sur la cellule qui contient les documents que vous souhaitez télécharger.
2. Une nouvelle fenêtre s'ouvre. **Tous les fichiers** enregistrés dans la cellule y sont listés.
3. Ainsi, vous pouvez créer une **fichier unique** télécharger :
    - Passez le curseur de la souris sur le document et cliquez sur l'**icône de téléchargement** {{< seatable-icon icon="dtable-icon-download" >}}.
4. Ainsi, vous pouvez **plusieurs fichiers** télécharger :
    - Cliquez sur **Sélectionner**.
    - Choisissez l'option **Tout sélectionner** ou **cochez** les cases devant les fichiers.
    - Cliquez ensuite sur **Télécharger**.

Si vous souhaitez télécharger tous les fichiers d'une colonne, ouvrez le menu déroulant au-dessus de l'en-tête de la colonne et sélectionnez **Télécharger tout**.

![Télécharger tous les fichiers dans une colonne](images/Download-all-files.png)

Ensuite, vous pouvez encore définir **votre propre nom de fichier** et le système vous indique **combien de fichiers** seront inclus dans l'exportation.

![Boîte de dialogue pour télécharger tous les fichiers](images/Download-all-files-dialog.png)

En cliquant sur les **trois points**, vous avez deux options pour enregistrer le fichier : En cas de **téléchargement**, un fichier zip est enregistré sur votre appareil, à partir duquel vous pouvez extraire tous les fichiers. En outre, vous pouvez également **enregistrer** les fichiers **dans Seafile**. Pour cela, vous devez au préalable [connecter une bibliothèque Seafile à votre base]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}).

## Renommer des fichiers

![Renommer les pièces jointes d'une colonne de fichiers.](images/Datei-Spalte-Anhaenge-umbenennen.gif)

1. Ouvrez la fenêtre **Tous les fichiers** en **double-cliquant** sur une cellule de la colonne Fichiers.
2. Placez le curseur de la souris sur le fichier que vous souhaitez renommer et cliquez sur les **trois points**.
3. Sélectionnez l'option **Renommer** et saisissez un nouveau **nom de fichier**.

## Suppression de fichiers

![Suppression de pièces jointes.](images/Loeschen-von-Anhaengen.gif)

1. Ouvrez la fenêtre **Tous les fichiers** en **double-cliquant** sur une cellule de la colonne Fichiers.
2. Ainsi, vous pouvez créer une **fichier unique** supprimer :
    - Placez le curseur de la souris sur le fichier que vous souhaitez supprimer et cliquez sur les **trois points**.
    - Sélectionnez l'option **Supprimer**.
3. Ainsi, vous pouvez **plusieurs fichiers** supprimer :
    - Cliquez sur **Sélectionner**.
    - Choisissez l'option **Tout sélectionner** ou **cochez** les cases devant les fichiers.
    - Cliquez sur **Supprimer**.

{{< warning  headline="Remarque" >}}

De cette manière, les fichiers ne sont **pas** définitivement supprimés. Ce n'est que lorsque vous supprimez les fichiers dans le [gestionnaire de fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) de la base qu'ils sont [définitivement supprimés]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}}).

{{< /warning >}}

## Questions fréquentes

{{< faq "Un fichier peut-il être téléchargé lors d'un partage en lecture ?" >}}Oui, même si un utilisateur n'a qu'une **autorisation de lecture**, il peut télécharger des fichiers.
{{< /faq >}}
{{< faq "Est-il possible de lire des fichiers audio dans SeaTable ?" >}}Non. Pour pouvoir lire **des fichiers audio**, vous devez d'abord les télécharger.
{{< /faq >}}
{{< faq "Est-il possible de modifier l'ordre des fichiers dans une colonne de fichiers ?" >}}Non, l'ordre ne peut **pas** être modifié dans une colonne de fichiers. Le premier document téléchargé est placé en premier. L'ordre dans lequel vous téléchargez les documents vous permet de déterminer l'ordre dans la colonne des fichiers.

{{< /faq >}}
