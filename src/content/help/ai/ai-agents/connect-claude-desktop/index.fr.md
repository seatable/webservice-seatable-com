---
title: 'Connecter SeaTable avec Claude Desktop'
description: 'Connectez Claude Desktop à votre base SeaTable via le serveur MCP — expliqué étape par étape.'
weight: 2
url: '/fr/aide/connecter-agent-ia-avec-claude-desktop'
seo:
    title: 'Connecter SeaTable avec Claude Desktop — Configuration en 5 minutes'
    description: 'Comment connecter Claude Desktop à votre base SeaTable via le serveur MCP : créer un jeton API, ajouter la configuration et poser votre première question.'
---

Dans ce guide, vous allez connecter Claude Desktop à votre base SeaTable. Une fois la configuration terminée, vous pourrez poser des questions à Claude sur vos données et lui faire modifier des entrées directement depuis le chat. La configuration prend environ cinq minutes.

## Prérequis

- Un compte SeaTable Cloud avec au moins une base
- Claude Desktop (disponible gratuitement sur [claude.ai/download](https://claude.ai/download/))
- Un compte Anthropic (nécessaire pour utiliser Claude)

{{< warning headline="L'abonnement gratuit suffit, mais nécessite une configuration spéciale" >}}

Le compte gratuit d'Anthropic prend actuellement en charge les connexions aux serveurs MCP personnalisés, mais ceux-ci doivent être configurés manuellement via des fichiers de configuration.

{{< /warning >}}

## Étape 1 : Créer un jeton API dans SeaTable

Le jeton API donne à Claude l'accès à une base spécifique. Vous décidez si Claude peut uniquement lire ou également écrire des données.
Pour savoir comment créer un jeton API, consultez l'article [Créer un jeton API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Conservez votre jeton en sécurité" >}}

Un jeton API est valable indéfiniment et doit être traité comme un mot de passe. Si vous le perdez ou s'il est accidentellement exposé, vous pouvez supprimer le jeton API à tout moment et en créer un nouveau.

{{< /warning >}}

## Étape 2 : Configurer Claude Desktop

Claude Desktop utilise un fichier de configuration JSON pour intégrer les serveurs MCP.

1. Ouvrez Claude Desktop.
2. Allez dans **Settings** → **Developer**

![Ajout d'un serveur MCP personnalisé dans Claude Desktop](images/claude-add-custom-mcp.png)

3. Le fichier `claude_desktop_config.json` s'ouvre dans votre éditeur de texte.
4. Ajoutez la configuration suivante :

```json
{
  "mcpServers": {
    "seatable": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx-cli.js",
        "mcp-remote",
        "https://mcp.seatable.com/mcp",
        "--header",
        "Authorization: Bearer INSEREZ-VOTRE-JETON-API-ICI"
      ]
    }
  }
}
```

5. Remplacez `INSEREZ-VOTRE-JETON-API-ICI` par le jeton de l'étape 1.
6. Enregistrez le fichier et redémarrez Claude Desktop.

Vous pouvez connecter plusieurs bases en même temps. Créez une entrée séparée sous `mcpServers` pour chaque base avec un nom unique, par exemple `seatable-crm` et `seatable-projets`.

## Étape 3 : Vérifier la connexion

Après le redémarrage, vous verrez la connexion à **SeaTable** sous `Tools` dans Claude Desktop. Cela indique que le serveur MCP est connecté. Cliquez dessus pour voir les outils disponibles — vous devriez trouver des outils SeaTable tels que `list_tables`, `list_rows` ou `query_sql`.

Vous pouvez également vérifier le statut de la connexion dans les paramètres.

![Statut de la connexion au serveur MCP](images/claude-mcp-connected.png)

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
