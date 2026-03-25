---
title: 'Connecter SeaTable avec Claude Code'
description: 'Connectez Claude Code à votre base SeaTable via le serveur MCP — expliqué étape par étape.'
weight: 3
url: '/fr/aide/connecter-agent-ia-avec-claude-code'
seo:
    title: 'Connecter SeaTable avec Claude Code — Configuration en 5 minutes'
    description: 'Comment connecter Claude Code à votre base SeaTable via le serveur MCP : créer un jeton API, ajouter le serveur MCP via CLI et poser votre première question.'
---

Dans ce guide, vous allez connecter Claude Code à votre base SeaTable. Une fois la configuration terminée, vous pourrez poser des questions à Claude sur vos données et lui faire modifier des entrées directement depuis le terminal. La configuration prend environ cinq minutes.

## Prérequis

- Un compte SeaTable Cloud avec au moins une base
- Claude Code (installable via `npm install -g @anthropic-ai/claude-code`, détails sur [docs.anthropic.com](https://code.claude.com/docs/en/overview))
- Un compte Anthropic (nécessaire pour utiliser Claude)

## Étape 1 : Créer un jeton API dans SeaTable

Le jeton API donne à Claude l'accès à une base spécifique. Vous décidez si Claude peut uniquement lire ou également écrire des données.
Pour savoir comment créer un jeton API, consultez l'article [Créer un jeton API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Conservez votre jeton en sécurité" >}}

Un jeton API est valable indéfiniment et doit être traité comme un mot de passe. Si vous le perdez ou s'il est accidentellement exposé, vous pouvez supprimer le jeton API à tout moment et en créer un nouveau.

{{< /warning >}}

## Étape 2 : Ajouter le serveur MCP via CLI

Claude Code se configure via la ligne de commande. Ouvrez un terminal et exécutez la commande suivante :

```bash
claude mcp add seatable \
  --transport http \
  https://mcp.seatable.com/mcp \
  -H "Authorization: Bearer INSEREZ-VOTRE-JETON-API-ICI"
```

Remplacez `INSEREZ-VOTRE-JETON-API-ICI` par le jeton de l'étape 1.

Vous pouvez connecter plusieurs bases en même temps. Exécutez la commande à nouveau pour chaque base en utilisant un nom unique, par exemple `seatable-crm` et `seatable-projets` au lieu de `seatable`.

## Étape 3 : Vérifier la connexion

Lancez Claude Code et saisissez la commande `/mcp`. Tous les serveurs MCP configurés s'affichent avec leur statut. Si la connexion est réussie, vous verrez **Status: connected** et **Auth: authenticated**.

![Connexion réussie au serveur MCP SeaTable dans Claude Code](images/claude-code-connected-to-mcp-seatable-com.png)

Depuis le menu `/mcp`, vous pouvez également effectuer d'autres actions, comme consulter les outils disponibles, rétablir la connexion (**Reconnect**) ou désactiver le serveur.

Posez maintenant une première question de test :

> *« Quelles tables contient ma base ? »*

Claude interrogera alors la structure des tables via le serveur MCP et listera toutes les tables avec leurs colonnes. Si cela fonctionne, la connexion est établie.

## Poser vos premières questions

Vous pouvez maintenant poser des questions à Claude sur vos données comme si vous parliez à un collègue. Voici quelques exemples à essayer :

- *« Combien d'entrées contient la table Contacts ? »*
- *« Montre-moi toutes les entrées dont le statut est "Ouvert". »*
- *« Résume les données de la table Chiffre d'affaires par mois. »*

Vos questions doivent se rapporter à des tables et des colonnes qui existent réellement dans votre base. Si vous n'êtes pas sûr, demandez d'abord à Claude la structure de la base. Il connaît vos tables et colonnes et peut vous indiquer ce qui est disponible.

Vous n'avez pas besoin de saisir les noms de tables et de colonnes de manière exacte. Claude reconnaît les petites fautes de frappe et les corrige automatiquement. N'hésitez pas à écrire « Contacts » au lieu de « contacts » ou « Projets » au lieu de « projects ». Claude trouvera la bonne table.

## Prochaines étapes

- [Exemples d'utilisation des agents IA]({{< relref "help/ai/ai-agents/use-cases" >}})
- [Poser de bonnes questions : comment obtenir les meilleures réponses]({{< relref "help/ai/ai-agents/good-questions" >}})
- [Dépannage des agents IA]({{< relref "help/ai/ai-agents/troubleshooting" >}})
- [Autorisations et protection des données pour les agents IA]({{< relref "help/ai/ai-agents/data-security" >}})
