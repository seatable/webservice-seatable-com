---
title: 'SeaTable 6.0 : Le No-Code devient intelligent'
description: "SeaTable 6.0 allie no‑code et IA : nouvelles fonctions d’IA, éditeur d’automations revu, vues calendrier, Kanban, galerie et colonne téléphone."
date: 2025-11-04
author: 'rdb'
url: '/fr/seatable-release-6-0'
color: '#ff9831'
categories:
    - 'product-features'
seo:
    title:
    description:
register:
   show: true    
---

SeaTable 6.0 combine la puissance du No-Code et de l'Intelligence Artificielle (IA). **Les nouvelles fonctionnalités d'IA** permettent d'analyser, de modifier et d'étendre des ensembles de données, d'exploiter des documents et d'extraire avec précision des informations pertinentes. Et ce, sans aucun souci de protection des données et de confidentialité : SeaTable prend en charge un grand nombre de fournisseurs et de modèles d'IA. Bien entendu, l'auto-hébergement des modèles d'IA est également possible. C'est ce que nous faisons pour protéger vos données.

**L'éditeur de règles d'automatisation** entièrement remanié rend l'utilisation des nouvelles fonctions d'IA très simple. Mais toutes les autres automatisations bénéficient également de l'interface utilisateur orientée workflow de l'éditeur de règles et de ses fonctions avancées.

**Les nouveaux types de vue Calendrier, Kanban et Galerie**, qui remplacent les plug-ins du même nom, offrent également plus de clarté et de fonctions. Tout comme la vue Tableau bien connue, les trois nouveaux types de vue favorisent la collaboration au plus haut niveau avec des fonctions telles que le partage de vues, les vues privées et la modification collaborative des données en temps réel.

De nombreuses améliorations dans l'App Builder et l'Éditeur de base, telles que la disponibilité universelle de filtres complexes et **le nouveau type de colonne Numéro de téléphone**, optimisent les fonctionnalités existantes et répondent aux besoins des clients.

Nous avons mis à jour SeaTable Cloud à la version 6.0 ce matin. Les auto-hébergeurs qui ont pu utiliser une version bêta depuis le 30 septembre peuvent désormais télécharger la version stable depuis le fameux [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) de SeaTable Server. Comme toujours, la liste complète des changements est disponible dans le [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/).

## KI-ready avec des automatisations d'IA (bêta)

Analyser des textes, traduire des manuscrits, extraire des informations de documents, créer des brouillons basés sur des mots-clés et bien plus encore – les nouvelles fonctionnalités d'IA de SeaTable apportent la puissance de l'IA moderne directement dans SeaTable.

Des **fonctions d'IA dédiées** sont disponibles pour les tâches standard. Des fonctions telles que *Summarize*, *OCR*, *Extract* et *Classify* rendent l'utilisation de l'IA dans les processus d'entreprise aussi simple qu'on puisse l'imaginer. Il vous suffit de choisir la fonction et de définir les colonnes d'entrée et de sortie. Vous pouvez transmettre des instructions détaillées, si nécessaire, au modèle d'IA via une invite.

