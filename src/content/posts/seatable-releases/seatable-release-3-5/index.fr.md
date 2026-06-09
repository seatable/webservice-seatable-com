---
title: "SeaTable 3.5 : Formules dans la première colonne, nouvelles actions d'automatisation et toutes sortes de choses réjouissantes - SeaTable"
description: 'Optez pour des formules en colonne clé, automatisez ajouter lien/process, exécutez actions conditionnelles, gérez lookups ciblés. App Builder universel sans code, couleurs sur mesure, import entre bases – tout pour moderniser votre gestion et workflow.'
date: 2023-04-12
lastmod: '2023-09-04'
author: 'kgr'
url: '/fr/seatable-release-3-5'
color: '#f3fa61'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.5 : formules, automatisation, app'
    description: 'Formule en 1ère colonne, nouveaux automatismes périodiques, boutons/lookups conditionnels, App Builder universel (bêta).'
---

Avril fait ce qu'il veut - mais SeaTable fait ce que vous voulez ! La version 3.5 répond à quelques-uns des souhaits de longue date de nos utilisateurs : la première colonne prend désormais en charge [les formules]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) et l'[automatisation]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) vous permet d'exécuter périodiquement deux actions supplémentaires. L'exécution conditionnelle des [actions des boutons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) et les [lookups]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) conditionnels vous offrent une plus grande flexibilité pour les cas d'application plus exigeants. Nous vous présentons ces améliorations en détail ci-dessous.

Avec cette version, nous publions également un nouvel App Builder en version bêta. L'Universal App Builder permet de construire des applications pour les cas d'utilisation et les groupes d'utilisateurs les plus divers sans aucune connaissance en programmation. Actuellement, notre équipe de développement travaille encore sur les finitions, mais l'avant-goût donne déjà envie d'en savoir plus. Nous attendons vos commentaires avec impatience !

Ce matin, nous avons mis à jour le nuage SeaTable à la version 3.5. Tous les auto-hébergeurs peuvent faire de même : L'image de SeaTable 3.5 est disponible en téléchargement dans le célèbre [dépôtDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Comme toujours, vous trouverez dans le [changelog]({{< relref "pages/changelog" >}}) la liste complète des modifications.

## Formules dans la première colonne

SeaTable 3.5 offre plus de flexibilité dans la première colonne du tableau : Jusqu'à présent, seuls les [types de colonnes]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) Texte, Nombre, Date, Sélection simple et Numéro automatique étaient autorisés. Le [type de colonne Formule]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), désormais également pris en charge, permet de "calculer" sa propre référence de ligne. Comme [la première colonne]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}) d'un tableau ne peut pas être masquée et qu'elle est toujours affichée dans la boîte de dialogue des liens, elle se prête particulièrement bien à cet usage.

Dans l'éditeur de formules, il suffit de saisir la colonne à référencer entre accolades. _par exemple, _{Numéro de produit}** récupère la valeur de la colonne "Numéro de produit". Vous pouvez concaténer plusieurs valeurs de colonne avec **&**. Bien entendu, vous pouvez également utiliser des fonctions de texte comme **left()\*\* pour raccourcir les valeurs. Par exemple, si vous gérez des factures dans un tableau, une référence de ligne composée de la date de la facture, du nom du client et du numéro de facture pourrait ressembler à ceci : _20230412-CustomerZ-INV202302347_.

![SeaTable 3.5 - La première colonne supporte les formules](SeaTable-3.5-FirstColumn.png)

## Deux actions supplémentaires pour les automatisations périodiques

Les [automatismes]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}}) de SeaTable vous facilitent la vie en vous épargnant de nombreux clics manuels. Les automatisations vous permettent donc non seulement de gagner du temps, mais aussi de réduire le nombre d'erreurs humaines. SeaTable dispose de quatre [déclencheurs d'automatisation]({{< relref "help/base-editor/automationen/automations-trigger" >}}) qui vous permettent d'exécuter différentes [actions d'automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) en fonction d'un événement (par exemple, l'ajout d'une nouvelle entrée) ou périodiquement (par exemple, chaque lundi à 10 heures). SeaTable 3.5 rend les automatisations périodiques beaucoup plus performantes grâce à deux actions supplémentaires.

Les actions "Ajouter des liens" et "Exécuter une opération de traitement des données" peuvent désormais être sélectionnées pour le déclencheur périodique en plus des actions "Envoyer une notification", "Envoyer un e-mail", "Ajouter une ligne" et "Exécuter un script Python". Ces deux actions permettent d'automatiser toutes les opérations de traitement des données que vous ne pouviez effectuer que manuellement jusqu'à présent.

Voyez par vous-même tout ce qu'il est possible de faire avec les [opérations de traitement des données dans SeaTable]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}).

## Exécution conditionnelle des actions des boutons

Un [bouton]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) permet d'exécuter une ou plusieurs actions en un seul clic, par exemple [envoyer un e-mail]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) puis modifier la ligne. Il n'était pas possible de lier l'exécution d'une action à une condition. Nous avons comblé cette lacune fonctionnelle avec SeaTable 3.5.

![SeaTable 3.5 - Les actions des boutons peuvent être liées à des règles](SeaTable-3.5-ConditionalExecution.png)

La nouvelle exécution conditionnelle vous permet de définir une règle pour chaque action de bouton. Une règle peut être constituée d'une ou de plusieurs conditions. L'action n'est exécutée que si la règle est remplie lorsque l'on clique sur le bouton. Si une condition ne s'applique pas, SeaTable passe à l'action suivante et affiche un message indiquant l'action non exécutée.

