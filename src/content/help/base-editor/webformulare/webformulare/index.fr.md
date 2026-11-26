---
title: 'Formulaires web'
date: 2022-08-25
lastmod: '2026-11-26'
categories:
    - 'webformulare'
author: 'cdb'
url: '/fr/aide/formulaires-web-seatable'
aliases:
    - '/fr/aide/webformulare'
seo:
    title: 'Formulaires web SeaTable : création, personnalisation et partage faciles'
    description: 'Formulaires web dans SeaTable : créez, configurez et testez des formulaires pour collecter facilement des données internes et externes.'
weight: 1
star: true
---

Les **formulaires web** sont le moyen de choix pour permettre aux membres de l'équipe et à des tiers externes de saisir de nouveaux enregistrements dans vos tableaux. Les utilisateurs accèdent à un formulaire par un **lien**, de sorte qu'il n'est **pas nécessaire de partager** le tableau. Les formulaires web sont donc particulièrement adaptés à la saisie de données par un grand nombre de **personnes au sein et en dehors de votre équipe**.

Familiarisez-vous avec la fonction de formulaire de SeaTable pour collecter facilement des données via des formulaires web !

## Fonctionnement des formulaires web

Le formulaire web classique est idéal pour les **enquêtes en ligne**, les **demandes** et la saisie structurée de nouvelles données. Les colonnes du tableau sont intégrées à l'aide de **champs de formulaire** et les utilisateurs sont guidés tout au long du processus de remplissage. Pour y accéder, vous créez un lien qui permet aux utilisateurs **sans compte SeaTable** de remplir le formulaire web. Un formulaire web rempli correspond à **un nouvel enregistrement** ou à une ligne ajoutée dans le tableau correspondant.

Les formulaires web se réfèrent toujours à un **tableau** de la base ouverte. C'est pourquoi vous devez d'abord sélectionner le tableau concerné avant de créer un formulaire. Dans chaque base, vous pouvez créer et enregistrer un **nombre illimité** de formulaires web.

## Créer un formulaire

Ouvrez la gestion des formulaires en cliquant sur le bouton {{< seatable-icon icon="dtable-icon-form" >}} **Formulaires** en haut à droite dans l'en-tête de la base. La gestion des formulaires se présente sous forme de liste vide si aucun formulaire n'a encore été créé dans la base. Sinon, les formulaires déjà existants sont affichés dans la fenêtre ouverte.

![Créer un formulaire classique](images/create-a-web-form.gif)

Vous créez un [nouveau formulaire web]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}}) en cliquant sur **Créer un formulaire web** en bas de la gestion des formulaires, puis en sélectionnant **Formulaire classique**.

Saisissez maintenant le **nom** du nouveau formulaire web qui doit également être affiché dans la gestion des formulaires. Utilisez un nom concis afin de garder une vue d'ensemble si vous avez de nombreux formulaires. Vous pourrez bien sûr modifier le nom ultérieurement.

Si vous cliquez sur l'**icône en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}}, l'**éditeur de formulaire web** s'ouvre avec sa vue en deux parties : à gauche, le formulaire web est affiché en mode brouillon ; à droite se trouvent les **paramètres**.

Il existe de nombreuses [possibilités de configuration]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}}) permettant d'adapter rapidement et facilement un formulaire web à vos souhaits et à vos idées.

Les **paramètres du formulaire web** à droite vous permettent de prendre les décisions suivantes :

- À quel **tableau** le formulaire est-il lié ?
- Quels **éléments statiques** et **champs de tableau** souhaitez-vous intégrer dans le formulaire ?
- Souhaitez-vous créer un **formulaire de plusieurs pages** à l'aide de sauts de page ?
- Une **notification** doit-elle être envoyée (à vous) lors de la soumission du formulaire ?
- Qui peut **accéder** au formulaire ?
- Tous les champs doivent-ils être **obligatoires** ?
- Une **barre de progression** doit-elle être affichée aux personnes qui remplissent un formulaire de plusieurs pages ?
- Faut-il afficher "Powered by" ?
- Quel **message** est affiché au participant après la soumission du formulaire ?
- Souhaitez-vous **rediriger** le participant **vers une page web** après la soumission du formulaire ?
- Le formulaire a-t-il un **délai de soumission** ?
- Le formulaire a-t-il une **limite de soumissions** ?

Les champs disponibles dans le formulaire dépendent des **colonnes** du tableau sélectionné. Si vous ajoutez ou supprimez des colonnes dans le tableau, les champs disponibles dans les paramètres s'adaptent automatiquement. Les **noms** et l'**ordre** des champs de tableau sont directement repris du tableau sous-jacent.

![Ajouter et configurer des champs dans un formulaire web](images/Add-fields-to-a-web-form.gif)