![Nouvelles fonctions d'IA](new-ai-function.png)

Si aucune fonction d'IA dédiée ne convient, la fonction **Custom** peut être utilisée. Avec cette fonction, le modèle d'IA agit uniquement sur la base de votre invite individuelle. Vous passez simplement les informations de l'ensemble de données en référençant une colonne entre accolades, par exemple "Écrivez une histoire de 1000 mots en vous basant sur les mots-clés de {Keywords}"

Les nouvelles fonctions d'IA sont intégrées aux automatisations de SeaTable et sont tout aussi faciles – probablement même plus faciles grâce à l'éditeur révisé – à créer, utiliser et gérer. Bien entendu, vous pouvez également ajouter des fonctions d'IA aux règles d'automatisation existantes pour les rendre encore plus performantes.

### Déployer l'IA sans compromettre la protection des données

SeaTable Cloud utilise comme modèle d'IA un **Gemma3** avec 12 milliards de paramètres. Ce modèle multimodal Large Language (LLM) de Google fonctionne **sur un serveur allemand** de Hetzner Online GmbH et est géré par les administrateurs de SeaTable Cloud. L'échange de données entre SeaTable Cloud et le modèle linguistique est **crypté**. Vos données ne sont donc pas transférées vers un autre fournisseur d'IA ni à l'étranger.

Tous les abonnés à SeaTable Cloud Enterprise reçoivent **500 crédits d'IA par membre de l'équipe**. Les crédits d'IA sont calculés de manière à permettre des tests à grande échelle. Des crédits supplémentaires sont nécessaires pour les charges de travail productives. Ceux-ci peuvent être fournis gratuitement sur demande pendant la phase bêta.

**Les auto-hébergeurs de SeaTable Server** peuvent également héberger eux-mêmes leur LLM, mais ce n'est pas obligatoire. **SeaTable AI**, un nouveau composant de SeaTable Server, est basé sur LiteLLM, ce qui permet de connecter un grand nombre de modèles et de fournisseurs, y compris tous les services LLM avec une API compatible avec OpenAI. Le déploiement de SeaTable AI, tout comme celui de tous les autres composants de SeaTable Server, s'effectue via Docker ou Docker Compose. Le [Guide de l'administrateur](https://admin.seatable.com/) contient des exemples de configurations pour de nombreux LLM populaires.

### Perspectives pour la suite du développement de l'IA

Les fonctionnalités d'IA de SeaTable 6.0 sont en version bêta et seront améliorées et étendues de manière dynamique dans les mois à venir. Le travail sur un **Assistant IA** et un **Serveur MCP** est en cours. D'autres modèles d'IA seront bientôt disponibles dans SeaTable Cloud. Outre le LLM hébergé par SeaTable, des modèles des fournisseurs bien connus **OpenAI, Anthropic, Meta et xAI** seront disponibles, ainsi que ceux du fournisseur européen **Mistral**. Les administrateurs de SeaTable Server pourront également configurer plusieurs modèles d'IA. Ils pourront ainsi utiliser le modèle optimal pour chaque cas d'utilisation.

**Le suivi de l'utilisation** et la **gestion des autorisations** sont d'autres points forts du développement. Notre objectif : un maximum de transparence et de contrôle sur l'utilisation des crédits d'IA dans SeaTable.

## L'automatisation n'a jamais été aussi simple

Dans SeaTable 6.0, **créer et gérer des règles d'automatisation** devient encore plus facile et pratique. Un éditeur entièrement repensé offre une plus grande clarté et des fonctionnalités supplémentaires.

![nouvel éditeur d'automatisation](new-automation-editor.png)

L'éditeur de SeaTable 6.0 s'étend sur toute la largeur de l'écran, ce qui permet **une nouvelle mise en page** : Sur la gauche, vous trouverez toutes les règles existantes, comme dans les vues. **Le passage d'une règle à une autre** se fait donc en un seul clic. Dans la zone centrale se trouve la règle d'automatisation active. La **configuration du déclencheur ou des actions** est affichée de manière dynamique sur le côté droit. Un autre facteur de confort est la **hauteur variable du tableau de bord de l'éditeur**. Ainsi, les noms des colonnes et les données d'exemple restent visibles pendant que vous travaillez sur une règle d'automatisation.

Le nouvel éditeur tient également compte du souhait souvent exprimé de pouvoir **grouper et déplacer les règles d'automatisation**. En outre, il est possible de dupliquer des actions dans une règle.

## Trois plugins deviennent des vues

Les trois plugins [Calendrier]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}), [Galerie]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}) et [Kanban]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}) ont été intégrés à SeaTable depuis la version 1.0. Après 5 ans d'existence, ils prennent une nouvelle forme : Les plugins Calendrier, Kanban et Galerie deviennent **Vues Calendrier, Kanban et Galerie**. Dans SeaTable 6.1, le plugin [Timeline]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}) suivra.

La réimplémentation des plugins sous forme de vues présente plusieurs avantages : D'une part, l'utilisation est considérablement simplifiée . **Il n'est pas nécessaire d'installer les plugins dans une base**, car les vues sont immédiatement disponibles. Les administrateurs de SeaTable Server apprécieront également cette intégration : La mise à jour séparée des plugins n'est plus nécessaire.

![nouvelle vue du calendrier](new-view-list-pinned.png)

En outre, les nouvelles vues sont fonctionnellement bien supérieures aux plugins existants : Les vues Calendrier, Kanban et Galerie peuvent être partagées individuellement dans le cadre d'un [partage de vue]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}}) ou d'une [autorisation de partage personnalisée]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}). L'ancienne nécessité de [partager la base entière]({{< relref "help/startseite/freigaben/eine-base-an-eine-gruppe-freigeben" >}}) pour travailler ensemble sur un calendrier ou un tableau Kanban est supprimée. Les vues de tous les types offrent également en option des **vues privées** que seul le créateur peut voir. Toutes les vues, à l'exception de la vue Big Data, prennent également en charge la **modification collaborative en temps réel**. Une modification effectuée par un utilisateur est immédiatement signalée aux autres utilisateurs.

