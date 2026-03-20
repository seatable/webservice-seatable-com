---
title: 'SeaTable 6.1 : Plus de puissance pour les applications, les bases et les intégrations'
description: "SeaTable 6.1 apporte des nouveautés pour l'App Builder, le Base Editor et dans la section Intégrations. Il y en a pour tout le monde."
date: 2026-03-20
author: 'rdb'
url: '/fr/seatable-release-6-1'
color: '#fad102'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.1 : Plus de puissance pour les applications, les bases et les intégrations'
    description: "SeaTable 6.1 apporte des nouveautés pour l'App Builder, le Base Editor et dans la section Intégrations. Il y en a pour tout le monde."
register:
   show: true    
---

Dans l'**App Builder**, le nombre de [types de pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) passe à 10 ; le type de page **Carte** est nouveau. Pour les autres types de pages, SeaTable 6.1 étend les possibilités des colonnes de liens. Celles-ci peuvent désormais être configurées de manière cohérente et se voir attribuer des permissions finement définies. Les utilisateurs de l'application peuvent également profiter d'une **option d'impression pour le Tableau de bord** ainsi que de fonctions de filtrage et de tri avancées.

Dans le **Base Editor**, la [colonne de Lien vers d’autres entrées]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) est mise en avant par une mise à jour fonctionnelle : des règles de filtrage dynamique permettent de contrôler les lignes sélectionnables en fonction de la ligne d'origine respective – chaque ligne reçoit ainsi sa propre sélection. Les deux [types de vues]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) **Arbre** et **Ligne du temps** sont également nouveaux et remplacent les plugins du même nom. Dans les journaux de base, les filtres permettent d'obtenir une meilleure vue d'ensemble de l'activité dans une base.

La section **Intégrations** a également connu quelques changements : SeaTable 6.1 introduit une connexion à Google Agenda et une fonction d'importation depuis Airtable. Le plugin amélioré de relations entre les tables est accompagné du nouveau [plugin de Chat IA]({{< relref "help/ai/ai-chat/introduction" >}}), qui permet d'effectuer des analyses et des modifications de données en langage naturel.

SeaTable 6.1 est maintenant disponible en téléchargement dans le fameux [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) ; dans le [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/), vous trouverez – comme toujours – la liste complète des changements.

La nouvelle version sera déployée sur [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) le 25 mars. Cette mise à jour s'accompagne d'une revalorisation des abonnements Free et Plus. **Les automatisations**, jusqu'à présent exclusivement incluses dans l'abonnement Enterprise, seront désormais également disponibles dans [Free et Plus]({{< relref "pages/prices" >}}). Les équipes Free recevront 100 exécutions d'automatisation par mois ; les équipes Plus 500 exécutions par mois et par membre de l'équipe. Le prix de l'abonnement Plus ne sera pas affecté et Free restera gratuit.

## Apps plus puissantes

Les distributions spatiales peuvent être visualisées dans les bases avec le [plugin de carte]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}). Le nouveau type de page **Carte** rend désormais cela possible dans les applications. Les préférences de la page permettent de masquer les enregistrements et de limiter le nombre d'enregistrements affichés, comme c'est le cas pour les autres pages. La valeur d'affichage et l'effet de survol peuvent également être configurés.

![nouveau type de page pour les cartes géographiques](map-page-app-builder-seatable-6-1.png)

{{< warning headline="Note pour les auto-hébergeurs" >}}

