---
title: 'La vue de calendrier'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/fr/aide/vue-de-calendrier'
aliases:
    - '/fr/aide/guide-plugin-calendrier-seatable'
    - '/fr/aide/anleitung-zum-kalender-plugin'
    - '/fr/aide/creer-calendriers-multiples-base-seatable'
    - '/fr/aide/mehrere-kalender-fuer-eine-base-anlegen'
    - '/fr/aide/ajouter-evenements-plugin-calendrier-seatable'
    - '/fr/aide/neue-kalendereintraege-im-kalender-plugin-anlegen'
seo:
    title: 'Vue de Calendrier dans SeaTable – Utiliser la vue chronologique'
    description: "La vue Calendrier de SeaTable affiche vos rendez-vous par année, mois, semaine, jour ou dans l'agenda. Configuration complète et conseils."
weight: 13
---

La vue de calendrier affiche les données d'un tableau sous forme de **calendrier**. Vous pouvez obtenir une vue d'ensemble de **différentes périodes (année, mois, semaine, jour)** ou afficher des rendez-vous sous forme de **agenda** sous forme de liste.

Un exemple est la vue d'ensemble mensuelle dans un calendrier de vacances :

![La vue du calendrier](images/calendar-view.jpg)

{{< warning type="warning" headline="Conditions" >}}

Pour que la vue de calendrier soit utile, vous devez avoir au moins une [colonne de date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) dans votre tableau.

{{< /warning >}}

## Pour créer une vue de calendrier

![Créer une vue de calendrier](images/create-calendar-view.jpg)

1. Cliquez sur le **nom de la vue actuelle**.
2. Cliquez sur **Ajouter une vue ou un dossier** et sélectionnez le **type de vue** souhaité.

![nommer une vue de calendrier](images/name-calendar-view.jpg)

3. Donnez un **nom** à la nouvelle vue.
4. Activez le curseur si vous souhaitez que la nouvelle vue ne soit pas visible par tous, mais **privée**.
5. Confirmez en cliquant sur **Envoyer**.

![créer une vue de calendrier](images/calendar-view-settings.jpg)

6. Dans le champ **Titre**, indiquez la colonne avec laquelle vous souhaitez étiqueter les entrées du calendrier.
7. Indiquez quelle colonne de date doit être utilisée pour la **date de début**. La vue du calendrier est ensuite générée automatiquement.
8. Vous pouvez également indiquer une colonne de date ou de durée pour la **date de fin**, qui définit la période des entrées de calendrier.
9. Enfin, vous pouvez choisir le jour de la semaine qui servira de **premier jour de la semaine**.

Si vous souhaitez faire des modifications ultérieures, cliquez sur **l'icône de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} dans le coin supérieur droit et ajustez les **paramètres**.

## Options de vue

Vous pouvez utiliser les options suivantes dans une vue de calendrier :
- [Verrouiller la vue]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) 
- [Couleur de la ligne]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Partager la vue]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Imprimer la vue]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Les options d'affichage en détail

Il existe au total 5 options d'affichage : Vous pouvez afficher les rendez-vous dans un calendrier par **an**, **mois** ou **semaine**, dans un **planificateur journalier** ou comme **agenda** sous forme de liste.

Vous pouvez facilement passer d'une des cinq options d'affichage du calendrier à l'autre. Pour cela, il vous suffit de cliquer sur l'option correspondante dans le **bouton** situé au-dessus du calendrier.

