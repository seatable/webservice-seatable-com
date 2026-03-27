---
title: 'Généralités sur les bases dans SeaTable'
date: 2022-08-25
lastmod: '2023-05-03'
categories:
    - 'arbeiten-mit-bases'
author: 'cdb'
url: '/fr/aide/bases-fonctions-gestion-seatable'
aliases:
    - '/fr/aide/bases'
seo:
    title: 'Bases SeaTable : fonctions, gestion et partage expliqués'
    description: 'Découvrez tout sur les bases dans SeaTable : gestion, création, partage, export, suppression, restauration et utilisation efficace.'
star: true
weight: 1
---

Les bases sont essentielles dans SeaTable. Chaque fois que vous saisissez, analysez, modifiez ou partagez des données dans SeaTable, vous vous trouvez dans une base.

À première vue, une base n'est qu'un **conteneur** pour un ou plusieurs **tableaux**. De ce point de vue, il est logique de comparer une base à un classeur dans Excel. Mais cette comparaison ne rend pas justice à une base. Les bases de SeaTable sont bien supérieures aux classeurs traditionnels :

- Fonctions de [base de données relationnelle]({{< relref "posts/relationale-datenbank" >}}) et [liens entre les tableaux]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- [Plus de 20 types de colonnes]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) couvrant tous les formats de données courants
- Diverses [possibilités de partage]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) pour faciliter le partage des données
- [Collaboration]({{< relref "help/erste-schritte/einfuehrung-funktionen/zusammenarbeit" >}}) en temps réel avec d'autres utilisateurs et transmission en temps réel de toutes les modifications
- Une [fonction de commentaire]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) pour chaque enregistrement sur une ligne
- [Versionnage]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) de toutes les modifications
- un [éditeur de formulaires web]({{< relref "help/base-editor/webformulare/webformulare" >}}) intégré et [des plugins]({{< relref "help/base-editor/ansichten" >}}) graphiques
- Possibilités d'intégration simples grâce à l'API REST

Les bases sont donc bien plus que des "conteneurs de tableaux" sur le web. Vous apprécierez très vite ces avantages et ne voudrez plus jamais vous en passer !

## Propriétaire de bases

Chaque base a un (et un seul) **propriétaire**. Il est toutefois possible de transférer la propriété d'une Base d'un utilisateur à un autre utilisateur.

Le propriétaire d'une base est soit un **utilisateur**, soit un **groupe**. Si un utilisateur est le propriétaire d'une base, il est le seul à en avoir les pleins pouvoirs. Si la base appartient à un groupe, tous les administrateurs du groupe ont un accès complet à la base. Vous trouverez ici plus d'informations sur les [autorisations des différents membres du groupe]({{< relref "help/startseite/gruppen/gruppenmitglieder-und-ihre-berechtigungen" >}}).

Le transfert direct de la propriété d'un utilisateur à un autre utilisateur n'est actuellement pas possible (état : 20.3.2023). Vous pouvez cependant effectuer un **changement de propriétaire** de manière indirecte, en exportant une base et en la faisant importer par le nouveau propriétaire. Vous trouverez plus d'informations sur l'importation et l'exportation de bases dans l'article [Importation et exportation de données]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Création de bases

Vous créez **de nouvelles bases** à partir de la page d'accueil. Vous vous trouvez toujours sur cette page lorsque vous vous connectez à SeaTable. Si vous êtes en train de travailler dans une base, vous pouvez revenir à la page d'accueil en cliquant sur l'**icône de la base** {{< seatable-icon icon="dtable-icon-dtable-logo" >}} en haut à gauche.

Dans la section **Mes bases** et dans chaque **groupe** dont vous êtes l'administrateur, vous trouverez le bouton **Ajouter une base ou un dossier**. En cliquant sur ce bouton, vous créez une nouvelle base là où vous le souhaitez.

Lors de la création d'une nouvelle base, vous avez **trois options**. Pour en savoir plus, consultez les articles correspondants :

