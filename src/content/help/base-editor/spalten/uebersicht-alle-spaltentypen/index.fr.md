---
title: 'Aperçu de tous les types de colonnes'
date: 2022-08-25
lastmod: '2024-03-18'
categories:
    - 'arbeiten-mit-spalten'
author: 'cdb'
url: '/fr/aide/types-colonne-overview'
aliases:
    - '/fr/aide/uebersicht-alle-spaltentypen'
seo:
    title: 'Types de colonnes dans SeaTable : aperçu complet'
    description: 'Découvrez les 26 types de colonnes SeaTable : texte, nombre, fichier, choix, formules, relations et plus encore. Explications et usages typiques.'
star: true
weight: 1
---

SeaTable permet de stocker des informations et des données dans des formats très variés.

- Outre les informations simples basées sur du texte (par ex. mots, chiffres, sommes d'argent), SeaTable prend également en charge le stockage d'informations complexes (par ex. fichiers, images, texte mis en forme, y compris les éléments insérés).
- Les champs de sélection vous permettent de classer vos données dans des catégories définies et les fonctions de validation intégrées (par ex. URL, données de position) garantissent que vos données saisies sont disponibles dans un format uniforme et directement exploitable.
- Les formules permettent d'effectuer des opérations arithmétiques et les jointures créent des relations entre les entrées de différents tableaux, ce qui permet d'effectuer de puissantes opérations dans la base de données.

Découvrez ici SeaTables 26 types de colonnes différents !

## Colonnes avec saisie manuelle des données

Un type est attribué à chaque colonne du tableau. Le type de colonne détermine les données que vous pouvez insérer dans les cellules de la colonne. Par exemple, vous ne pouvez pas insérer de fichiers dans une zone de texte. La colonne date, quant à elle, force la saisie d'une date dans le format choisi.

### Texte

Symbole : {{< seatable-icon icon="dtable-icon-single-line-text" >}} **Texte**

Ce type de colonne stocke **du texte** sans mise en forme et fait partie des types de colonnes les plus basiques de SeaTable. Le contenu textuel est composé de **lettres**, de **chiffres**, de **caractères spéciaux** et **d'espaces**. C'est pourquoi les colonnes de texte sont souvent utilisées pour les noms et les (courtes) descriptions.

[En savoir plus sur la colonne de texte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Texte mis en forme

Symbole : {{< seatable-icon icon="dtable-icon-long-text" >}} **Texte mis en forme**

Dans ce type de colonne, vous pouvez enregistrer **des textes plus longs** avec des éléments insérés, tels que **des images** et **des tableaux**. Pour vos textes, vous disposez en outre de diverses options de formatage et de structuration à l'aide du langage de balisage Markdown. C'est pourquoi la colonne _Texte mis en forme_ est souvent utilisée pour les descriptions et la documentation. S'il est utile pour la saisie d'informations que les textes contiennent des éléments structurants et/ou que le texte et les images soient proches les uns des autres, ce type de colonne est alors idéal.

[En savoir plus sur la colonne Texte mis en forme]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Nombre

Symbole : {{< seatable-icon icon="dtable-icon-number" >}} **Nombre**

Les colonnes de nombres stockent **des informations numériques** et peuvent être utilisées de différentes manières pour travailler avec des nombres de toutes sortes. Une information numérique peut être un **nombre**, un **pourcentage** ou une **somme d'argent**. De plus, les colonnes numériques vous permettent de **calculer des valeurs** que vous pouvez visualiser à l'aide de formules et [de statistiques]({{< relref "help/base-editor/statistiken" >}}). Cependant, les colonnes numériques ne conviennent pas pour stocker des chaînes de caractères de n'importe quelle longueur et SeaTable refuse de saisir des lettres dans ce type de colonne.

[En savoir plus sur la colonne des chiffres]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})

### Date

Symbole : {{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} **Date**

La colonne des dates vous permet de saisir **des heures** et **des dates** à la minute près dans vos tableaux. Notez que les colonnes de date interprètent toujours les informations saisies comme des dates, de sorte que les saisies qui ne peuvent pas être interprétées comme des dates sont toujours rejetées comme non valables.

[En savoir plus sur la colonne des dates]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})

