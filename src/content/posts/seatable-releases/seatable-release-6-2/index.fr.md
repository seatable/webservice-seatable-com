---
title: 'SeaTable 6.2 : Quand le code rencontre le No-code'
description: "SeaTable 6.2 introduit un type de page HTML extrêmement flexible et enrichit l'App Builder. Les colonnes de formule et les liens externes bénéficient eux aussi de nouvelles fonctionnalités."
date: 2026-07-13
author: 'rdb'
url: '/fr/seatable-release-6-2'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.2 : Quand le code rencontre le No-code'
    description: "SeaTable 6.2 : nouveau type de page HTML et autres améliorations dans l'App Builder, ainsi que de nouvelles fonctionnalités pour les colonnes de formule et les liens externes."
register:
    show: true
draft: true
---

L'[App Builder]({{< relref "help/app-builder" >}}) de SeaTable accueille un nouveau type de page : les **pages HTML** permettent de créer des pages entièrement personnalisées à partir de HTML, JavaScript et CSS. En matière de visualisation des données, quasiment toutes les limites disparaissent. Les formulaires web peuvent eux aussi être conçus exactement selon vos besoins, et même les interactions les plus complexes se réalisent sans difficulté. « Impossible » n'existe plus !

Mais ce n'est pas la seule nouveauté de l'App Builder dans la version 6.2. Le type de page [Enregistrement unique]({{< relref "help/app-builder/seitentypen-in-universellen-apps/seiten-vom-typ-einzelner-datensatz-in-universellen-apps" >}}) bénéficie de trois améliorations : toutes les valeurs de colonnes peuvent désormais être affichées de manière uniforme sous forme de texte, formatées de façon universelle et — une demande fréquente — modifiées directement sur la page. [Les autres types de pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) profitent d'une gestion des autorisations étendue pour les colonnes de liens. Par ailleurs, quelques ajustements de design apportent plus de clarté : les applications sans page sont désormais identifiées comme telles afin d'éviter tout malentendu, et l'avatar ainsi que les notifications d'application ont trouvé une nouvelle place.

Avec SeaTable 6.2, deux nouvelles fonctionnalités font leur apparition parmi les [formules]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) : la nouvelle fonction **datetimeFormat()** convertit les valeurs de date en chaînes de caractères selon un format librement définissable. Si le format de date que vous préférez n'était jusqu'à présent pas proposé par SeaTable, c'est désormais de l'histoire ancienne. En outre, les formules qui renvoient une chaîne de caractères prennent maintenant en charge les **retours à la ligne**, ce qui permet de composer des textes à partir de différentes colonnes avec beaucoup plus de souplesse.

