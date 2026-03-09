---
title: "Que sont les automatisations IA ?"
description: "Les automatisations IA traitent les données de votre base automatiquement — de la catégorisation au résumé."
weight: 1
url: '/fr/aide/automatisations-ia-dans-seatable'
seo:
    title: 'Automatisations IA dans SeaTable : traiter les données automatiquement'
    description: 'Les automatisations IA de SeaTable catégorisent, traduisent et résument vos données automatiquement — conformément au RGPD sur des serveurs en Allemagne.'
star: true
---

Depuis la version 6.0, SeaTable propose des actions d'automatisation basées sur l'IA qui peuvent traiter vos données automatiquement. Résumer des textes, catégoriser des demandes de support, extraire des données de factures ou traduire du contenu — tout cela se passe directement dans votre base, déclenché par les règles d'automatisation que vous connaissez déjà de SeaTable. Aucune plateforme IA externe nécessaire, aucun suivi manuel.

{{< youtube A1_LWaFWveM >}}

## Comment fonctionnent les automatisations IA ?

Les automatisations IA sont des actions au sein du système d'automatisation de SeaTable. Elles suivent le même principe que toutes les autres automatisations : un **déclencheur** initie une ou plusieurs **actions**. La différence est que les actions IA utilisent un modèle de langage pour comprendre et traiter le contenu.

Un flux de travail typique ressemble à ceci :

1. Une nouvelle entrée est créée dans une table (déclencheur).
2. Une action IA lit le contenu d'une colonne spécifique — par exemple le texte d'une demande de support.
3. Le modèle de langage analyse le texte et écrit le résultat dans une autre colonne — par exemple la catégorie « Problème technique » ou un résumé en trois phrases.

Cela se passe entièrement automatiquement en arrière-plan. Vous n'avez pas besoin d'intervenir ni de formuler de questions — l'IA travaille selon les règles et les spécifications que vous avez définies dans l'automatisation.

## Que peut automatiser l'IA ?

Dans SeaTable, vous créez une automatisation avec l'action Run AI et choisissez l'une des cinq fonctions disponibles :

- **Summarize** : Les textes longs, rapports ou notes sont automatiquement condensés à l'essentiel. Utile lorsqu'une colonne contient des descriptions détaillées et que vous avez besoin d'un bref résumé dans une autre colonne.
- **Classify** : Les textes entrants sont analysés et attribués à une catégorie. Exemple typique : les demandes de support sont automatiquement classées comme « Technique », « Facturation » ou « Général » et stockées dans une colonne de sélection unique.
- **OCR** : Le texte est reconnu et extrait d'images ou de documents numérisés — par exemple à partir d'une photo de carte de visite ou d'un bon de livraison numérisé.
- **Extract** : Des informations spécifiques sont extraites de texte non structuré — par exemple le numéro de facture, la date et le montant d'une facture.
- **Custom** : Pour tous les cas qui ne correspondent pas aux quatre fonctions standard, vous définissez votre propre prompt. Cela vous permet de faire traduire des textes par l'IA, de rédiger des suggestions de réponse ou d'évaluer du contenu selon vos propres critères.

## Automatisations IA vs. agents IA

SeaTable propose deux façons de faire travailler l'IA avec vos données. Les deux se complètent mais fonctionnent de manière fondamentalement différente :

**Les automatisations IA** s'exécutent automatiquement en arrière-plan, déclenchées par des règles. Elles conviennent aux tâches récurrentes qui doivent se dérouler de la même manière pour chaque nouvelle entrée — par exemple catégoriser chaque demande de support entrante ou résumer chaque nouvelle note.

**Les agents IA** travaillent de manière interactive. Vous posez une question, l'agent répond. Cela convient aux analyses ponctuelles, aux requêtes flexibles et aux tâches uniques — par exemple « Quels clients n'ont eu aucun chiffre d'affaires ce mois-ci ? »

| | Automatisations IA | Agents IA |
|---|---|---|
| **Déclencheur** | Automatique (règle/événement) | Manuel (votre question) |
| **Interaction** | Aucune — s'exécute en arrière-plan | Dialogue en langage naturel |
| **Utilisation typique** | Catégoriser, résumer, extraire | Interroger, analyser, modifier |
| **Modèle IA** | Serveur IA propre à SeaTable (UE) | Fournisseur externe (par ex. Anthropic) |
| **Traitement des données** | Entièrement dans l'UE | Les données sont transmises au fournisseur d'IA |

Pour en savoir plus sur les agents IA, consultez l'article [Que sont les agents IA ?]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}).

## Protection des données : IA made in Europe

Un avantage clé des automatisations IA par rapport aux services IA externes : **vos données ne quittent pas l'UE.** SeaTable exploite son propre serveur IA fonctionnant avec le modèle open source Gemma-3-12B sur une infrastructure GPU chez Hetzner en Allemagne.

Concrètement, cela signifie :

- Vos données ne sont pas transmises à OpenAI, Google ou d'autres fournisseurs américains.
- Aucun entraînement n'a lieu avec vos données — le modèle est pré-entraîné et n'apprend pas de vos entrées.
- Le traitement est conforme au RGPD et soumis exclusivement au droit européen.

Pour les organisations qui travaillent avec des données personnelles, des documents confidentiels ou des informations commerciales sensibles, c'est une différence décisive par rapport aux solutions IA où les données transitent par les États-Unis.

## Disponibilité

Les automatisations IA sont disponibles à partir de SeaTable version 6.0. Les clients Enterprise peuvent utiliser les fonctionnalités sans coût supplémentaire. Un quota limité sera disponible pour les plans Free et Plus à partir de la version 6.1.

## Prochaines étapes

- Configurer les automatisations IA — guide étape par étape