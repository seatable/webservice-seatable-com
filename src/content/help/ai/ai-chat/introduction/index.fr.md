---
title: "Qu'est-ce que le plugin de chat IA ?"
description: "Le plugin de chat IA vous permet de dialoguer directement avec vos données dans SeaTable. Posez des questions en langage naturel et l'IA répond avec vos données réelles."
weight: 1
url: '/fr/aide/plugin-chat-ia-dans-seatable'
seo:
    title: 'Plugin de chat IA dans SeaTable : dialoguez avec vos données'
    description: 'Le plugin de chat IA dans SeaTable permet une conversation naturelle avec vos données. Posez des questions, analysez et modifiez vos données, directement dans votre base.'
star: true
---

Le plugin de chat IA (bêta) est une nouvelle extension de SeaTable (à partir de la version 6.1) qui vous permet d'utiliser un chat assisté par IA directement dans votre base. Posez des questions en langage naturel et l'IA répond sur la base de vos données réelles. Vous n'avez besoin d'aucun logiciel externe, d'aucun assistant IA séparé et d'aucune configuration technique. Le chat fonctionne directement dans SeaTable.

## Comment fonctionne le plugin de chat IA ?

Le plugin repose sur le **Model Context Protocol (MCP)**, le même standard ouvert qu'utilisent également les [agents IA]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}). En arrière-plan, le chat accède à vos données via le serveur MCP de SeaTable, lit les tableaux, les colonnes et les entrées, et vous fournit des réponses précises.

La différence fondamentale avec les agents IA : vous n'avez pas besoin d'installer une application externe comme Claude Desktop ou Cursor. Le chat est disponible directement sous forme de plugin dans SeaTable. Vous ouvrez le plugin, posez votre question et recevez la réponse, le tout au sein de votre base.

## Que peut faire le plugin de chat IA ?

Le chatbot peut aussi bien **lire** que **modifier** vos données. Vous pouvez par exemple :

- **Interroger des données** : « Quels projets ont une échéance dans les 7 prochains jours ? »
- **Créer des analyses** : « Comment se répartissent les tickets d'assistance par catégorie ? »
- **Créer des entrées** : « Crée un nouveau contact avec le nom Müller GmbH. »
- **Modifier des données** : « Passe le statut de toutes les tâches terminées à "Archivé". »

## Modèles IA pris en charge

Pour le plugin de chat IA, vous apportez votre propre clé API. Vous pouvez choisir parmi les fournisseurs et modèles suivants :

| Fournisseur | Modèles |
|---|---|
| **Anthropic (Claude)** | Haiku, Sonnet |
| **OpenAI** | GPT-4o, GPT-4o mini |
| **Mistral** | Large, Small |

## Trois fonctions IA dans SeaTable

SeaTable propose trois fonctions IA différentes qui se distinguent fondamentalement par leur mode de fonctionnement :

| | Automatisations IA | Agents IA | Plugin de chat IA |
|---|---|---|---|
| **Disponible depuis** | Version 6.0 | Version 6.0 | Version 6.1 (bêta) |
| **Déclencheur** | Automatique (règle/événement) | Manuel (votre question) | Manuel (votre question) |
| **Interaction** | Aucune, fonctionne en arrière-plan | Dialogue dans l'outil IA externe | Dialogue directement dans SeaTable |
| **Utilisation typique** | Catégoriser, résumer, extraire | Analyses ad hoc, tâches complexes | Questions rapides, modifier des données |
| **Modèle IA** | Serveur IA propre à SeaTable (UE) | Fournisseur externe | Fournisseur externe (clé API propre) |
| **Logiciel externe nécessaire ?** | Non | Oui (p. ex. Claude Desktop, Cursor) | Non |

Les [automatisations IA]({{< relref "help/ai/ai-automations/introduction" >}}) conviennent aux tâches récurrentes qui doivent s'exécuter en arrière-plan selon des règles. Les [agents IA]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}) offrent une flexibilité maximale via des clients MCP externes. Le **plugin de chat IA** comble l'écart entre les deux : une utilisation interactive de l'IA sans logiciel externe, directement là où se trouvent vos données.

## Statut bêta

Le plugin de chat IA est actuellement en phase bêta. Les fonctionnalités et l'interface utilisateur peuvent encore évoluer dans les versions à venir.
