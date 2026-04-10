---
title: 'Pages de tableau dans les applications de SeaTable'
date: 2023-12-01
lastmod: '2025-07-04'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-tableau-apps-seatable'
aliases:
    - '/fr/aide/tabellenseiten-in-universellen-apps'
    - '/fr/aide/pages-tableau-apps-universelles'
seo:
    title: 'Pages de tableau dans les applications de SeaTable'
    description: 'Ajoutez des tableaux comme pages dans une application, réglez filtres, tris, groupes et visibilité des colonnes. Gérez les droits, exportez vers Excel, tout est possible.'
weight: 2
---

Ce type de page vous permet d'[ajouter]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) n'importe quel **tableau** de votre base comme page à votre application.

![Table page dans l'application](images/Table-page-in-Universal-App.png)

## Modifier les paramètres de la page

Si vous souhaitez modifier les paramètres d'une page, cliquez dans la navigation sur le **symbole de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondant.

![Ouvrir les paramètres de la page](images/page-permissions-universal-app.png)

Lorsque vous modifiez des pages de tableau, vous pouvez définir de nombreux **paramètres de page** afin d'adapter exactement les données affichées du tableau sous-jacent à un groupe d'utilisateurs.

![Paramètres de page sur les pages de tableaux](images/Page-settings-on-table-pages.png)

## Filtres, tris et groupes prédéfinis

Vous pouvez définir des **filtres**, des **tris** et des **groupes** **prédéfinis** dans les paramètres de la page afin de limiter et d'organiser les données affichées pour un groupe d'utilisateurs.

![Ajouter un filtre sur la page du tableau dans les applications](images/Add-filter-on-table-page-in-Universal-Apps.png)

Pour ce faire, cliquez sur **Ajouter un filtre**, **Ajouter un tri** ou **Ajouter un groupe**, sélectionnez la **colonne** et la **condition** souhaitées et confirmez en cliquant sur **Envoyer**.

{{< warning  headline="Remarque importante"  text="Les utilisateurs de l'application ne peuvent **pas modifier** les **filtres prédéfinis**. Ils n'obtiennent donc, comme ils le souhaitent, que les données filtrées. En revanche, les tris et les regroupements prédéfinis ne définissent qu'un **affichage standard** que les utilisateurs peuvent modifier individuellement." />}}

![Vue par défaut regroupée par une colonne sur une page de tableau dans les applications](images/Default-view-grouped-by-one-column-on-a-table-page-in-Universal-Apps.png)

{{< warning  headline="Filtrer par colonnes de chiffres ou de durée"  text="Si vous souhaitez filtrer par colonnes de chiffres ou de durées, il y a certaines consignes de format à respecter. Vous devez écrire **les nombres décimaux** avec un point comme séparateur, indiquer **les pourcentages** sous forme de nombres décimaux (p. ex. 99% = 0,99) et convertir la **durée** en secondes (p. ex. 1 heure = 3600 secondes)." />}}

## Colonnes masquées et en lecture seule

En plus des filtres prédéfinis, vous pouvez également définir des **colonnes masquées et en lecture seule** afin de limiter davantage la visibilité et la modifiabilité de certaines données.

![Colonnes cachées prédéfinies dans l'App Builder](images/Preset-hidden-columns-in-Universal-App-Builder.png)

Il suffit de cliquer sur les **curseurs** ou les **cases** des colonnes qui doivent être **masquées** ou **uniquement lisibles** par les utilisateurs.

![Colonnes en lecture seule sur les pages de tableaux dans les applications](images/Read-only-columns-on-table-pages-in-Universal-Apps.png)

Vous reconnaissez les colonnes en lecture seule au fait qu'elles sont **grisées** dans le tableau et marquées par un **symbole de cadenas**.

{{< warning  headline="Pas d'héritage des paramètres de vue de la base"  text="Veuillez noter que **les colonnes masquées et bloquées** dans le tableau sous-jacent n'ont **aucun** effet sur l'app. Lorsque vous créez une nouvelle page de tableau dans l'app, toutes les colonnes sont d'abord affichées et peuvent être modifiées." />}}

## Options d'affichage de l'utilisateur

Les **options d'affichage** au-dessus du tableau permettent aux utilisateurs de l'application de définir leurs propres paramètres complémentaires, qui fonctionnent exactement comme dans la base. Il s'agit notamment de

- [Filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})
- [Trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Grouper]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Masquer des colonnes]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Sélectionner l'hauteur de ligne]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Ajuster le nombre de colonnes fixes]({{< relref "help/base-editor/spalten/anzahl-der-fixierten-spalten-anpassen" >}})

![User view options on table pages in apps](images/user-view-options-on-table-pages-in-apps.png)

Comme indiqué ci-dessus, les paramètres d'affichage individuels de l'utilisateur **n'ont aucun effet sur les paramètres par défaut** de la page de tableau que vous avez prédéfinis. Par exemple, l'utilisateur peut filtrer davantage une vue que vous avez pré-filtrée ou masquer d'autres colonnes, mais il ne peut pas afficher les enregistrements que vous avez filtrés ou les colonnes que vous avez masquées, ni même les rendre visibles pour les autres.