Un **token API Google** doit être défini dans la configuration de SeaTable Server pour que le type de page puisse être affiché et utilisé dans l'App Builder. Pour plus de détails, consultez l' [Admin Manual](https://admin.seatable.com/configuration/plugins/#map-plugin).

{{< /warning >}}

SeaTable 6.1 unifie les options de paramétrage et le concept d'autorisation pour les **colonnes de liens dans l'App Builder**. Trois autorisations peuvent être activées individuellement sur les pages de type Galerie, Kanban, Calendrier, Ligne de temps et Enregistrement unique :
- Créer et lier de nouvelles entrées
- Lier des entrées existantes
- Modifier les entrées liées

Dans SeaTable 6.2, une quatrième autorisation **Supprimer les liens existants** sera ajoutée. Les pages de type Tableau de bord et Requête ne disposeront toujours pas de paramètres de lien, car ces deux types de pages ne permettent en principe pas de modification.

Les **paramètres de colonne pour le tableau lié** permettent d'adapter individuellement ces autorisations à un cas d'utilisation concret. L'administrateur de l'application peut définir quelles colonnes sont affichées dans le tableau lié, lesquelles sont modifiables et lesquelles sont obligatoires.

Sur les types de pages Galerie, Kanban et Calendrier, des **fonctions de tri et de filtrage** ont été ajoutées dans la nouvelle version. Celles-ci permettent aux utilisateurs de l'application d'adapter le volume des données affichées et leur présentation – un gain sensible de clarté dès lors que la quantité de données augmente.

La **nouvelle fonction d'impression sur la page du Tableau de bord** offre une plus grande flexibilité. Si elle est activée, elle permet d'imprimer facilement une page sur papier.

## Base Editor plus puissant

### Deux nouveaux types de vues

Le nouveau type de vue **Arbre** représente les enregistrements dans une structure hiérarchique avec des nœuds qui peuvent être développés et réduits – une structure arborescente – et permet ainsi une visualisation intuitive des relations entre les enregistrements. La **hiérarchie des enregistrements** résulte des liens entre les tables. La vue arborescente est particulièrement adaptée à la gestion des catégories de produits et des organisations de projets.

{{< warning headline="Note d'utilisation" >}}
La nouvelle vue arborescente est actuellement limitée à **trois niveaux hiérarchiques** et ne prend pas en charge les liens au sein d'une table.
{{< /warning >}}

Le deuxième nouveau type de vue **Ligne de temps** organise les enregistrements sur une ligne de temps et est donc le premier choix lorsque les relations et les dépendances temporelles sont au premier plan.

![Nouveaux types de vues](two-new-views-seatable-6-1.png)

Les nouvelles vues **remplaceront les plugins du même nom**. La réimplémentation en tant que vues est cependant plus qu'un simple changement d'interface utilisateur. En tant que vues à part entière, elles peuvent être partagées de manière ciblée via des partages de vues et incluses dans des partages personnalisés, ce qui n'est tout simplement pas possible avec un plug-in. La vue arborescente ajoute également des fonctionnalités. Les colonnes à afficher peuvent être sélectionnées pour chaque niveau de la hiérarchie. Avec le [plugin d'Arbre]({{< relref "help/base-editor/plugins/anleitung-zum-tree-plugin" >}}), cela était limité au niveau supérieur.

### Règles de filtrage dans les colonnes de Lien vers d’autres entrées

Un peu caché dans les paramètres de la colonne de Lien vers d’autres entrées se trouve l'une des nouveautés les plus utiles : L'option **Restreindre les liens avec une règle de filtrage**. Cela permet de restreindre la sélection des lignes pouvant être liées sur la base de règles simples ou complexes. Les filtres eux-mêmes peuvent être statiques ou dynamiques :
- Dans le cas d'un **filtre statique**, une valeur de filtre uniforme est utilisée pour filtrer les lignes dans la table liée (par exemple, seules les lignes qui n'ont pas la valeur "archivé" peuvent être liées). L'effet est donc analogue à celui de l'option **Restreindre les liens à une seule vue**.
- Dans le cas d'un **filtre dynamique**, la valeur de filtre utilisée pour filtrer les lignes dans le tableau lié est une valeur de colonne de la ligne active (par exemple, seules les lignes dont l'état est identique à l'état de la ligne active peuvent être liées). **Les lignes avec des valeurs de filtre différentes** ont donc des lignes liées différentes.

![règles de filtrage dans les colonnes de Lien vers d’autres entrées](dynamic-link-selection-filters-seatable-6-1.png)

### Options de filtrage dans les Base Logs

Les administrateurs seront ravis d'apprendre que des options de filtrage ont été ajoutées dans les [Base Logs]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}). Les logs peuvent maintenant être filtrés par utilisateur, table et période. Bien entendu, des filtres combinés sont également possibles. Si vous souhaitez **suivre ou annuler des modifications** dans une base avec de nombreux utilisateurs, vous apprécierez rapidement la nouvelle clarté.

## Plus d'intégrations

Le passage d'Airtable à SeaTable n'a jamais été aussi simple avec SeaTable 6.1 : lors de la création d'une nouvelle base, il suffit de sélectionner **Importer la base depuis Airtable**, de saisir un ID de base Airtable et un jeton d'accès personnel dans la boîte de dialogue d'importation, et le tour est joué. SeaTable s'occupe du reste.

