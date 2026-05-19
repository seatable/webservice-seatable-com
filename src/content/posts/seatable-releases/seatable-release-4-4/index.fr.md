---
title: 'SeaTable 4.4 : Application universelle, importation Excel & jeux de données communs'
description: 'Actions dans les pages requêtes, drag n drop agenda, poignées de remplissage en colonnes, collaborateurs sur formulaires, dashboards plus riches, titres masquables. Apps galerie et requêtes fusionnent vers l’universel, import plus robuste, datasets synchronisables, valeurs vraiment universelles.'
date: 2024-05-15
lastmod: '2024-05-15'
author: 'kgr'
url: '/fr/seatable-release-4-4'
color: '#96b228'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.4 : apps universelles, Excel et datasets'
    description: 'App universelle enrichie (actions/drag-drop), import Excel optimisé, datasets et valeurs par défaut partout : SeaTable 4.4 simplifie la vie.'
---

Dans SeaTable 4.4, nous poursuivons avec verve le développement de l'Universal App Builder. De nombreuses nouvelles fonctions permettent de créer des applications web encore plus puissantes et confortables. En outre, nous avons peaufiné la fonction d'importation et les jeux de données communs. Les valeurs par défaut pratiques s'appliquent désormais de manière universelle.

Ce matin, nous avons mis à jour SeaTable Cloud à la version 4.4. Tous les auto-hébergeurs peuvent faire de même : L'image de SeaTable 4.4 est disponible en téléchargement dans le célèbre [dépôtDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Comme toujours, vous trouverez dans le [changelog]({{< relref "pages/changelog" >}}) la liste complète des modifications.

## Un App Builder plus flexible et plus puissant

Dans SeaTable 4.4, nous avons à nouveau apporté un grand nombre d'améliorations et de corrections de bugs à l'[application universelle]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}), dont bénéficient presque tous les [types de pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). La fin de la phase bêta approche donc à grands pas.

### Boutons sur les pages d'interrogation

[Les pages de requête]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) prennent désormais en charge l'exécution d'actions à l'aide de boutons : Après une requête de données réussie, il est possible d'actionner [des boutons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) dans la liste de résultats affichée afin d'effectuer des actions. Il s'agit d'une nouveauté particulière, car jusqu'à présent, SeaTable ne permettait nulle part d'interagir avec les lignes interrogées.

![Exécuter des boutons sur des pages de requête](Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Un exemple d'application est une bourse d'emploi interne : la page de requête permet de rechercher rapidement les postes pertinents. Si un poste intéressant y figure, il suffit alors de cliquer sur le bouton dans les résultats de recherche pour postuler directement à l'emploi.

### Glisser-déposer dans le calendrier

Jusqu'à présent, il n'était pas possible de modifier les rendez-vous sur la [page du calendrier]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}). Avec SeaTable 4.4, vous bénéficiez d'une plus grande flexibilité. Désormais, vous pouvez déplacer facilement vos rendez-vous dans le calendrier par glisser-déposer. De plus, vous pouvez modifier les valeurs dans les [colonnes de dates]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) correspondantes via les détails de la ligne, à condition de disposer des [autorisations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) nécessaires.

### Manipulation simplifiée des données côté tableau

Comme dans la base, vous pouvez désormais [sélectionner toutes les entrées d'une colonne]({{< relref "help/base-editor/tabellen/hinzufuegen-von-daten-per-copy-and-paste" >}}) sur les [pages de tableau]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) de vos apps en un seul clic sur l'en-tête de la colonne. La [poignée de remplissage]({{< relref "help/base-editor/zeilen/duplizieren-einer-zeile" >}}) pratique est également désormais possible : faites glisser le petit carré dans le coin inférieur droit d'une cellule vers le bas pour transférer la valeur dans toutes les lignes situées en dessous.

![Marquer les entrées de colonne](Spalteneintraege-markieren-und-Fuellgriff-in-App.gif)

### Colonne des employés disponible sur les pages de formulaires

Si vous utilisez une [colonne d'employés]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) dans votre tableau, elle n'est **pas** disponible dans [les formulaires web]({{< relref "help/base-editor/webformulare" >}}). Cependant, à partir de SeaTable 4.4, vous pouvez ajouter des colonnes d'employés sur les [pages de formulaires]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) de l'application universelle. Ainsi, les membres de votre équipe peuvent par exemple se sélectionner eux-mêmes lors d'une demande de congé et ne doivent plus saisir leur nom manuellement. Auparavant, vous devez activer dans les [paramètres de l'application]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}) l'option permettant d'afficher la liste des collaborateurs.