Imaginez que vous souhaitiez envoyer des e-mails à vos clients dans différentes langues. La version anglaise, par exemple, ne doit être envoyée que si l'anglais est défini comme langue du client dans une colonne. Jusqu'à présent, vous aviez besoin d'un bouton séparé pour cela. Grâce à l'exécution conditionnelle, un seul bouton suffit désormais pour autant de langues que vous le souhaitez. Il suffit d'ajouter au bouton autant d'actions "Envoyer un e-mail" que de langues à utiliser et de leur attribuer les règles appropriées. Une fois les règles définies, lorsque vous cliquez sur le bouton, SeaTable n'envoie que l'e-mail dans la langue du client concerné.

Depuis la version 3.5, SeaTable exécute toutes les actions définies de manière strictement séquentielle. Tant qu'une action n'est pas terminée, l'action suivante n'est pas lancée. Cela permet de s'assurer qu'une action qui prend du temps (par exemple la création d'un PDF) est terminée avant qu'une autre action (par exemple l'envoi d'un e-mail auquel le PDF doit être joint) ne démarre.

## Lookups conditionnels dans la colonne Formule pour les liens

Le type de colonne Formule pour les liens permet d'évaluer les entrées liées. Au total, cinq méthodes d'évaluation sont à votre disposition : [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}}), [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}}), [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}}), [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}}) et [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}). La formule Lookup vous permet d'afficher des valeurs supplémentaires de lignes déjà liées dans votre tableau actuel. Vous pouvez ainsi extraire et afficher autant d'informations que vous le souhaitez à partir du tableau lié.

![SeaTable 3.5 - Colonnes de formules de liens supportant les recherches conditionnelles](SeaTable-3.5-ConditionalLookup.png)

Dans SeaTable 3.5, nous avons amélioré la formule de recherche et implémenté une fonction qui existait déjà depuis un certain temps dans les autres formules : une évaluation conditionnelle. Si l'évaluation conditionnelle est activée pour les lookups, seules les valeurs qui remplissent la ou les conditions définies sont affichées. Ainsi, vous obtenez exactement les informations dont vous avez besoin à partir de la table liée.

## Universal App Builder (bêta)

Vous avez toujours voulu construire vos propres applications ? SeaTable fait de ce rêve une réalité : grâce à l'Universal App Builder, vous créez à partir d'une base des applications individuelles pour des groupes d'utilisateurs ayant des besoins d'information différents (par ex. employés, chefs de service, directeurs). Comme backend, vous utilisez simplement la structure et les données dans une base, sur laquelle vous pouvez placer autant de frontaux que vous le souhaitez pour chaque groupe d'utilisateurs.

L'interface utilisateur graphique permet de créer des pages, des tableaux, des formulaires web, des tableaux Kanban, des calendriers et des galeries personnalisés en fonction des groupes d'utilisateurs. Celles-ci fonctionnent comme dans la base, mais avec quelques particularités comme des options d'affichage prédéfinies et immuables.

L'accès se fait par URL (personnalisée) avec ou sans connexion. En définissant un accès ouvert, vous pouvez également permettre à des tiers externes sans compte SeaTable (par ex. clients, partenaires commerciaux) d'accéder à des données via l'application. Actuellement, notre équipe de développement peaufine encore la version bêta, mais la structure de base de l'application universelle est prête. Essayez-la dès maintenant !

## Et bien d'autres choses encore

Pour simplifier le transfert de données d'une base à une autre, SeaTable 3.5 offre désormais la possibilité pratique d'importer des tableaux directement depuis une autre base et de transférer ainsi des données au-delà des frontières de la base.

Pour les options de sélection, les boutons et le formatage conditionnel, SeaTable propose 24 couleurs. Pour répondre aux besoins individuels ou aux exigences de l'identité visuelle, SeaTable 3.5 permet de définir un nombre illimité de couleurs supplémentaires dans chaque base. Les auto-hébergeurs ont en outre l'option de définir globalement des couleurs individuelles dans SeaTable via le fichier de configuration.

![SeaTable 3.5 - Nouvelle mise en page pour les détails des rangées](SeaTable-3.5-RowDetails.png)

La présentation sur une seule colonne des détails des lignes est remplacée dans la nouvelle version par un design sur deux colonnes. La présentation des tableaux avec de nombreuses colonnes est ainsi plus courte et plus claire. Le journal de base, dans lequel vous pouvez suivre toutes les modifications au sein d'une base, a également un nouveau look. Si vous cliquez sur Logs dans l'historique de la base {{< seatable-icon icon="dtable-icon-history" >}}, une fenêtre séparée s'ouvre désormais avec des entrées de logs claires.

Nous avons apporté les modifications les plus importantes à l'interface utilisateur dans les boîtes de dialogue de la colonne des liens. Outre la largeur des colonnes, il est également possible de modifier la taille des boîtes de dialogue. Si vous souhaitez masquer les colonnes non pertinentes, c'est également désormais possible. Comme dans les options d'affichage, la boîte de dialogue "Entrées liées" comporte désormais une option permettant de masquer ainsi que de trier les colonnes.

## Deux nouvelles limites

Comme annoncé dans les [dernières notes de version]({{< relref "posts/seatable-releases/seatable-release-3-4" >}}), SeaTable 3.5 introduit une limite de 100.000 caractères pour les cellules individuelles de type [Texte formaté]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}). Si le texte d'une cellule dépasse 100 000 caractères (ce qui correspond à environ 25 pages A4 de texte), un message d'avertissement s'affiche. Si vous ne raccourcissez pas le texte et fermez l'éditeur, SeaTable n'enregistrera que 100 000 caractères.

Avec la version 3.5 de SeaTable Cloud, nous avons réduit le nombre maximum de lignes renvoyées dans un appel API de 10 000 à 1 000. Veuillez vérifier si cela nécessite des ajustements dans vos intégrations.