- [Créer une base vide]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Importer une base à partir d'un fichier]({{< relref "help/startseite/import-von-daten/welche-import-formate-unterstuetzt-seatable" >}})
- [Créer une base à partir d'un modèle]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})

## Gestion des bases

Vous gérez les bases via le **menu contextuel** de la page d'accueil. Si vous déplacez le curseur de la souris sur une de vos bases, une **icône en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}} et une **icône à trois points** {{< seatable-icon icon="dtable-icon-more-vertical" >}} apparaissent à droite du nom pour les options avancées. Vous aurez régulièrement besoin de ces dernières pour la gestion de vos bases.

Vous ne pouvez **pas gérer** les bases que vous avez partagées. Dans les fonctions avancées de ces bases, vous ne disposez que de deux options : **Quitter la base partagée** et **Copier**.

## Renommer les bases

Vous pouvez **renommer** ultérieurement les bases dont vous êtes le propriétaire ou l'administrateur. Placez le curseur de la souris sur le nom de la base à renommer et cliquez ensuite sur l'**icône en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}}. Vous pouvez maintenant modifier le nom et l'enregistrer en cliquant sur la **touche Entrée**. Lisez [ici]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) ce à quoi vous devez faire attention lors du choix du nom.

## Changer l'icône et la couleur d'une base

Vous pouvez donner un nouveau look aux bases dont vous êtes le propriétaire ou l'administrateur. Pour savoir comment faire, [cliquez ici]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}}). Pour apporter un vent de fraîcheur à vos bases, vous disposez de plus de **10 couleurs** et de plus de **25 icônes**.

## Ajouter une description de base

Vous pouvez ajouter une description à vos bases afin de donner un "mode d'emploi" aux autres utilisateurs ou de consigner des informations complémentaires sur une base. Vous apprendrez [ici]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}) comment utiliser cette fonction.

## Libérer les bases

Vous pouvez **partager** des bases dont vous êtes le propriétaire ou l'administrateur avec d'autres **utilisateurs et groupes** et leur donner ainsi accès aux données. Les partages s'effectuent avec différentes autorisations, ce qui vous permet de contrôler à tout moment les modifications apportées à vos bases.

Vous trouverez plus d'informations sur cette fonction importante et extrêmement utile dans l'article Vue d ['ensemble des partages de base et de vue]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}).

## Copier la base

Vous pouvez **copier** toutes les bases auxquelles vous avez accès. Selon l'origine de la base et l'endroit où vous voulez la copier, l'article [Dupliquer une base]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}) vous aideront.

## Déplacer les bases dans des dossiers ou les ajouter aux favoris

Si vous avez accumulé un grand nombre de bases sur votre page d'accueil, il peut être utile, pour plus de clarté, de [regrouper plusieurs bases dans des dossiers]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}}) les bases auxquelles vous accédez le plus souvent.

## Exporter la base

Vous pouvez exporter des bases à des fins de sauvegarde, de transfert à un autre utilisateur ou de transfert vers un autre serveur SeaTable. En principe, l'exportation se fait dans un [fichier DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}).

Vous trouverez plus d'informations sur l'exportation des bases dans l'article [Enregistrer une base en tant que fichier DTABLE]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Supprimer et restaurer des bases

Vous pouvez [supprimer]({{< relref "help/startseite/papierkorb/loeschen-einer-base" >}}) les bases dont vous êtes le propriétaire ou l'administrateur si nécessaire et les [restaurer]({{< relref "help/startseite/papierkorb/eine-geloeschte-base-wiederherstellen" >}}) pendant 30 jours au maximum. Pour ce faire, suivez les instructions des articles liés.

### Restaurer la base à partir d'un snapshot

Vous pouvez afficher et restaurer les snapshots des bases dont vous êtes le propriétaire ou l'administrateur. Pour tout savoir sur les snapshots dans SeaTable, consultez les articles suivants

- [Enregistrer la base actuelle en tant que snapshot]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}})
- [Restauration d'un snapshot]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}})

## Configurer un compte de messagerie dans une base

Si vous souhaitez envoyer des e-mails depuis une base, vous devez connecter votre compte e-mail à la base. Nous vous montrons comment utiliser cette fonction utile dans SeaTable dans l'article [Configuration d'un compte e-mail dans une base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
