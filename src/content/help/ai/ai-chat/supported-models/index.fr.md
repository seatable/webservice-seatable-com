---
title: 'Modèles IA pris en charge'
description: "Le plugin de chat IA prend en charge des modèles d'Anthropic, OpenAI et Mistral. Découvrez quel modèle convient le mieux à votre cas d'utilisation."
weight: 3
url: '/fr/aide/plugin-chat-ia-modeles-pris-en-charge'
seo:
    title: 'Modèles IA pris en charge dans le plugin de chat SeaTable'
    description: "Aperçu des modèles IA pris en charge dans le plugin de chat SeaTable : Claude, GPT, Mistral. Comparaison, recommandations et coûts."
---

Le plugin de chat IA utilise par défaut **SeaTable AI**, qui est déjà installée. Il prend également en charge les modèles de langage de trois fournisseurs externes : **Anthropic**, **OpenAI** et **Mistral**. Vous choisissez vous-même le modèle que vous souhaitez utiliser. Les coûts de tokens sont soit directement imputés à votre abonnement SeaTable, soit payés au fournisseur externe de votre modèle.

## SeaTable AI

SeaTable AI, qui est préinstallée, repose sur **Qwen 3.8 27B**, un modèle open-weights de 27 milliards de paramètres développé par Alibaba. Le modèle d'IA est hébergé dans des centres de données allemands d'Exoscale – le même fournisseur qui met également à disposition les serveurs de SeaTable Cloud. Il est conçu pour le raisonnement avancé, la programmation, la recherche, le traitement de documents et les tâches complexes en plusieurs étapes, et il est publié sous licence Apache 2.0.

Vous pouvez en outre apporter votre propre **clé API** pour le plugin de chat IA afin de connecter un **modèle d'IA cloud externe**.

## Aperçu des modèles des fournisseurs externes

Chaque fournisseur propose deux modèles : un modèle rapide et économique pour les tâches simples, et un modèle plus performant pour les analyses exigeantes.

| Fournisseur | Modèle | Points forts | Tendance de coût |
|---|---|---|---|
| **Anthropic** | Claude Haiku | rapide, efficace, adapté aux requêtes simples | économique |
| **Anthropic** | Claude Sonnet | performant, précis pour les analyses complexes | moyen |
| **OpenAI** | GPT-6 Luna | rapide, économique, polyvalent | économique |
| **OpenAI** | GPT-6.1 Sol | très performant, haute qualité de réponse | plus élevé |
| **Mistral** | Mistral Small | rapide, économique, bonnes performances de base | économique |
| **Mistral** | Mistral Large | performant, adapté aux tâches complexes | plus élevé |

## Configurer la clé API

Pour utiliser un modèle externe dans le plugin de chat IA, vous avez besoin d'une **clé API** du fournisseur correspondant. Vous la créez directement sur le site du fournisseur :

- **Anthropic** : Créez une clé API sur [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI** : Créez une clé API sur [platform.openai.com](https://platform.openai.com/).
- **Mistral** : Créez une clé API sur [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

Chez les trois fournisseurs, vous devez enregistrer un **moyen de paiement**. Les coûts dépendent du nombre de tokens consommés et sont facturés directement par le fournisseur.

## Recommandations par cas d'utilisation

### Requêtes simples et réponses rapides

Pour rechercher des valeurs individuelles, obtenir de courts résumés ou poser des questions de filtrage simples, les modèles économiques conviennent parfaitement : **Claude Haiku**, **GPT-6 Luna** ou **Mistral Small**. Ils fournissent des réponses rapides à faible coût.

### Analyses complexes et évaluations de données

Si vous souhaitez analyser des jeux de données volumineux, identifier des tendances ou effectuer des calculs en plusieurs étapes, optez pour **Claude Sonnet**, **GPT-6.1 Sol** ou **Mistral Large**. Ces modèles fournissent des résultats plus précis pour les tâches exigeantes.

### Rédaction de textes

Pour rédiger des e-mails, des rapports ou des descriptions à partir de vos données, **Claude Sonnet** ou **GPT-6.1** sont recommandés. Ces deux modèles produisent des textes de haute qualité linguistique.

## Coûts et facturation

### Avec SeaTable AI

Les tokens consommés par l'IA sont convertis en **crédits IA** et déduits de votre solde : 1 million de tokens d'entrée correspond à 500 crédits IA et 1 million de tokens de sortie à 1 500 crédits IA.

Le nombre de crédits IA dont vous disposez dépend de l'[abonnement SeaTable]({{< relref "pages/prices" >}}) de votre équipe. Avec SeaTable Plus, vous bénéficiez chaque mois de **50 crédits IA par utilisateur** et avec SeaTable Enterprise, de **500 crédits IA par utilisateur**.

Vous pouvez consulter à tout moment votre solde restant et votre consommation sur la **barre située dans le panneau latéral gauche** du plugin de chat IA.

![Crédits IA consommés et restants avec SeaTable AI](images/seatable-ai-credits.png)

### Avec des modèles IA externes

Tous les coûts de tokens sont facturés directement entre vous et le fournisseur IA concerné. SeaTable ne facture aucun frais supplémentaire pour l'utilisation du plugin de chat IA. Les tarifs exacts par token sont disponibles sur la page de tarification du fournisseur respectif.