### Plus d'options de customisation pour des pages personnalisées

Dans la version 4.4, il est possible de masquer la **barre de titre** sur la [page individuelle]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}). Cela permet de créer des pages de renvoi visuellement attrayantes. Pour les éléments image et carte, des menus déroulants permettent de **créer** rapidement **des liens** à partir d'autres pages de l'application. Pour les **statistiques**, nous avons ajouté d'autres types de graphiques et ajouté des possibilités de configuration supplémentaires qui rendent la création de tableaux de bord encore plus confortable. Afin de présenter clairement les nombreuses options de style, nous avons divisé le style du graphique et le style général en deux onglets différents.

## Applications de galerie et de consultation de données

Comme nous l'avons annoncé dans les dernières notes de version, nous avons **supprimé** le **Générateur d'applications de galerie** dans SeaTable 4.4. Si vous souhaitez créer une nouvelle application avec une [galerie]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}), vous disposez d'une alternative plus fonctionnelle avec l'Universal App Builder.

{{< warning headline="Bon à savoir" text="**Les applications de galerie existantes continuent de fonctionner**. Nous recommandons toutefois de passer les applications de galerie existantes aux applications universelles afin de profiter des développements et des améliorations." />}}

![Créer un dialogue d'application](Create-app-dialog-.png)

L'[application de consultation des données]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) a également connu quelques changements. L'ancien App Builder pour la consultation des données a été supprimé et remplacé par un nouveau basé sur l'Universal App Builder. Cela signifie que vous pouvez bien sûr continuer à créer des applications publiques pour la consultation de vos bases, mais l'interface ressemble désormais à celle de l'Universal App Builder. Pour les apps de requête existantes, la situation est la même que pour les apps de galerie : vous ne devez rien faire et vous pouvez continuer à les utiliser.

{{< warning headline="Gain d'efficacité" text="Les changements décrits ci-dessus nous permettent de nous concentrer sur le développement de l'Universal App Builder et d'atteindre ainsi une vitesse de développement plus élevée pour les fonctionnalités à venir." />}}

## Une expérience utilisateur plus agréable lors de l'importation d'Excel

Avec SeaTable 4.4, l'[importation de tableaux Excel]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) est plus rapide, plus flexible et plus stable : Des tableaux de plusieurs milliers de lignes sont désormais disponibles dans SeaTable en quelques instants. Dans la fenêtre d'aperçu nettement élargie, vous pouvez désormais choisir quels tableaux d'un classeur - tous ou seulement certains - vous souhaitez importer depuis le fichier XLSX. Alors que les caractères spéciaux dans les noms de colonnes et autres cas spéciaux donnaient des résultats indésirables dans le passé, ils sont désormais pris en compte de manière fiable. Des messages d'erreur améliorés donnent des indications claires sur les conflits, notamment lors de l'[importation dans le stockage de données volumineuses]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

![Importation Excel](Excel-Import.png)

{{< warning headline="Petit avant-goût" text="Avec SeaTable 5.0, nous rendons l'importation encore plus flexible ! Il est désormais possible de sélectionner des colonnes individuelles d'un tableau et de les exclure de l'importation." />}}

## Plus de fonctions pour les ensembles de données partagés

[Les ensembles de données partagés]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}) sont très utiles lorsque vous et les membres de votre équipe avez besoin de certains tableaux (par exemple une liste d'employés) à travers différents [groupes]({{< relref "help/startseite/gruppen/einfuehrung-in-die-arbeit-mit-gruppen" >}}) dans vos bases. Avec SeaTable 4.4, trois nouvelles fonctions viennent s'ajouter à celles déjà existantes :

1. Si vous avez une [Copier la base]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}})Si vous utilisez des bases de données qui contiennent des enregistrements partagés, vous pouvez décider de conserver ou non le lien avec ces enregistrements. Le groupe dans lequel vous copiez la base doit bien sûr avoir accès aux enregistrements communs.

    ![Retenir le lien vers le dataset commun lors de la copie d'une base](Retain-link-to-common-dataset-when-copying-a-base.gif)

2. Après la [Restauration de bases à partir de snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}) ou le [Création d'une base à partir d'un modèle]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}}) permet de lier des tables existantes à un enregistrement commun et de permettre ainsi la synchronisation avec les données qui s'y trouvent. Jusqu'à présent, il n'était pas possible de réimporter des enregistrements communs, mais seulement de les intégrer dans de nouvelles tables.

    ![Réimportation common dataset](Reimport-common-dataset.gif)

