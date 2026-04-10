---
title: 'La colonne des collaborateurs'
date: 2023-01-07
lastmod: '2024-02-14'
categories:
    - 'datum-dauer-und-personen'
author: 'ssc'
url: '/fr/aide/colonne-collaborateurs-seatable'
aliases:
    - '/fr/aide/die-spalte-mitarbeiter'
seo:
    title: 'Colonne collaborateurs dans SeaTable : assignation, notifications et gestion'
    description: 'Colonne collaborateur SeaTable : attribuez des tâches, activez les notifications et utilisez-la pour filtres et automatisations.'
---

Dans la **colonne des collaborateurs**, vous pouvez attribuer une ou plusieurs **personnes** à une ligne. SeaTable vous permet de sélectionner aussi bien les personnes qui ont actuellement **accès** à la **base** que tous les autres membres de l'équipe qui n'y ont pas accès.

![La colonne des collaborateurs dans SeaTable](images/employee-column.png)

## Sélectionner les personnes ayant accès à la base

Si vous **double-cliquez** dans une cellule d'une colonne de collaborateurs, une liste de tous les utilisateurs qui ont actuellement accès à la base apparaît. Sélectionnez une ou plusieurs de ces **personnes**. Vous pouvez également utiliser le **champ de recherche** pour trouver un utilisateur spécifique.

![Sélectionner les personnes ayant accès à une base dans la colonne des collaborateurs](images/Personen-mit-Zugriff-auf-eine-Base-in-der-Mitarbeiter-Spalte-auswaehlen.png)

{{< warning  headline="Remarque"  text="Si l'accès à une base est **retiré** à un collaborateur, mais qu'il est inscrit dans une colonne de collaborateurs, la valeur reste inscrite dans la colonne jusqu'à ce que vous la supprimiez manuellement. Une fois supprimé, le collaborateur n'est plus disponible pour la sélection dans la liste." />}}

## Sélectionner des membres de l'équipe sans accès à la base

Si vous ne pouvez pas trouver un utilisateur via le champ de recherche dans la colonne des collaborateurs, cela signifie qu'il n'a actuellement **pas accès** à la base. S'il est **membre de votre équipe**, vous pouvez tout de même le saisir dans la colonne des collaborateurs.

Cliquez sur l'icône {{< seatable-icon icon="dtable-icon-add\_members" >}} pour ajouter des membres d'équipe sans accès. Saisissez le nom de l'utilisateur dans le **champ de recherche**, sélectionnez le **membre de l'équipe** souhaité et confirmez en cliquant sur **Ajouter**.

![Saisir les membres de l'équipe sans accès à une base dans la colonne des collaborateurs](images/Teammitglieder-ohne-Zugriff-auf-eine-Base-in-die-Mitarbeiter-Spalte-eintragen.gif)

## Notification du collaborateur lors de l'ajout

Lors de la création d'une colonne des collaborateurs, vous pouvez **activer** le **curseur** pour que les collaborateurs reçoivent une [notification]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) lorsque d'autres les inscrivent dans la colonne et les affectent ainsi à une ligne.

![Activation des notifications aux collaborateurs ajoutés à une colonne des collaborateurs](images/turn-on-notification-for-collaborateur-1.png)

Les collaborateurs reçoivent ensuite une notification correspondante dans la base, qu'ils peuvent consulter via l'**icône de la cloche** {{< seatable-icon icon="dtable-icon-notice" >}} en haut à droite.

![Notification de l'ajout d'un collaborateur](images/Benachrichtigung-wenn-Mitarbeiter-hinzugefuegt-wird.png)

## Définir la valeur par défaut

Vous pouvez définir un ou plusieurs collaborateurs comme [valeur par défaut]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) dans une colonne des collaborateurs. Vous avez le choix entre l'**utilisateur actuel** et **certains utilisateurs**. Chaque fois que quelqu'un ajoute une nouvelle ligne dans le tableau, soit le créateur de la ligne, soit les personnes sélectionnées sont alors automatiquement inscrites dans la colonne des collaborateurs.

![Définir les valeurs par défaut dans les colonnes du collaborateur](images/Set-default-values-in-collaborator-columns.png)

## Choisir les collaborateurs comme destinataires de notifications automatisées

Lorsque vous envoyez des notifications via [des automatismes]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}), vous pouvez sélectionner toutes les personnes inscrites dans la colonne des collaborateurs comme destinataires du message.

![Colonne du collaborateur pour les notifications automatisées](images/Collaborator-column-for-automated-notifications.gif)

## La colonne des collaborateurs dans les applications

La colonne des collaborateurs est également avantageuse dans l'[application]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Vous pouvez activer l'option permettant de voir les membres de l'équipe dans la liste déroulante pour tous les utilisateurs dans les [paramètres]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) de l'application.

Si vous ne souhaitez pas que les utilisateurs de l'application puissent voir les enregistrements d'autres utilisateurs, définissez **des filtres prédéfinis**: si une page est filtrée par la colonne des collaborateurs avec la condition "inclut l'utilisateur actuel", chaque utilisateur de l'application ne verra que les enregistrements qui lui sont attribués dans le tableau.

![Colonne des collaborateurs dans l'application](images/Mitarbeiter-Spalte-in-der-Universellen-App.gif)
