---
title: 'Configurer le plugin de chat IA'
description: 'Découvrez comment installer et configurer le plugin de chat IA dans votre base SeaTable.'
weight: 2
url: '/fr/aide/configurer-plugin-chat-ia'
seo:
    title: 'Configurer le plugin de chat IA : guide étape par étape'
    description: 'Installez le plugin de chat IA dans votre base SeaTable, saisissez votre clé API et lancez votre première conversation avec vos données.'
---

Le plugin de chat IA vous permet de dialoguer directement avec vos données dans SeaTable. Dans ce guide, vous apprendrez comment installer le plugin, enregistrer une clé API et lancer votre première conversation. Pour un aperçu général du plugin, consultez l'[article d'introduction]({{< relref "help/ai/ai-chat/introduction" >}}).

{{< warning headline="Version bêta" text="Le plugin de chat IA est disponible depuis SeaTable 6.1 en version bêta. Les fonctionnalités et l'interface peuvent encore évoluer." />}}

## Prérequis

- Un compte SeaTable avec accès à au moins une base
- Une **clé API** d'un des fournisseurs IA pris en charge :
  - [Anthropic](https://console.anthropic.com/) (Claude)
  - [OpenAI](https://platform.openai.com/) (GPT)
  - [Mistral](https://console.mistral.ai/) (Mistral)

## Étape 1 : Installer le plugin dans votre base

1. Ouvrez la base dans laquelle vous souhaitez utiliser le plugin de chat IA.
2. Cliquez sur **Plugins** dans l'en-tête de la base.
3. Recherchez **AI Chat** dans le gestionnaire de plugins et cliquez sur **Ajouter**.

Le plugin apparaît alors dans votre barre de plugins et peut être ouvert à tout moment.

![Le plugin AI Chat installé dans l'en-tête de la base](images/ai-chat-plugin-installed.png)

## Étape 2 : Sélectionner le modèle IA et enregistrer la clé API

1. Ouvrez le plugin de chat IA.
2. Sélectionnez le modèle souhaité parmi l'un des trois fournisseurs IA (Anthropic, OpenAI ou Mistral). Les modèles plus performants fournissent généralement de meilleurs résultats, mais entraînent des coûts plus élevés par requête.
3. Saisissez votre **clé API** dans le champ prévu à cet effet.

![Sélectionner le modèle IA et saisir la clé API](images/ai-model-and-api-key.png)

{{< warning headline="Remarque" text="Pendant la phase bêta, la clé API est stockée dans la base. Tous les utilisateurs de la base partagent la même clé API. Cependant, l'historique des conversations est individuel et n'est pas partagé entre les utilisateurs." />}}

## Étape 3 : Lancer la première conversation

Saisissez votre première question dans le champ de saisie et appuyez sur **Entrée**.

Le plugin analyse la structure et les données de votre base et répond à votre question dans la fenêtre de chat.

## Conseils pour bien démarrer

Commencez par une question simple pour tester la connexion et vous familiariser avec le plugin. Voici de bonnes premières questions :

- « Quels tableaux y a-t-il dans ma base ? »
- « Combien d'entrées contient le tableau [nom du tableau] ? »
- « Résume les données du tableau [nom du tableau]. »

Plus votre question est formulée avec précision, plus la réponse sera exacte. Dans la mesure du possible, indiquez le nom exact du tableau ou de la colonne concerné par votre question.