{{< warning headline="Veuillez noter" text="Avec SeaTable 6.0, les trois plugins ne pourront plus être installés dans les bases. Dans les bases où les plugins sont déjà utilisés, ils resteront disponibles et pourront être utilisés sans restriction. Cependant, notre recommandation est différente : Profitez des avantages des nouvelles vues ! Le changement ne pourrait pas être plus simple. Les trois plug-ins proposent la **migration en un clic**. Celle-ci convertit un onglet dans un plugin en une vue du même type sans effort supplémentaire" />}}

## Plus de flexibilité dans l'App Builder

Dans le [App Builder]({{< relref "help/app-builder" >}}) de SeaTable 6.0, vous remarquerez **le nouveau bouton orange Plus**. Il vous permet d'ajouter un nouvel élément à la navigation, où que vous soyez dans votre application. Une nouveauté fonctionnelle apparaît lorsque vous cliquez sur le bouton : en plus des pages et des dossiers, vous pouvez désormais ajouter des **liens directs vers des sites Web externes** dans la navigation. Un lien vers une déclaration de confidentialité ou un wiki externe ne doit donc plus être intégré dans une page, mais peut apparaître bien en vue directement dans la navigation. Plusieurs clients nous ont demandé cette option de conception.

![insérer un lien direct](new-direct-link-in-apps.gif)

Les autres améliorations apportées à l'App Builder concernent également la flexibilité : les paramètres de page des [types de page]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) Calendrier, Kanban, Galerie et Ligne de temps permettent désormais de **protéger les colonnes individuelles des modifications**. Ainsi, tous les types de pages concernés offrent désormais cette fonctionnalité.

Disponible dans la Base depuis la version 5.2, elle est maintenant également disponible dans l'App Builder : **filtres complexes**. Les paramètres de données et les paramètres des colonnes de liens prennent désormais en charge les groupes de filtres. De même, les utilisateurs d'une page de tableau peuvent désormais utiliser des modèles de recherche avec des opérateurs logiques ET et OU.

## Plus de fonctionnalités dans la gestion d'équipe

La [gestion d'équipe]({{< relref "help/teamverwaltung" >}}) de SeaTable Cloud a été largement remaniée dans la version majeure. La première chose qui saute aux yeux est l'harmonisation du design de la gestion d'équipe avec celui du site web. Mais ce qui est plus important pour l'utilisation, ce sont les nouvelles fonctionnalités :

- Configuration du SSO via SAML (uniquement pour les abonnés Enterprise)
- Intégration d'un journal des activités de l'équipe (uniquement pour les abonnés Enterprise)
- Intégration d'un journal des connexions de l'équipe
- Envoi de factures par e-mail
- Gestion de plusieurs moyens de paiement


## Autres améliorations

La version 6.0 introduit le 26e type de colonne de SeaTable. **Le nouveau type de colonne Numéro de téléphone** rend la communication encore plus facile. Un clic sur l'icône du téléphone dans une cellule transfère le numéro de téléphone dans votre application de téléphonie. Sur les téléphones portables, cela fonctionne sans aucune configuration supplémentaire. Sur le bureau, il en va de même si un raccourci vers un logiciel de téléphonie est configuré dans le navigateur.

![type de colonne numéro de téléphone](new-column-type-phone-number.gif)

La [fonction d'exportation]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) prend en charge, avec SeaTable 6.0, l'**exportation des données archivées dans l'entrepôt de big data**. Si vous activez cette option lors de l'exportation, SeaTable crée d'abord le fichier d'exportation au format DTABLE et vous en informe par une notification une fois le processus terminé. Le téléchargement du fichier s'effectue ensuite via le gestionnaire de fichiers de la base. Les données de l'entrepôt de big data sont enregistrées dans un format binaire dans le dossier "archive" du fichier DTABLE. Bien entendu, un fichier DTABLE contenant des données volumineuses peut être facilement réimporté dans SeaTable comme tout autre fichier DTABLE.

La saisie des données dans les [colonnes de dates]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) devient plus pratique. Auparavant, SeaTable exigeait la saisie d'une date complète. Si une partie, par exemple l'année ou un zéro de tête, était omise, il s'agissait d'une entrée non valide. Ce n'est plus le cas. "25-11-4" est correctement interprété comme 2025-11-04. Et cela ne fonctionne logiquement pas seulement pour les dates au format ISO.

Essayez SeaTable 6.0 ! Nous sommes convaincus que vous serez vous aussi enthousiasmé.

{{< newsletter title="Restez informé" subtitle="" submit="S'abonner maintenant" >}}

Inscrivez-vous à notre **Newsletter** et ne manquez plus jamais les nouveautés de SeaTable !

{{< /newsletter >}}