Enfin, cette nouvelle version améliore la collaboration : les [liens externes]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}}) et les [liens d'invitation]({{< relref "help/startseite/freigaben/einladungs-link-erklaert" >}}) peuvent désormais être accompagnés d'une description, ce qui permet de noter directement sur le lien son objectif et ses destinataires prévus. Par ailleurs, la barre de menu des bases et des vues ouvertes via un lien externe a été retravaillée et rendue plus claire.

Le [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/) recense — comme d'habitude — toutes les modifications importantes.

La version 6.2 de [SeaTable Server]({{< relref "pages/product/seatable-server" >}}) est disponible au téléchargement dès aujourd'hui dans le [dépôt Docker de SeaTable](https://hub.docker.com/r/seatable/seatable-enterprise).

La mise à jour de [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) aura lieu dans une semaine, **le 22 juillet**. Avec cette mise à jour, le quota mensuel pour l'[exécution des scripts Python]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}) devient dynamique. À l'instar des appels d'API ou des automatisations, le quota global pour les scripts Python est lié à la taille d'une équipe. Une équipe Plus reçoit 1 000 exécutions de scripts Python, une équipe Enterprise 5 000 exécutions Python par utilisateur et par mois. Pour l'abonnement Free, une limite forfaitaire de 100 exécutions par mois continue de s'appliquer.

## Un nouveau type de page pour les Apps : les pages HTML

L'**App Builder de SeaTable** permet de créer des applications performantes — sans aucune programmation. Grâce aux types de pages prédéfinis, une application web pleinement fonctionnelle peut voir le jour en peu de temps. Cette efficacité a toutefois un prix : les **10 types de pages** offrent certes de nombreuses possibilités de configuration, mais ils imposent la structure et le comportement d'une page. Les mises en page et/ou les interactions sortant de ce cadre prédéfini n'étaient jusqu'à présent pas possibles.

Vous souhaitez utiliser un type de diagramme que SeaTable ne prend pas en charge ? Créer un formulaire web hautement personnalisé ? Intégrer un schéma interactif comportant des éléments cliquables ? Ou combiner plusieurs représentations — par exemple un tableau et un enregistrement unique — sur une même page ? Le nouveau **type de page HTML** permet de répondre à ces besoins et à bien d'autres encore.

\[IMAGE]

Les pages HTML peuvent afficher des **contenus statiques**, mais elles révèlent tout leur potentiel en lien avec les **données d'une base**. Vous pouvez récupérer des données d'une base et modifier des enregistrements, tout comme les autres types de pages de l'App Builder. En ce qui concerne le **design de l'interface utilisateur**, vous êtes en revanche presque entièrement libre. Tout ce qui peut être réalisé avec HTML, CSS et JavaScript peut en principe l'être également sous forme de page HTML dans l'App Builder.

Ne vous laissez pas tromper par le nom : les pages HTML ne prennent pas seulement en charge le **HTML**, mais aussi le **JavaScript et le CSS**. L'ensemble du code de la page est chargé dans l'application sous forme de bundle. Vous trouverez le fonctionnement, les approches de développement possibles ainsi que la référence du kit de développement logiciel (SDK) associé dans la [Documentation Développeur SeaTable](https://developer.seatable.com/html-pages/ "SeaTable Developer Manual"). Vous y trouverez également un exemple de page.

Actuellement, les pages HTML s'adressent en particulier **aux utilisateurs ayant une expérience de la programmation**. Une fonctionnalité IA est cependant déjà en développement : elle permettra de créer des pages HTML en langage naturel et sans connaissances en programmation.

## Plusieurs améliorations pour le type de page Enregistrement unique

Celui-ci bénéficie en effet de plusieurs améliorations dans cette nouvelle version. Jusqu'à présent, les enregistrements ne pouvaient être modifiés que via les détails de la ligne, qui devaient d'abord être ouverts à l'aide du bouton « Modifier l'entrée ». Cela impliquait des clics supplémentaires et une rupture inutile dans le flux de modification.

Avec SeaTable 6.2, cette étape intermédiaire appartient au passé. Si un utilisateur dispose des droits de modification nécessaires, les champs peuvent désormais être modifiés directement sur la page. **Un clic sur un champ active le mode de modification**, les saisies sont validées comme d'habitude et les modifications sont enregistrées immédiatement. Cela garantit un flux de travail nettement plus fluide et plus intuitif.

L'affichage a lui aussi été enrichi. Les **colonnes** disposant d'une représentation visuelle propre — par exemple les [colonnes de sélection]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou de [collaborateurs]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) — peuvent désormais, en option, être affichées sous forme de texte simple. Pour toutes les valeurs affichées sous forme de texte, un ensemble uniforme d'**options de mise en forme** est en outre disponible. La taille et la couleur de la police, l'alignement et l'arrière-plan peuvent être ajustés de manière cohérente, indépendamment du type de colonne d'origine. Il est ainsi possible de concevoir des pages à l'apparence uniforme et soignée.

\[IMAGE]

## Des autorisations étendues pour les liens dans l'application

La version 6.2 comble une lacune dans la gestion des autorisations des [colonnes de liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) au sein de l'App Builder. La nouvelle autorisation **« Supprimer les entrées existantes »** permet de déterminer précisément si les utilisateurs sont autorisés à supprimer des liens existants.

Jusqu'à présent, tout utilisateur disposant d'une autorisation de modification pouvait supprimer les liens existants. Ce comportement peut désormais être contrôlé indépendamment des autres [autorisations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) de la colonne de liens.

\[IMAGE]

Les droits d'accès aux colonnes de liens peuvent ainsi être gérés de façon complète : selon la configuration, les utilisateurs peuvent créer, modifier et/ou supprimer des liens — chacune de ces actions étant régie par sa propre autorisation. Cela permet **un contrôle nettement plus précis des droits de modification dans les applications**.

## Deux nouvelles fonctionnalités dans la colonne de formule

La nouvelle fonction **datetimeFormat()** vous aide à afficher les valeurs de date exactement comme vous en avez besoin. Le premier paramètre contient la date à formater ou la référence à la colonne qui contient la valeur. Dans le second paramètre, vous définissez le format cible.

![](https://file.seatable.com/lib/36bf10a0-17b4-4f96-a428-603ca6ddebd1/file/images/auto-upload/image-1783721478269.png?raw=1)

Dans les formules qui renvoient des chaînes de caractères, vous pouvez désormais insérer un **retour à la ligne** avec « \n » ou '\n'. Cela est particulièrement utile lorsque vous concaténez plusieurs colonnes mais que vous ne souhaitez pas écrire les valeurs sur la même ligne. L'exemple type est celui d'une adresse (voir ci-dessous).

![](https://file.seatable.com/lib/36bf10a0-17b4-4f96-a428-603ca6ddebd1/file/images/auto-upload/image-1783721727898.png?raw=1)

## Améliorations des liens externes et des liens d'invitation

Enfin, SeaTable 6.2 apporte une optimisation pour les **liens externes et les liens d'invitation**. Vous pouvez désormais les accompagner d'une **description**, ce qui permet par exemple de noter directement sur le lien son objectif et ses destinataires prévus. Par ailleurs, nous avons retravaillé et rendu plus claire la barre de menu des bases et des vues ouvertes via un lien externe.

## Et bien plus encore

* **Journal de la base amélioré :** le [journal de la base]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}) a été retravaillé à plusieurs endroits. Des champs de recherche facilitent la sélection dans les bases volumineuses, les menus déroulants adoptent un design uniforme et il est désormais possible de filtrer les actions effectuées dans des tableaux supprimés.

* **Widget de date amélioré :** le widget de date a été optimisé en matière d'utilisation et d'affichage, pour une manipulation encore plus confortable des [valeurs de date et d'heure]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}).

* **Emojis dans les commentaires :** les [commentaires]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) prennent désormais en charge les emojis. Cela rend les retours, les réactions et la collaboration encore plus expressifs.