La deuxième nouvelle intégration concerne Google Agenda. La nouvelle action d'automatisation **Gérer les rendez-vous dans Google Agenda** permet de créer des rendez-vous dans un Google Agenda directement depuis SeaTable et de mettre à jour les rendez-vous existants.

### Mise à jour du plugin de relations entre les tables

Le plugin [Relations entre les tables]({{< relref "help/base-editor/plugins/anleitung-zum-tabellenbeziehungen-plugin" >}}) est une vieille connaissance qui bénéficie d'une mise à jour importante avec SeaTable 6.1 :
- Les tableaux peuvent être masqués individuellement
- Les colonnes affichées peuvent être contrôlées par la sélection d'une vue
- Les liens dans un tableau peuvent être masqués
- Nombreuses fonctions de mise en forme
- Fonction d'exportation
- Fonction de réinitialisation du graphique
- Fonction de prise de notes

Vous pouvez ainsi créer des diagrammes de relations clairs, même pour des bases complexes.

![Plugin de relations de tables amélioré](table-relationship-plugin-seatable-6-1.png)

### Chattez avec une intelligence artificielle

Le **plugin Chat IA** est tout nouveau. Il permet de modifier et d'évaluer des bases en langage naturel. Créez des enregistrements, modifiez des valeurs, reliez des lignes, créez des analyses – en allemand, anglais, français et autres langues. Le plug-in est particulièrement utile pour les évaluations ad hoc qui dépassent les fonctions standard.

Une invite d'exemple pour l'évaluation d'une liste de données d'adresses serait : "Listez toutes les personnes de la liste de données d'adresses qui habitent dans une ville de plus d'un million d'habitants." Le modèle évalue alors les adresses résidentielles, détermine le nombre d'habitants du lieu de résidence et génère la liste de résultats sur cette base.

![Plugin de chat IA](chat-ai-plugin-seatable-6-1.png)

Pour utiliser le plugin, vous devez enregistrer un **token API pour l'un des LLMs** supportés dans les [paramètres]({{< relref "help/ai/ai-chat/setup" >}}) du plugin. Les [modèles supportés]({{< relref "help/ai/ai-chat/supported-models" >}}) incluent ceux d'Anthropic, OpenAI et Mistral. D'autres modèles seront ajoutés prochainement.

{{< warning headline="Stade bêta" >}}
Le plugin de Chat IA est en phase bêta. Nous vous invitons à partager votre expérience avec nous sur le [Forum SeaTable](https://forum.seatable.com/t/we-need-your-feedback-ai-chat-for-seatable/7265).
{{< /warning >}}

## Et plus encore

- Les [formulaires]({{< relref "help/base-editor/webformulare/webformulare" >}}), qu'ils soient classiques ou dans des apps, peuvent désormais être **multi-pages**. Cela améliore sensiblement la clarté dès qu'il y a beaucoup de champs en jeu.

- Les [colonnes d'e-mails]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) permettent de stocker des adresses e-mail au format "nom d'affichage < mail@example.com >". L'envoi d'e-mails à de telles adresses échouait jusqu'à présent, que ce soit dans les règles d'automatisation ou les boutons. Ceci est de l'histoire ancienne avec SeaTable 6.1.

- La nouvelle [action d'automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) **archivage** permet d'automatiser le déplacement des enregistrements du Base Editor vers le [backend Big Data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). L'action est proposée pour les deux déclencheurs périodiques.

## Annulations

Avec SeaTable 6.2, deux fonctions sont supprimées de SeaTable.

1. La fonction de **synchronisation du courrier électronique via IMAP** sera supprimée de SeaTable à partir de la version 6.2. Nous invitons les utilisateurs concernés à recréer la synchronisation via l'une des plateformes d'automatisation prises en charge – Make, n8n ou Zapier.
2. SeaTable 6.2 met également fin au support des applications basées sur le [constructeur d'applications de galerie ou de requête de données]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) de SeaTable version 4.3 et antérieures. Nous vous recommandons de migrer ces applications vers l' [Universal App Builder]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}), qui offre beaucoup plus de possibilités.

La sortie de SeaTable 6.2 est prévue pour mi/fin mai 2026.