---
title: 'La première base'
date: 2022-08-25
lastmod: '2023-05-15'
categories:
    - 'kurzanleitungen'
author: 'cdb'
url: '/fr/aide/creer-premiere-base-seatable'
aliases:
    - '/fr/aide/die-erste-base'
seo:
    title: 'Créer votre première base SeaTable: guide complet'
    description: 'Découvrez comment créer et organiser une base SeaTable : tableaux, colonnes et relations pour une gestion des données plus efficace.'
---

Dans SeaTable, vous organisez vos données dans des [bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). Une base est un conteneur pour une ou plusieurs tableaux. Les tableaux d'une base peuvent être juxtaposés indépendamment les uns des autres ou, comme dans une base de données, reliés entre eux par des relations.

Vous pouvez également [partager]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) avec d'autres membres de l'équipe ou [inviter]({{< relref "help/startseite/freigaben/unterschiede-zwischen-einladungs-links-und-externen-links" >}}) des tiers externes à y travailler ensemble.

SeaTable gère un [historique]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) en arrière-plan pour chaque base, ce qui vous permet d'annuler les modifications et de rétablir les états précédents si nécessaire.

## La page d'accueil

Après vous être connecté, vous vous trouvez sur la **page d'accueil**. C'est ici que vous gérez vos bases. Si vous avez choisi [des templates]({{< relref "templates" >}}) lors de l'inscription, ils seront affichés ici.

En cliquant sur l'**image de l'avatar** dans le coin supérieur droit, vous pouvez accéder aux [paramètres personnels]({{< relref "help/startseite/persoenliche-einstellungen" >}}), par exemple pour adapter la langue du système.

En cliquant sur **Ajouter une** base, vous créez votre première base personnelle. Donnez-lui un **nom**, appuyez sur **Entrée** et la base sera placée sur la page d'accueil. Si vous déplacez le curseur de la souris sur le nom de la base, un **symbole de crayon** {{< seatable-icon icon="dtable-icon-rename" >}} et le symbole à trois points {{< seatable-icon icon="dtable-icon-more-vertical" >}} apparaissent à droite pour les fonctions avancées.

L'icône en forme de crayon permet de renommer la base et de lui attribuer une autre icône et une autre couleur. Les fonctions avancées comprennent par exemple le [partage]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) d'une base ou son [exportation]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}). Vous ouvrez la base en cliquant sur son nom.

## Vue du tableau

La nouvelle base contient dès le départ un [tableau]({{< relref "help/erste-schritte/einfuehrung-funktionen/einfuehrung-in-die-arbeit-mit-bases-und-tabellen" >}}). La vue Tableau est la vue centrale, mais pas la seule, de SeaTable. Dans la vue Tableau, vous gérez les tableaux de la base, définissez leur structure en colonnes et saisissez ou analysez vos données.

SeaTable propose [plus de 20 types de colonnes]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) au total. Vous connaissez certainement déjà les colonnes de texte, de chiffres et de dates des tableurs traditionnels. Bien sûr, SeaTable les connaît aussi. En outre, SeaTable propose des colonnes pour les images et les fichiers, des boutons et des cases à cocher, ainsi que des sélections uniques et multiples.

Vous voulez ajouter des images à une entrée ? Faites simplement glisser l'image dans une colonne d'images et SeaTable l'enregistrera directement dans le tableau. Dans SeaTable, vous avez toutes vos données au même endroit !

Un autre type de colonne que vous ne connaissez pas dans un tableur est la [liaison à d'autres entrées]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Les liens permettent de créer des relations entre les lignes de différents tableaux. Cette procédure, qui correspond au mode de fonctionnement des bases de données relationnelles, permet d'éviter les saisies en double, d'assurer la cohérence des données et de créer une vue d'ensemble.

Voici un exemple d'application : une gérance immobilière saisit dans un tableau les objets gérés et les relie aux locataires qui sont gérés dans un autre tableau. Si les propriétés de l'objet changent, le gestionnaire doit uniquement modifier l'adaptation dans le tableau des objets. Grâce à la liaison, les informations modifiées sont automatiquement mises à jour pour tous les locataires affectés.

[Vous créez d'autres tableaux à l'aide des onglets]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}). Chaque tableau a une mise en page individuelle : aménagez les colonnes selon vos propres souhaits et besoins.