### Durée

Symbole : {{< seatable-icon icon="dtable-icon-duration" >}} **Durée**

La colonne des durées est un type de colonne de nombres spécialisé pour l'enregistrement de **mesures, de durées et d'intervalles de temps** et peut enregistrer une période à la minute ou même à la seconde près. C'est la raison pour laquelle cette colonne convient particulièrement bien, entre autres, pour enregistrer la durée de différents événements. Notez toutefois que les entrées non numériques sont toujours rejetées comme non valables.

[En savoir plus sur la colonne permanente]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})

### Sélection unique

Symbole : {{< seatable-icon icon="dtable-icon-single-election" >}} **Sélection unique**

Dans une cellule d'une colonne de sélection unique, vous pouvez choisir **une valeur** dans une liste d'options définies. Vous créez vous-même la liste des options définies pour chaque colonne de sélection unique et pouvez l'adapter à tout moment aux circonstances changeantes. La sélection unique est donc particulièrement adaptée à la catégorisation et au regroupement de vos données.

[En savoir plus sur la colonne de sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})

### Sélection multiple

Symbole : {{< seatable-icon icon="dtable-icon-multiple-selection" >}} **Sélection multiple**

Lors d'une sélection multiple, vous pouvez choisir un **nombre quelconque de valeurs** dans une liste d'options définies. Comme pour la sélection unique, vous créez vous-même la liste des valeurs possibles et l'adaptez à vos besoins individuels. La sélection multiple est donc idéale pour l'indexation - également appelée tagging.

[En savoir plus sur la colonne de sélection multiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})

### Image

Symbole : {{< seatable-icon icon="dtable-icon-picture" >}} **Image**

Le type de colonne Image enregistre un nombre quelconque de **fichiers image** dans les formats de fichier **BMP**, **GIF**, **ICO**, **JPG**, **PNG**, **SVG** et **TIF**. La colonne Image est donc une colonne de fichiers limitée aux formats de fichiers image.

[En savoir plus sur la colonne d'images]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}})

### Fichier

Icône de la page : {{< seatable-icon icon="dtable-icon-file" >}} **Fichier**

Le type de colonne Fichier stocke un nombre quelconque de fichiers **de tout type**. SeaTable propose une fonction d'aperçu pour de nombreux formats de fichiers image.

[En savoir plus sur la colonne des fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})

### E-mail :

Symbole : {{< seatable-icon icon="dtable-icon-email" >}} **E-mail**

Les colonnes d'e-mails sont des colonnes de texte spécialisées pour la saisie et l'enregistrement d'**adresses e-mail** et permettent une utilisation directe par un simple clic de souris. La colonne e-mail est particulièrement pratique pour les formulaires web. L'utilisation d'un champ e-mail à la place d'une colonne de texte garantit que la saisie a la syntaxe d'une adresse e-mail valide. En outre, les colonnes d'e-mails peuvent être utilisées pour envoyer des e-mails via des [boutons]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) et [des automatisations]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).

Si vous avez besoin d'informations plus détaillées sur la colonne des e-mails, jetez un coup d'œil à cet [article]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}).

### URL

Symbole : {{< seatable-icon icon="dtable-icon-url" >}} **URL**

Les colonnes URL interprètent les informations saisies comme une **ressource** du réseau local ou d'Internet et permettent un appel direct par un clic. Comme les entrées dans ce type de colonne ne sont pas validées, il est possible d'enregistrer dans une cellule une adresse Internet (par ex. https://seatable.com) ou une adresse IP (par ex. 192.168.178.1).

[En savoir plus sur la colonne URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})

### Case à cocher

Symbole : {{< seatable-icon icon="dtable-icon-check-square-solid" >}} **case à cocher**

Les cases à cocher permettent de saisir **des informations binaires**: Oui ou Non ou _coché_ vs _non coché_. Il n'est pas possible de saisir d'autres données. C'est pourquoi elles conviennent bien, par exemple, pour marquer des tâches comme étant terminées - c'est-à-dire pour avoir un aperçu des lignes qui remplissent une certaine condition oui/non. Pour cette raison, les colonnes de cases à cocher peuvent également être utilisées de manière optimale pour [filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) ou [regrouper]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}).