![options d'affichage du calendrier](images/display-options-calendar-view.png)

### Aperçu de l'année

Ici, vous pouvez voir l'**année** en un coup d'œil. Le **point** sous une date vous indique qu'il existe une entrée à cette date. De plus, vous avez la possibilité d'afficher les **détails de la ligne** en cliquant sur la date.

![Vue d'ensemble de l'année dans le calendrier](images/year-overview-calendar-view.png)

### Aperçu mensuel

Dans cette représentation, vous avez un aperçu de tous les jours d'un **mois**. Ici aussi, vous pouvez accéder aux **détails de la ligne** en cliquant sur l'une des entrées du calendrier.

### Aperçu hebdomadaire

Cette représentation vous montre sur l'axe vertical les **heures** et de gauche à droite les sept jours d'une **semaine**. Ici aussi, vous pouvez ouvrir les **détails de la ligne** en cliquant sur l'une des dates.

### Planificateur journalier

L'aperçu journalier est particulièrement utile si vous souhaitez avoir plusieurs rendez-vous sur une **journée**. Tout comme la vue d'ensemble hebdomadaire, il affiche les **heures** sur l'axe vertical. Ici aussi, vous pouvez ouvrir les **détails de la ligne** en cliquant sur l'un des rendez-vous.

### Affichage de l'agenda

L'**Agenda** liste tous les rendez-vous d'un **mois** et vous permet de voir certaines **informations** sur les rendez-vous en un coup d'œil.

Pour ce faire, il vous suffit d'afficher les **colonnes** souhaitées du tableau dans les **paramètres** de la vue – par exemple le sujet, le statut et le type de publication.

![Agenda dans la vue Calendrier](images/calendar-view-agenda.jpg)

## Ajouter un nouvel enregistrement dans la vue de calendrier

Pour ajouter **de nouveaux enregistrements** dans la vue de calendrier, vous avez plusieurs possibilités.

### 1. Via le grand symbole plus

![ajouter un nouvel enregistrement dans la vue du calendrier](images/add-new-record-in-calendar-view.jpg)

Cliquez sur le **cercle orange avec le symbole plus** dans le coin inférieur droit. Une nouvelle fenêtre s'ouvre. Créez un nouvel enregistrement dans les **détails de la ligne** et saisissez les données souhaitées. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.

{{< warning type="warning" headline="Note" text="Cette fonction existe pour **toutes** les options d'affichage du calendrier" />}}

### 2. À propos d'un champ de calendrier

![créer une nouvelle entrée de calendrier dans la vue Calendrier](images/add-record-in-monthly-calendar-view.jpg)

Placez le curseur de la souris sur un **champ** du calendrier et cliquez sur l'icône **Plus** qui apparaît dans le coin supérieur droit. Créez un nouvel enregistrement dans les **détails de la ligne** et saisissez les données souhaitées. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.

{{< warning type="warning" headline="Note" text="Cette fonction n'existe que pour les options d'affichage **mois** et **semaine**" />}}

### 3. En double-cliquant

Si vous faites un **double clic** sur une position dans le calendrier, les **détails de la ligne** s'ouvrent également. Sinon, vous créez l'entrée de la même manière que pour les autres options.

{{< warning type="warning" headline="Note" text="Le double-clic ne fonctionne que pour les options d'affichage **mois**, **semaine** et **jour**" />}}

### 4. Dérouler les dates

Pour cette fonction, vous avez besoin de **deux colonnes de dates** qui peuvent saisir des **heures**.

1. Créez deux colonnes de dates pour les **heures de début et de fin**, en activant à chaque fois l'option **à la minute près**.
2. Ouvrez la vue **Calendrier** et sélectionnez l'affichage **Semaine ou Jour**.
3. Dans les **paramètres** (accessibles via l'icône en forme de roue dentée {{< seatable-icon icon="dtable-icon-set-up" >}}), sélectionnez les deux colonnes de date pour le calendrier.
4. Dans le calendrier, cliquez sur l'heure à laquelle vous souhaitez que le rendez-vous commence, maintenez le **bouton gauche de la souris** enfoncé et faites glisser la boîte jusqu'à l'heure à laquelle vous souhaitez que le rendez-vous se termine.

![dérouler les rendez-vous dans la vue hebdomadaire et quotidienne](images/add-record-in-weekly-calendar-view.gif)

{{< warning type="warning" headline="Remarque" text="Vous ne pouvez dérouler les rendez-vous que dans le **calendrier hebdomadaire ou journalier**" />}}

## Déplacer les rendez-vous par glisser-déposer

Vous pouvez facilement **déplacer les entrées dans l'affichage du calendrier par glisser-déposer**. Cela modifie automatiquement les valeurs correspondantes dans les colonnes de dates de votre tableau. Cette fonction est disponible pour les vues **mensuelles**, **hebdomadaires** et **journalières**.

![déplacer des entrées de calendrier](images/move-record-in-weekly-calendar-view.gif)
