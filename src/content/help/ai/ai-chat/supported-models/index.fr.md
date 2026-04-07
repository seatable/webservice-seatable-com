---
title: 'Modèles IA pris en charge'
description: "Le plugin de chat IA prend en charge des modèles d'Anthropic, OpenAI et Mistral. Découvrez quel modèle convient le mieux à votre cas d'utilisation."
weight: 3
url: '/fr/aide/plugin-chat-ia-modeles-pris-en-charge'
seo:
    title: 'Modèles IA pris en charge dans le plugin de chat SeaTable'
    description: "Aperçu des modèles IA pris en charge dans le plugin de chat SeaTable : Claude, GPT-4o, Mistral. Comparaison, recommandations et coûts."
---

Le plugin de chat IA de SeaTable prend en charge les modèles de langage de trois fournisseurs : **Anthropic**, **OpenAI** et **Mistral**. Vous choisissez vous-même le modèle que vous souhaitez utiliser et apportez votre propre clé API. Les coûts de tokens sont facturés directement par le fournisseur concerné, et non par SeaTable.

## Aperçu des modèles

Chaque fournisseur propose deux modèles : un modèle rapide et économique pour les tâches simples, et un modèle plus performant pour les analyses exigeantes.

| Fournisseur | Modèle | Points forts | Tendance de coût |
|---|---|---|---|
| **Anthropic** | Claude Haiku | Rapide, efficace, adapté aux requêtes simples | économique |
| **Anthropic** | Claude Sonnet | Performant, précis pour les analyses complexes | moyen |
| **OpenAI** | GPT-4o mini | Rapide, économique, polyvalent | économique |
| **OpenAI** | GPT-4o | Très performant, haute qualité de réponse | plus élevé |
| **Mistral** | Mistral Small | Rapide, économique, bonnes performances de base | économique |
| **Mistral** | Mistral Large | Performant, adapté aux tâches complexes | plus élevé |

## Configurer la clé API

Pour utiliser un modèle dans le plugin de chat IA, vous avez besoin d'une clé API du fournisseur correspondant. Vous la créez directement sur le site du fournisseur :

- **Anthropic** : Créez une clé API sur [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI** : Créez une clé API sur [platform.openai.com](https://platform.openai.com/).
- **Mistral** : Créez une clé API sur [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

Chez les trois fournisseurs, vous devez enregistrer un moyen de paiement. Les coûts dépendent du nombre de tokens traités et sont facturés directement par le fournisseur.

## Recommandations par cas d'utilisation

### Requêtes simples et réponses rapides

Pour rechercher des valeurs individuelles, obtenir de courts résumés ou poser des questions de filtrage simples, les modèles économiques conviennent parfaitement : **Claude Haiku**, **GPT-4o mini** ou **Mistral Small**. Ils fournissent des réponses rapides à faible coût.

### Analyses complexes et évaluations de données

Si vous souhaitez analyser des jeux de données volumineux, identifier des tendances ou effectuer des calculs en plusieurs étapes, optez pour **Claude Sonnet**, **GPT-4o** ou **Mistral Large**. Ces modèles fournissent des résultats plus précis pour les tâches exigeantes.

### Rédaction de textes

Pour rédiger des e-mails, des rapports ou des descriptions à partir de vos données, **Claude Sonnet** ou **GPT-4o** sont recommandés. Ces deux modèles produisent des textes de haute qualité linguistique.

## Coûts et facturation

Tous les coûts de tokens sont facturés directement entre vous et le fournisseur IA concerné. SeaTable ne facture aucun frais supplémentaire pour l'utilisation du plugin de chat IA. Les tarifs exacts par token sont disponibles sur la page de tarification du fournisseur respectif.
