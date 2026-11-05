---
title: 'SeaTable 7.0 : génération de pages par IA, chat IA prêt pour la production et automatisations plus intelligentes'
description: "SeaTable 7.0 est placé sous le signe de l'IA. Décrivez une page en langage naturel et l'App Builder la génère sous forme de page HTML. Le plugin AI Chat sort de la phase bêta et utilise désormais par défaut un modèle hébergé chez Exoscale. Un SDK enrichi pour les pages HTML, des actions d'automatisation nouvelles et améliorées, de nombreuses améliorations de sécurité et l'abandon du générateur d'applications de requête de données complètent cette version."
date: 2026-11-05
author: 'rdb'
url: '/fr/seatable-release-7-0'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 7.0 : Toute la puissance de l’IA au service du No-Code !'
    description: 'SeaTable 7.0 met l’IA à l’honneur : analysez vos bases avec l’IA et utilisez-la pour créer des pages HTML dans vos applications grâce au nouveau SDK HTML.'
register:
    show: false
---

Avec la version 7.0, SeaTable franchit une étape importante en matière d'intelligence artificielle. Deux nouveautés se distinguent : dans l'App Builder, vous pouvez désormais générer des pages HTML avec l'IA, simplement en décrivant ce que la page doit faire et à quoi elle doit ressembler. Et le plugin AI Chat, lancé en version bêta avec SeaTable 6.1, est maintenant prêt pour une utilisation en production. Ces deux fonctionnalités s'appuient sur un modèle d'IA plus performant qui, pour SeaTable Cloud, fonctionne sur l'infrastructure de notre partenaire Exoscale.

Mais SeaTable 7.0 ne se limite pas à l'IA. Le SDK pour les pages HTML, également utilisé par les pages générées par l'IA, bénéficie de quatre améliorations demandées par nos utilisateurs. Les automatisations gagnent deux nouvelles actions pour les enregistrements liés, et deux actions existantes deviennent plus polyvalentes. En coulisses, cette version apporte de nombreuses corrections de bugs et améliorations de sécurité qui répondent à la menace immédiate que représentent les bots dopés à l'IA et les exploits générés automatiquement. Des améliorations plus modestes des formulaires, des statistiques et de l'authentification à deux facteurs complètent la version. Enfin, une fonctionnalité prend sa retraite : il n'est plus possible de créer de nouvelles applications de requête de données, mais les applications existantes continuent de fonctionner.