## Paramètres de la colonne des liens

Dans les **paramètres de la colonne des liens**, vous pouvez définir pour chaque tableau lié quelles données sont visibles et quelles opérations sont autorisées.

![Paramètres de colonne de lien sur les pages de tableau dans les applications](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Paramètres des champs** : Ici, vous pouvez définir précisément les colonnes auxquelles s'appliquent les autorisations suivantes.
- **Créer et lier de nouvelles entrées** : Si vous activez ce curseur, les utilisateurs peuvent ajouter de nouvelles entrées dans le tableau lié. Les paramètres de champ vous permettent de définir quelles colonnes sont **nécessaires**, c'est-à-dire qu'elles doivent être remplies.
- **Lier des entrées existantes** : Si vous activez ce curseur, les utilisateurs peuvent lier les entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **visibles** dans les paramètres de champ.
- **Filtres prédéfinis** : Si vous ajoutez un filtre ici, seules les options qui remplissent les conditions du filtre seront affichées lors de la liaison d'entrées.
- **Activer la fonction Big Data** : Lorsque la fonction Big Data est activée, les utilisateurs peuvent effectuer des recherches sur plus de 20 000 enregistrements, à condition qu'il y ait autant d'entrées dans le tableau lié.
- **Limiter les liens à une seule ligne maximum** : Si vous activez ce curseur, les utilisateurs ne pourront lier qu'une seule ligne du tableau lié à la fois dans les cellules de la colonne de jointure.
- **Modifier les entrées liées** : Si vous activez ce curseur, les utilisateurs peuvent modifier les entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **éditables** dans les paramètres de champ.

## Empêcher l'ajout de doublons

Sur les pages de tableaux permettant à différents utilisateurs d'effectuer de nouvelles entrées dans une base, il est vite arrivé que **des lignes identiques** soient créées. Vous pouvez empêcher cela en empêchant l'ajout de doublons. Pour ce faire, activez le **curseur** correspondant et sélectionnez les **colonnes** dans lesquelles les valeurs doivent correspondre pour qu'une ligne soit considérée comme **un doublon**. Si l'ajout d'une ligne est bloqué, un message d'erreur correspondant apparaît.

![Empêcher l'ajout de doublons dans les applications](images/Prevent-adding-duplicate-records-in-Universal-Apps.gif)

## Contrôle du format pour les nouvelles entrées

Vous pouvez activer un autre **curseur** pour [valider les entrées dans les colonnes de texte]({{< relref "help/base-editor/spaltentypen/validierung-der-eingabe-bei-textfeldern" >}}). Dès que la **vérification du format** est activée, les détails de la ligne s'ouvrent toujours lorsque quelqu'un veut ajouter une nouvelle entrée sur la page du tableau - et cela n'est possible que si les entrées correspondent au format défini. Pour les entrées dont le format est différent, un **message d'erreur** apparaît.

![Vérification du format sur la page du tableau](images/Format-check-on-table-page.png)

Vous pouvez par exemple minimiser **les erreurs de frappe** sur des chaînes de caractères clairement définies, comme les codes postaux ou les numéros de compte. Vous définissez les [expressions régulières]({{< relref "help/base-editor/spaltentypen/validierung-der-eingabe-bei-textfeldern" >}}) pour valider les entrées dès la création d'une colonne de texte dans la base.

## Afficher le formatage des cellules

Si vous utilisez la [colorisation des cellules]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}) dans le tableau sous-jacent, vous pouvez activer d'un clic l'option permettant d'afficher le formatage des cellules également sur la page du tableau.

![Afficher la couleur des cellules sur les pages de tableaux dans les applications](images/Show-cell-coloring-on-table-pages-in-Universal-Apps.gif)

## Exporter la page du tableau en tant que fichier Excel

Cette fonction est désactivée par défaut. Si vous souhaitez permettre l'exportation vers Excel, activez le curseur correspondant dans les paramètres de la page du tableau. Ensuite, tous les utilisateurs de l'app qui ont accès à la page du tableau peuvent exporter les données visibles sous forme de fichier Excel. Pour ce faire, cliquez sur les **trois points** dans les options d'affichage, puis sur **Exporter vers Excel**.

![Activer l'exportation Excel d'une page de tableau](images/Enable-Excel-export-of-a-table-page.png)

Les données exportées depuis la page du tableau sont indépendantes de l'**affichage** actuel. Même si vous **filtrez ou masquez des colonnes**, toutes les données sont incluses dans l'exportation.

## Autorisations des pages

Dans les [autorisations de page]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}), vous pouvez définir avec précision qui peut voir et modifier le tableau.

{{< warning  headline="Attention aux boutons" >}}

[Les boutons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) peuvent **toujours** être actionnés indépendamment des autorisations de la page. Cela permet à tout utilisateur de l'application d'effectuer certaines modifications sur les enregistrements que vous avez définis au préalable, même si les colonnes concernées sont par ailleurs bloquées pour lui ou si l'utilisateur n'est pas autorisé à modifier la page.

{{< /warning >}}

![Définition des autorisations des pages](images/page-permissions.png)