**Glissez-déposez** les champs du tableau dans votre brouillon ou cliquez sur le **symbole plus** à droite du nom de la colonne. Vous pouvez modifier l'ordre des champs dans le formulaire web à votre guise en cliquant sur le **symbole à six points** {{< seatable-icon icon="dtable-icon-drag" >}} dans le coin droit d'un champ et en glissant-déposant le champ à l'endroit souhaité.

{{< warning  type="warning" headline="Types de colonnes non sélectionnables"  text="Vous ne pouvez en principe pas intégrer dans un formulaire web des colonnes de type Collaborateur, Formule, Formule pour les liens, Créateur, Date de création, Dernier éditeur, Date de dernière modification, Numéro automatique et Bouton." />}}

Dans le brouillon, vous pouvez cliquer sur chaque champ, ce qui vous permet d'accéder aux **paramètres du champ**. Pour chaque champ, vous pouvez déterminer si ...

- un **nom de champ** différent du nom de la colonne doit être affiché dans le formulaire,
- un champ reçoit un **texte d'aide** complémentaire comme indication de remplissage,
- un champ est un **champ obligatoire**,
- un champ doit contenir une **valeur par défaut**,
- l'affichage du champ dépend d'une **condition**.

{{< warning  headline="Champs de sélection"  text="Pour les champs de sélection unique et multiple, vous pouvez également définir si les valeurs doivent être affichées sous forme de **liste** ou de **liste déroulante**." />}}

Pour vérifier à quoi ressemble le formulaire pour le destinataire, cliquez en haut à droite sur le bouton **Page du formulaire web**. Le formulaire s'ouvre alors dans un nouvel onglet, tel qu'un autre utilisateur le verrait.

## Partager le formulaire

Pour rendre le formulaire accessible à d'autres personnes, vous avez besoin d'un **lien**. Vous obtenez le lien du formulaire dans l'éditeur de formulaire web en cliquant sur le bouton {{< seatable-icon icon="dtable-icon-share" >}} **Partager**. Vous pouvez utiliser le **lien généré automatiquement** ou créer **vos propres liens** et les enrichir de [valeurs pré-remplies]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}).

![Nouvelle boîte de dialogue de lien de formulaire dans SeaTable 4.3](images/Formularlink-Dialog.gif)

{{< warning  headline="Liens personnalisés"  text="La partie personnalisée qui est ajoutée au lien doit comporter **entre 5 et 30 caractères** et ne peut contenir que des **lettres**, des **chiffres** et des **tirets**. De plus, chaque URL doit être unique : si une URL personnalisée est déjà utilisée, un message d'erreur apparaît." />}}

Avant d'envoyer le lien du formulaire ou de le rendre public, vous devriez tester le formulaire de manière approfondie.

## Tester le formulaire

Des tests approfondis évitent toute frustration de la part des destinataires. Les problèmes peuvent être causés par des ambiguïtés ou des conflits dans le formulaire. Dans le pire des cas, un formulaire ne peut pas être envoyé parce qu'un champ obligatoire ne peut pas être rempli (par exemple, si aucune valeur n'est définie pour une sélection unique).

Ouvrez le formulaire web pour le tester. Depuis l'éditeur de formulaire web, vous pouvez le faire en cliquant sur le bouton **Page du formulaire web**. Depuis la vue tableau, ouvrez d'abord la gestion des formulaires et cliquez ensuite sur le nom du formulaire web. Dans les deux cas, le formulaire web s'ouvre dans un nouvel onglet du navigateur.

![Tester un formulaire web](images/Test-a-web-form.gif)

Les valeurs saisies dans le formulaire sont enregistrées dans le tableau lié. N'oubliez pas de supprimer les données de test du tableau avant la collecte de données proprement dite.

## Modifier le formulaire

Vous pouvez à tout moment modifier les formulaires web à l'aide de l'éditeur de formulaire web. Pour revenir à l'éditeur, ouvrez la gestion des formulaires, placez le curseur de la souris sur le nom du formulaire, puis cliquez sur l'**icône en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}} à droite du nom.

## Copier le formulaire

Si vous avez déjà créé un formulaire que vous souhaitez seulement modifier légèrement pour un autre cas d'utilisation, vous pouvez copier le formulaire. Pour ce faire, placez le curseur de la souris sur le nom du formulaire et cliquez sur l'**icône de copie** {{< seatable-icon icon="dtable-icon-copy" >}} à droite du nom.

## Supprimer le formulaire

Vous pouvez à tout moment supprimer des formulaires web via la gestion des formulaires. Placez le curseur de la souris sur le nom du formulaire, puis cliquez sur l'**icône de la corbeille** {{< seatable-icon icon="dtable-icon-delete" >}} à droite du nom.

![Options de la gestion des formulaires](images/form-management-options.png)