Ce matin, nous avons mis à jour SeaTable Cloud vers la version 7.0. Nous recommandons à tous les administrateurs de systèmes auto-hébergés d'en faire autant, notamment en raison des améliorations de sécurité. L'image Docker de SeaTable 7.0 est disponible au téléchargement sur [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise/). Comme toujours, vous trouverez la liste complète des modifications dans le [changelog](https://seatable.com/changelog/#release-7).

## Générer des pages HTML avec l'IA

SeaTable 7.0 vous permet de créer des pages HTML directement dans l'App Builder, en dialoguant avec une IA. Vous décrivez en langage naturel ce que la page doit faire et à quoi elle doit ressembler, et l'IA la construit pour vous. Pour cela, l'IA s'appuie sur le SDK de SeaTable pour les pages HTML (nous y revenons dans la section suivante). Une page générée par l'IA peut ainsi être tout aussi performante qu'une page codée à la main.

Rien de plus simple pour commencer : cliquez sur l'icône IA dans le ruban de gauche. Un assistant vous guide dans la configuration : donnez un nom au projet, choisissez un style d'interface, définissez les sources de données et les autorisations de la page, puis décrivez la page souhaitée. L'IA génère alors une première version et l'affiche dans un aperçu. Vous affinez ensuite la page en dialoguant avec l'IA, jusqu'à ce qu'elle fasse exactement ce dont vous avez besoin. Un clic sur « Publier » ajoute la page à votre application SeaTable.

![Générer une page HTML avec l'IA dans SeaTable 7.0](AI-generated_HTML_page.png)

Le chat conserve l'intégralité de la conversation ainsi que chaque version de la page. Vous pouvez donc reprendre là où vous vous étiez arrêté à tout moment, ou revenir à une version antérieure si une modification ne vous convient pas. Les conversations et les pages non publiées sont conservées pendant 365 jours. Et si vous préférez peaufiner une page vous-même, vous pouvez la télécharger et la modifier manuellement.

Curieux de savoir ce qui se passe en coulisses ? Cliquez sur le lien « Raisonnement » dans le chat. Pour chaque étape, il affiche le prompt système, votre saisie et le résultat renvoyé par l'IA. Une section de statistiques indique en outre la durée de l'étape et le nombre de tokens consommés.

![Le raisonnement de l'IA dans le chat IA](Thought_process_AI_chat.png)

Sur SeaTable Cloud, la génération de pages repose sur un puissant modèle open-weights hébergé par notre partenaire d'infrastructure Exoscale, qui exploite également les serveurs de SeaTable Cloud. Vos prompts et les schémas de vos bases ne sont donc traités par aucun autre tiers. Quant aux données stockées dans vos bases, elles ne sont de toute façon jamais transmises au modèle d'IA. Les administrateurs de systèmes auto-hébergés peuvent utiliser un modèle cloud de l'un des grands laboratoires d'IA ou connecter un modèle auto-hébergé de leur choix. SeaTable prend en charge tous les LLM disposant d'un point de terminaison compatible avec OpenAI.

{{< warning headline="Une infrastructure IA plus performante" >}}
Le modèle d'IA utilisé pour la génération de pages HTML est Qwen 3.8 27B, un grand modèle de langage multimodal de 27 milliards de paramètres développé par Alibaba. Il est conçu pour le raisonnement avancé, la programmation, la recherche, le traitement de documents et les tâches complexes en plusieurs étapes, et il est publié sous licence Apache 2.0. Qwen 3.8 27B remplace également le modèle open-weights [Gemma 4 E4B de Google DeepMind](https://seatable.com/seatable-release-6-0/#ai-deployment-without-compromising-on-data-protection), qui alimentait jusqu'ici les actions IA des automatisations de SeaTable.
{{< /warning >}}

## Un SDK enrichi pour les pages HTML

Le SDK SeaTable pour les pages HTML relie vos pages personnalisées aux données de votre base, qu'il s'agisse de pages que vous écrivez vous-même ou de pages générées par l'IA. Pour répondre aux retours de nos utilisateurs, SeaTable 7.0 lui apporte quatre améliorations qui le rendent nettement plus puissant.

Premièrement, le SDK connaît désormais les noms des utilisateurs. Jusqu'à présent, il ne pouvait que lire les données des lignes de la base, sans pouvoir rechercher les noms : les pages n'affichaient donc que des noms d'utilisateur internes tels que `a1b2c3…@auth.local`. Désormais, vos pages montrent en un coup d'œil qui est qui.

Deuxièmement, le SDK identifie l'utilisateur connecté. Auparavant, une page n'avait aucun moyen de savoir qui la consultait. Grâce à la nouvelle méthode `getCurrentUser()`, les pages peuvent filtrer les données en fonction de l'utilisateur actuel, par exemple pour n'afficher à chaque membre de l'équipe que ses propres tâches.

Troisièmement, le SDK propose de nouvelles méthodes pour ajouter ou supprimer des liens individuels dans les colonnes de lien. Jusqu'ici, la méthode `updateRow()` ne permettait de mettre à jour une colonne de lien que dans son ensemble, en remplaçant tous les liens existants. Les nouvelles méthodes permettent d'ajouter facilement une tâche à un projet, d'insérer un article dans un devis ou de désinscrire un participant d'un séminaire, sans toucher aux autres liens.

Quatrièmement, le SDK prend en charge trois nouvelles actions : envoyer un e-mail, envoyer une notification et exécuter un script. Les pages HTML peuvent ainsi envoyer des messages et lancer des scripts d'un simple clic sur un bouton, par exemple pour confirmer une réservation par e-mail directement depuis la page. Les comptes e-mail et les scripts que vous souhaitez utiliser doivent être configurés dans la base.

![Trois nouvelles actions pour les pages HTML: Envoyer un e-mail, envoyer une notification et exécuter un script](Action_permissions_HTML_page.png)

## Le plugin AI Chat prêt pour la production

Le plugin AI Chat a été lancé en version bêta avec [SeaTable 6.1](https://seatable.com/seatable-release-6-1/#chat-with-an-artificial-intelligence). Il vous permet de modifier et d'analyser vos bases en langage naturel : créer des enregistrements, modifier des valeurs, relier des lignes ou analyser des données, en français, en anglais, en allemand et dans d'autres langues. (Les modifications du schéma de la base ne sont pas prises en charge.)

Avec SeaTable 7.0, le plugin sort de la phase bêta. Sur la base des retours de nos utilisateurs, nous avons amélioré à la fois le plugin et le serveur MCP qu'il utilise. Les requêtes sont désormais nettement plus efficaces, ce qui réduit considérablement la consommation de tokens. Nous avons également mis à jour la liste des modèles d'IA cloud pris en charge.

Le plugin est aussi devenu beaucoup plus simple à utiliser. Pendant la phase bêta, vous deviez fournir votre propre jeton d'API pour un LLM pris en charge. Sur SeaTable Cloud, le plugin utilise désormais par défaut notre propre modèle d'IA hébergé chez Exoscale. Les tokens consommés sont convertis en crédits IA et déduits de votre solde : 1 million de tokens d'entrée correspond à 500 crédits IA, et 1 million de tokens de sortie à 1 500 crédits IA. Si vous préférez ne pas utiliser le modèle par défaut, vous pouvez choisir l'un des autres modèles pris en charge des grands laboratoires d'IA.

{{< warning headline="Bientôt disponible pour les systèmes auto-hébergés" >}}
Le plugin AI Chat est actuellement réservé aux clients de SeaTable Cloud et de SeaTable Dedicated. Nous le rendrons disponible pour les systèmes auto-hébergés dans les mois à venir.
{{< /warning >}}

## Des automatisations améliorées

SeaTable 7.0 apporte deux nouvelles actions d'automatisation, rend deux actions existantes plus polyvalentes et enrichit le journal des automatisations.

La première nouvelle action, « Ajouter un enregistrement dans un tableau relié », fonctionne de manière similaire à l'action existante « Ajouter un enregistrement dans un autre tableau » : elle crée un nouvel enregistrement dans un autre tableau. En plus, elle relie ce nouvel enregistrement à l'enregistrement qui a déclenché l'automatisation. La seconde nouvelle action, « Modifier un enregistrement relié dans un autre tableau », complète la première en modifiant des enregistrements reliés existants dans d'autres tableaux. Par exemple, lorsque le statut d'un enregistrement change, tous les enregistrements reliés qui en dépendent peuvent être mis à jour immédiatement. Les deux nouvelles actions sont disponibles avec le déclencheur « Lorsqu'une ligne est mise à jour ».

![Nouvelle action d'automatisation pour les enregistrements reliés dans SeaTable 7.0](New_automated_actions.png)

L'action « Convertir la page en PDF » génère un PDF à partir d'un modèle du plugin Conception de Page et l'enregistre dans une colonne de fichiers. Dans SeaTable 6.x, elle n'était disponible qu'avec le déclencheur planifié. Vous pouvez désormais l'utiliser avec tous les déclencheurs liés à une ligne : « Lorsqu'une ligne est ajoutée », « Lorsqu'une ligne est mise à jour » et « À une heure programmée pour les enregistrements qui correspondent aux conditions ». Cela ouvre la voie à des workflows entièrement automatisés. Par exemple, un client envoie une demande de devis, SeaTable génère le devis (avec ou sans l'aide de l'IA), et le devis est envoyé au client par e-mail.

L'action « Gérer les événements dans Google Agenda » peut désormais aussi supprimer des événements d'un agenda.

Enfin, le journal des automatisations est plus informatif : en plus de l'heure de déclenchement, il enregistre désormais aussi la fin de l'exécution.

## Et bien plus encore

Les formulaires de plusieurs pages peuvent désormais afficher une barre de progression, pour que les répondants voient où ils en sont. En outre, les messages de confirmation après l'envoi prennent désormais en charge le texte enrichi.

Les statistiques des applications SeaTable ont été reconstruites avec D3.js, une bibliothèque JavaScript de visualisation de données puissante et très répandue. Ce changement technique ouvre la voie à des graphiques plus personnalisables à l'avenir. Les statistiques de la base suivront dans la prochaine version mineure.

Lors de la configuration de l'authentification à deux facteurs, SeaTable affiche désormais la clé secrète, afin que vous puissiez l'enregistrer dans votre gestionnaire de mots de passe.

Et une dernière chose : les applications natives SeaTable pour iOS et Android arrivent très bientôt. Les derniers tests sont en cours. Restez à l'écoute !

## Les applications de requête de données tirent leur révérence

Avec SeaTable 7.0, nous avons supprimé le générateur d'applications de requête de données. Il n'est plus possible de créer de nouvelles applications de ce type. Les applications de requête de données existantes ne sont pas concernées et continuent de fonctionner normalement.

Pour vos nouvelles applications, utilisez plutôt les applications universelles. Elles offrent les mêmes fonctionnalités que les applications de requête de données, et bien plus encore. Vous découvrirez comment les créer dans les [pages d'aide consacrées aux applications universelles](https://seatable.com/help/page-types-overview-app-builder/).