3. Depuis peu, le créateur d'un ensemble de données communes peut [Synchronisation]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}}) de toutes les tables dépendantes avec l'ensemble de données, garantissant ainsi que les autres utilisateurs utilisent l'état actuel des données dans leurs bases. Par le passé, vous deviez compter sur les utilisateurs pour configurer la synchronisation automatique ou pour la déclencher manuellement.

    ![Synchronisation forcée du jeu de données commun](Force-sync-of-common-dataset.png)

## Les valeurs par défaut s'appliquent partout

Avec la version 4.4, SeaTable généralise l'application des [valeurs par défaut]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}). Lorsque vous créez une nouvelle ligne, que ce soit dans le tableau d'une base ou d'une app, via une [colonne de liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), un [formulaire web]({{< relref "help/base-editor/webformulare" >}}), un [bouton]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) ou [une automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), les valeurs par défaut s'appliquent partout lors de la création de la ligne. Jusqu'à présent, les valeurs par défaut ne s'appliquaient que lorsqu'une nouvelle ligne était créée manuellement dans un tableau.

Comme le champ d'action des valeurs par défaut s'est considérablement élargi, nous avons également créé un point de menu bien en vue dans les options de colonne, qui vous permet de régler facilement les valeurs par défaut.

![La valeur par défaut s'applique à toutes les nouvelles lignes](Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

{{< warning headline="Remarque" text="Si une valeur par défaut est définie à la fois dans le tableau et dans le formulaire web, la valeur du formulaire s'applique à toutes les lignes créées via le formulaire." />}}

D'ailleurs, même lorsque vous créez de nouvelles lignes via l'API, vous pouvez activer les valeurs par défaut avec le paramètre correspondant.

## Et bien plus encore

Vous connaissez déjà l'**éditeur de texte formaté** de plusieurs endroits dans SeaTable, comme la [description de la base]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}), le [type de colonne pour les textes longs]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) ou [les messages électroniques]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}). Avec SeaTable 4.4, nous avons amélioré la convivialité et corrigé quelques bugs. En voici deux : jusqu'à présent, les retours à la ligne multiples étaient supprimés lors de la fermeture de l'éditeur et le texte existant était écrasé lorsque l'utilisateur tapait dans la cellule. Dans le nouvel éditeur, les retours à la ligne multiples sont conservés et peuvent servir à structurer le texte de manière plus claire. Nous avons également éliminé le risque de suppressions involontaires : Lors de la saisie, le nouveau texte précède le texte existant.

Dans la nouvelle version, nous avons également amélioré le **centre de notifications** {{< seatable-icon icon="dtable-icon-notice" >}} sur la page d'accueil. Désormais, vous pouvez voir toutes les [notifications]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) du système au même endroit, suivre la source de la notification et accéder à la page correspondante en un seul clic.

Enfin, nous avons optimisé la boîte de dialogue pour la **réinitialisation du mot de passe SeaTable**. Pour cela, nous avons uniformisé le design et ajouté plus de fonctions. Lorsque vous [modifiez votre mot de passe]({{< relref "help/startseite/persoenliche-einstellungen/eigenes-passwort-aendern" >}}) dans vos paramètres personnels, vous pouvez désormais le faire apparaître en texte clair en cliquant sur l'icône en forme d'œil. De plus, la force de votre nouveau mot de passe s'affiche automatiquement.