[En savoir plus sur la colonne des cases à cocher]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}})

### Classement

Symbole : {{< seatable-icon icon="dtable-icon-rate" >}} **Classement**

Une colonne de classement permet de **classer** vos enregistrements afin d'établir un **classement** ou une **évaluation de la qualité**. Vous pouvez choisir une échelle de notation de 1 à 10 et choisir entre différentes couleurs et formes. Les données peuvent ainsi être évaluées et notées rapidement et facilement, de manière compréhensible pour tous.

[En savoir plus sur la colonne Classement]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})

### Numéro de téléphone

Symbole : {{< seatable-icon icon="dtable-icon-telephone" >}} **Numéro de téléphone**

SeaTable dispose de son propre type de colonne pour les numéros de téléphone. Par rapport à une colonne de texte normale, la colonne de numéro de téléphone offre l'avantage de pouvoir **appeler un numéro de téléphone** d'un simple clic de souris.

[En savoir plus sur la colonne Numéro de téléphone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

### Formule

Symbole : {{< seatable-icon icon="dtable-icon-formula" >}} **Formule**

Les formules vous permettent de **relier** différentes valeurs de colonnes d'une ligne et de créer différentes **fonctions** basées sur le contenu de ces colonnes. Vous pouvez entre autres calculer des valeurs dans vos tableaux, modifier des valeurs ou mettre en relation des valeurs de la même ligne.

Vous avez besoin de plus d'informations sur la colonne des formules ? Jetez un coup d'œil à cet [article]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}). Les formules étant une fonctionnalité très complexe, vous trouverez de nombreux autres articles d'aide dans notre manuel. Cliquez [ici]({{< relref "help/base-editor/formeln" >}}) et vous serez redirigé vers la page d'aperçu.

### Lien vers d'autres entrées

Symbole : {{< seatable-icon icon="dtable-icon-link-other-record" >}} **Lien vers d'autres entrées**

Dans les cellules de ce type de colonne, vous pouvez saisir un nombre quelconque de **références à des entrées dans d'autres tableaux** de la base. La colonne des liens est conçue pour représenter des relations entre des entrées de différents tableaux. Les relations 1:n et n:1 peuvent être représentées avec la colonne de liaison, tout comme les relations n:m. La colonne de liaison peut également être utilisée pour représenter les relations entre les tableaux.

Vous trouverez plus d'informations sur le type de colonne Lien vers d'autres entrées [ici]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

### Formule pour les liens

Symbole : {{< seatable-icon icon="dtable-icon-link-formulas" >}} **Formule pour les liens**

La formule pour les liens vous permet d'**afficher** les données des **tableaux liés** dans votre tableau actuel et de les **mettre** en relation. Pour le type de colonne, cinq formules différentes sont ensuite disponibles, avec lesquelles vous pouvez également effectuer des calculs statistiques. La condition préalable à l'utilisation de la colonne est la présence d'au moins une colonne de type **lien vers d'autres entrées** dans votre tableau.

[En savoir plus sur la colonne Formule pour les liens]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}})

### Collaborateur

Symbole : {{< seatable-icon icon="dtable-icon-collaborator" >}} **Collaborateur**

Dans une colonne Collaborateur, vous pouvez saisir un nombre quelconque d'**utilisateurs** qui ont au moins un accès en lecture à la base. Les utilisateurs de SeaTable sans accès ne peuvent pas être saisis dans la colonne comme collaborateurs. D'autres saisies ne sont pas non plus autorisées. La colonne des collaborateurs est particulièrement utile pour la gestion de projet. Si vous saisissez par exemple des tâches à effectuer dans un tableau, vous pouvez enregistrer les personnes qui les exécutent et le responsable dans des colonnes de type collaborateur.

[En savoir plus sur la colonne des collaborateurs]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}})

### Bouton

Symbole : {{< seatable-icon icon="dtable-icon-button" >}} **Bouton**

