---
title: "Que sont les agents IA ?"
description: "Les agents IA accèdent directement à vos données SeaTable via MCP. Découvrez comment cela fonctionne et ce que vous pouvez en faire."
weight: 1
url: '/fr/aide/que-sont-les-agents-ia'
seo:
    title: "Que sont les agents IA et comment fonctionnent-ils avec SeaTable ?"
    description: "Les agents IA se connectent directement à vos données SeaTable via le serveur MCP. Lisez, écrivez et analysez vos données en langage naturel — aucune compétence en programmation requise."
---

Les assistants IA comme Claude, ChatGPT ou Copilot sont des outils puissants — mais ils ont un problème fondamental : ils ne connaissent pas vos données. Si vous souhaitez poser une question sur vos projets, vos clients ou votre inventaire, vous devez d'abord exporter les données, les coller dans le chat et expliquer à l'IA ce que signifient les colonnes. C'est fastidieux et source d'erreurs.

**Les agents IA résolvent exactement ce problème.** Un agent IA est un assistant IA qui peut accéder directement à vos données via une interface standardisée. Dans SeaTable, cela se fait via le **Model Context Protocol (MCP)** — un standard ouvert soutenu par l'ensemble de l'industrie de l'IA.

## L'essentiel en bref

- Le **serveur MCP officiel de SeaTable** (`https://mcp.seatable.com/mcp`) connecte ChatGPT, Claude Desktop, Claude Code, Cursor et d'autres assistants compatibles MCP à votre base.
- L'accès s'applique par base, en lecture seule ou en lecture et écriture, selon le token.
- L'agent travaille sur les données, pas sur la structure : il ne crée ni ne supprime de tables ou de colonnes.
- Gratuit et open source (licence MIT), pour SeaTable Cloud et les installations auto-hébergées.

## Comment cela fonctionne-t-il ?

Lorsque vous connectez un agent IA à votre base SeaTable, voici ce qui se passe :

1. Vous posez une question en langage naturel, par exemple : *« Quelles tâches sont en retard ? »*
2. L'agent IA reconnaît qu'il a besoin de données de votre base et les interroge via le serveur MCP.
3. Le serveur MCP lit les lignes pertinentes de SeaTable et les renvoie à l'agent.
4. L'agent évalue les données et répond — de manière claire et précise.

Tout cela ne prend que quelques secondes. Vous ne remarquez rien, si ce n'est que vous obtenez une réponse précise.

## Que peut faire un agent IA avec mes données ?

Cela dépend des autorisations que vous accordez. Avec un **token en lecture seule**, l'agent peut interroger, rechercher et analyser vos données. Avec un **token en lecture-écriture**, il peut en plus créer, modifier ou supprimer des entrées — mais uniquement après votre confirmation.

Concrètement, cela signifie :

- **Interroger** : « Montre-moi tous les clients de Berlin avec un chiffre d'affaires supérieur à 5 000 euros. »
- **Analyser** : « Combien de tâches ont été terminées cette semaine ? Regrouper par collaborateur. »
- **Créer** : « Crée une nouvelle entrée dans la table Contacts pour Müller GmbH. »
- **Modifier** : « Mets le statut de toutes les tâches en retard sur 'Escaladé'. »
- **Lier** : « Lie le nouveau contact au projet 'Refonte du site web'. »

L'agent reconnaît automatiquement la structure de votre base — tables, colonnes, types de colonnes — et utilise les formats corrects. Il corrige également les fautes de frappe dans les noms de tables ou de colonnes de manière autonome dans la plupart des cas.

{{< youtube 5T4pWJgfOgc >}}

## Quelle est la différence entre les agents IA et les automatisations IA ?

SeaTable propose également des **automatisations IA** — des actions automatisées qui font appel à l'IA lorsque certains événements se produisent, par exemple pour résumer des textes ou catégoriser des entrées. Celles-ci s'exécutent en arrière-plan selon des règles, sans aucune intervention de votre part.

Les agents IA fonctionnent différemment : ils sont **interactifs**. Vous posez une question, l'agent répond. Vous donnez une instruction, l'agent l'exécute. C'est un dialogue — tout comme avec un collègue qui connaît votre base de données sur le bout des doigts.

| | Automatisations IA | Agents IA |
|---|---|---|
| **Déclencheur** | Automatique (règle/événement) | Manuel (votre question) |
| **Interaction** | Aucune — s'exécute en arrière-plan | Dialogue en langage naturel |
| **Utilisation typique** | Résumer des textes, catégoriser | Interroger, analyser, modifier des données |
| **Configuration** | Configurée dans SeaTable | Via un assistant IA externe (par ex. Claude) |

Les deux approches se complètent : les automatisations pour les tâches récurrentes de routine, les agents pour les questions ponctuelles et l'interaction flexible.

## De quoi ai-je besoin pour commencer ?

- Un **compte SeaTable Cloud** (ou une installation auto-hébergée)
- Un **assistant IA** prenant en charge MCP — par exemple ChatGPT, Claude Desktop, Claude Code ou Cursor
- Un **token API** pour la base à laquelle l'agent doit accéder

La configuration ne prend que quelques minutes. Des guides étape par étape sont disponibles pour [ChatGPT]({{< relref "help/ai/ai-agents/connect-chatgpt" >}}), [Claude Desktop]({{< relref "help/ai/ai-agents/connect-claude-desktop" >}}), [Claude Code]({{< relref "help/ai/ai-agents/connect-claude-code" >}}) et [Cursor]({{< relref "help/ai/ai-agents/connect-cursor" >}}).

## Est-ce sûr ?

L'agent IA n'accède qu'à la base pour laquelle vous avez créé un token API. Pas aux autres bases, pas à votre compte. Via le token, vous contrôlez si l'agent peut uniquement lire ou également écrire.

Important à savoir : lorsque l'agent interroge vos données, les résultats sont transmis au fournisseur d'IA (par exemple Anthropic pour Claude) afin que le modèle de langage puisse les traiter. Les principaux fournisseurs s'engagent à ne pas utiliser les données API pour l'entraînement de leurs modèles. Si vous avez besoin d'un contrôle maximal, vous pouvez auto-héberger SeaTable et le combiner avec un modèle de langage local.

Pour en savoir plus sur la sécurité et les autorisations, consultez l'article « Autorisations et protection des données pour les agents IA ».