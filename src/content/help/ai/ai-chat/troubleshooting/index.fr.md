---
title: 'Dépannage'
description: 'Solutions aux problèmes courants avec le plugin de chat IA dans SeaTable.'
weight: 6
url: '/fr/aide/plugin-chat-ia-depannage'
seo:
    title: 'Plugin de chat IA : dépannage et problèmes courants'
    description: "Solutions aux problèmes courants du plugin de chat IA : erreurs de clé API, réponses manquantes et problèmes de plugin."
---

Si le plugin de chat IA ne fonctionne pas comme prévu, vous trouverez ici les solutions aux problèmes les plus courants. Pour des informations générales sur la configuration, consultez l'article [Configurer le plugin de chat IA]({{< relref "help/ai/ai-chat/setup" >}}).

## Problèmes de clé API

### Clé API invalide

Si le message d'erreur indique une clé API invalide, vérifiez les points suivants :

- Assurez-vous que la clé a été saisie correctement et qu'elle ne contient pas d'espaces accidentels.
- Vérifiez que la clé API est encore active. Certains fournisseurs désactivent les clés après une certaine période d'inactivité.
- Assurez-vous que le **fournisseur** sélectionné dans les paramètres du plugin correspond à la clé API. Par exemple, une clé OpenAI ne fonctionne pas avec le fournisseur Anthropic.

### Crédit ou quota épuisé

La plupart des fournisseurs IA fonctionnent avec un crédit prépayé. Si aucune réponse n'est plus générée, vérifiez votre crédit dans le tableau de bord du fournisseur concerné :

- [Anthropic Console](https://console.anthropic.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Mistral Console](https://console.mistral.ai/)

## Aucune réponse ou réponses incorrectes

### L'IA ne trouve pas les données

Assurez-vous que les données demandées existent bien dans la base. Indiquez dans votre question le nom exact du tableau et de la colonne afin que l'IA puisse identifier les bonnes données.

### Résultats imprécis ou erronés

Formulez votre question de manière aussi précise que possible. Évitez les formulations vagues et indiquez concrètement quel tableau et quelles colonnes sont pertinents. Pour les tâches complexes, il peut être utile de décomposer la demande en plusieurs étapes simples.

### Délai d'attente dépassé ou absence de réponse

Les requêtes très volumineuses peuvent entraîner un dépassement du délai d'attente. Simplifiez la demande ou limitez-vous à un seul tableau. Notez également que les modèles plus petits comme Haiku, GPT-4o mini ou Mistral Small peuvent atteindre leurs limites pour les tâches complexes en plusieurs étapes.

## Problèmes de plugin

### Le plugin ne s'affiche pas

Vérifiez que le plugin est installé et activé dans le gestionnaire de plugins. Pour cela, ouvrez la section **Plugins** dans l'en-tête de la base et recherchez **AI Chat**.

### Le plugin ne se charge pas

Rechargez la page dans le navigateur. Si le problème persiste, essayez avec un autre navigateur ou videz le cache du navigateur.

### Les paramètres ne sont pas enregistrés

Veillez à confirmer les paramètres avec **Save** après avoir saisi la clé API. Sans enregistrement, les saisies sont perdues à la fermeture de la boîte de dialogue des paramètres.

## Conseils généraux

- Commencez par une question simple comme « Quels tableaux existe-t-il ? » pour vérifier la connexion au fournisseur IA.
- Si l'IA fournit des résultats inattendus, demandez-lui d'expliquer son raisonnement.
- Décomposez les tâches complexes en plusieurs petites étapes pour obtenir de meilleurs résultats.