Les boutons permettent **d'automatiser** le traitement des données ou l'exécution de certaines actions. Notez toutefois que vous devez toujours utiliser les boutons **manuellement**. Le bouton que vous pouvez ajouter à vos lignes dans cette colonne vous permet de déclencher certaines actions définies au préalable. C'est pourquoi ce type de colonne convient particulièrement bien à l'automatisation des étapes de processus.

Vous trouverez plus d'informations sur le bouton et les actions pouvant être déclenchées dans les colonnes de ce type dans cet [article]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}).

### Géolocalisation

Symbole : {{< seatable-icon icon="dtable-icon-location" >}} **Géolocalisation**

Dans cette colonne, vous pouvez enregistrer **des lieux** et les visualiser plus tard avec le [plug-in de carte]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}/). Pour cela, vous pouvez choisir d'indiquer le pays et la région ou la latitude et la longitude. Vous avez en outre la possibilité de trouver un pays ou une région à l'aide de la fonction de recherche et de l'ajouter comme entrée.

[En savoir plus sur la colonne de Géolocalisation]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

### Signature digitale

Symbole : {{< seatable-icon icon="dtable-icon-rename" >}} **Signature digitale**

Dans une colonne de Signature digitale, vous pouvez déposer **des signatures digitales** qui seront automatiquement enregistrées dans le gestionnaire de fichiers de votre base. Les signatures digitales conviennent très bien à la saisie de données à l'aide de **formulaires web**, par exemple pour faire signer facilement des demandes en ligne.

[En savoir plus sur la colonne "Signature digitale".]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}})

## Types de colonnes avec saisie automatique des données

Outre les types de colonnes dans lesquels vous saisissez des données en tant qu'utilisateur, il existe dans SeaTable cinq autres types de colonnes dont le contenu est généré automatiquement par SeaTable. Ces colonnes ne peuvent pas être modifiées manuellement par l'utilisateur. Elles sont principalement utilisées à des fins de documentation.

### Créateur

Symbole : {{< seatable-icon icon="dtable-icon-creator" >}} **Créateur**

SeaTable documente automatiquement le **nom de l'utilisateur** qui a créé la ligne dans la colonne du créateur.

[En savoir plus sur la colonne du créateur]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Date de création

Symbole : {{< seatable-icon icon="dtable-icon-creation-time" >}} **Date de création**

SeaTable documente automatiquement **la date et l'heure de création de la ligne** dans la colonne de la date de création. La date et l'heure sont affichées au format AAAA-MM-JJ HH:MM.

[En savoir plus sur la colonne de la date de création]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Dernier éditeur

Symbole : {{< seatable-icon icon="dtable-icon-creator" >}} **Dernier éditeur**

SeaTable documente automatiquement le **nom de l'utilisateur** qui a **apporté** la **dernière modification** à une entrée dans la colonne Dernier éditeur. Comme cette colonne enregistre automatiquement les modifications apportées aux entrées, elle convient bien, par exemple, comme déclencheur pour les automatisations ainsi que pour les filtres et les tris.

[En savoir plus sur la colonne Dernier éditeur]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Date de dernière modification

Symbole : {{< seatable-icon icon="dtable-icon-creation-time" >}} **Date de dernière modification**

SeaTable documente **la date et l'heure de la dernière modification d'une entrée** dans la colonne Date de dernière modification. La date et l'heure sont affichées au format AAAA-MM-JJ HH:MM. Comme la colonne enregistre automatiquement les modifications apportées aux entrées, elle convient bien comme déclencheur pour les automatisations ainsi que pour les filtres et les tris.

[En savoir plus sur la colonne Date de dernière modification]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Numéro automatique

Symbole : {{< seatable-icon icon="dtable-icon-autonumber" >}} **Numéro automatique**

Le type de colonne Numéro automatique génère **automatiquement** un **numéro croissant** pour chaque nouvelle ligne. Ce type de colonne est toujours utilisé lorsque vous avez besoin d'un identifiant unique pour chaque enregistrement.

[En savoir plus sur la colonne Numéro automatique]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}).
