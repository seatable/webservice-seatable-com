---
title: 'Résumer des textes (Summarize)'
description: 'Avec la fonction IA Summarize, résumez automatiquement de longs textes dans votre base SeaTable.'
weight: 3
url: '/fr/aide/automatisation-ia-resumer-textes'
seo:
    title: 'Automatisation IA : Résumer automatiquement des textes dans SeaTable'
    description: 'Comment résumer automatiquement des textes dans SeaTable : configurer une automatisation IA avec la fonction Summarize — contrôler la longueur, le ton et la langue via le prompt.'
---

La fonction IA **Summarize** résume automatiquement le contenu d'une ou de plusieurs colonnes. C'est particulièrement utile lorsque votre tableau contient de longues descriptions, des rapports ou des notes et que vous avez besoin d'un résumé compact dans une colonne supplémentaire.

## Cas d'utilisation typiques

- **Demandes de support** : Condenser les descriptions détaillées de problèmes clients en deux ou trois phrases.
- **Notes de réunion** : Résumer des procès-verbaux complets en un court résumé.
- **Avis sur les produits** : Réduire les longues critiques aux points essentiels.
- **Candidatures** : Résumer les lettres de motivation ou les CV sous forme abrégée.

## Prérequis

- Un tableau avec au moins une **colonne Texte** ou **colonne Texte formaté** servant d'entrée.
- Une **colonne Texte** ou **colonne Texte formaté** pour le résultat (le résumé).

## Guide étape par étape

### 1. Créer une automatisation et choisir un déclencheur

Créez une nouvelle règle d'automatisation comme décrit dans l'article [Configurer une automatisation IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Choisissez un déclencheur approprié — par exemple **Lorsqu'une ligne est ajoutée**, afin que chaque nouvelle entrée soit automatiquement résumée.

### 2. Ajouter l'action « Appeler l'IA »

Cliquez sur **Ajouter une action** et sélectionnez **Appeler l'IA**.

### 3. Sélectionner la fonction « Summarize »

Dans les paramètres de l'action, choisissez :

- **Tableau** : Le tableau dans lequel l'IA doit travailler.
- **Fonction** : **Summarize**

![Paramètres de l'action pour la fonction IA Summarize](images/ai-automation-summarize.png)

### 4. Définir les colonnes d'entrée

Sélectionnez une ou plusieurs colonnes dont le contenu doit être résumé. Si vous sélectionnez plusieurs colonnes, l'IA combine le contenu de toutes les colonnes en un seul résumé.

### 5. Personnaliser le prompt

Dans le champ **Summary prompt**, vous pouvez contrôler l'apparence du résumé. Si vous laissez le champ vide, l'IA crée un résumé standard. Avec un prompt, vous pouvez influencer la longueur, le ton, le format et la langue.

**Exemples de prompts :**

| Prompt | Résultat |
|---|---|
| *Le résumé doit contenir au maximum 50 mots.* | Résumé court et concis |
| *Résume le texte en trois points.* | Vue d'ensemble en points |
| *Crée un résumé formel en français.* | Ton formel, langue française |
| *Résume l'essentiel en une phrase.* | Résumé en une phrase |

{{< warning headline="Astuce" text="Rédigez le prompt dans la langue dans laquelle vous attendez le résultat. Un prompt en français produira généralement un résumé en français." />}}

### 6. Définir la colonne de résultat

Sélectionnez la colonne dans laquelle le résumé doit être écrit. Celle-ci doit être de type **Texte** ou **Texte formaté**.

### 7. Enregistrer et tester

Cliquez sur **Enregistrer**. Testez l'automatisation en déclenchant l'événement déclencheur — par exemple, créez une nouvelle ligne avec un texte plus long. Le résumé devrait apparaître dans la colonne de résultat en quelques secondes.

## Exemple d'application : Résumer des demandes de support

Imaginez un tableau dans lequel les demandes de support arrivent via un formulaire web. Chaque demande contient une **Description du problème** détaillée dans une colonne texte. Pour le chef d'équipe, une **Description courte** doit être générée automatiquement afin qu'il puisse parcourir les demandes plus rapidement.

**Configuration :**

- **Déclencheur** : Lorsqu'une ligne est ajoutée
- **Fonction** : Summarize
- **Colonne d'entrée** : Description du problème
- **Prompt** : *Résume la demande de support en deux phrases maximum. Mentionne le problème principal et la fonctionnalité concernée.*
- **Colonne de résultat** : Description courte

Dès qu'un client soumet le formulaire et qu'une nouvelle ligne est créée, l'IA écrit automatiquement une description courte dans la colonne de résultat.

## Conseils pour de bons résultats

- **Indiquez la longueur souhaitée.** Sans indication, la longueur du résumé peut varier. Un prompt comme « maximum 50 mots » garantit des résultats uniformes.
- **Utilisez plusieurs colonnes d'entrée** lorsque le contexte est réparti sur différentes colonnes. L'IA prend en compte toutes les entrées.
- **Testez avec des données réelles.** Créez quelques lignes de test avec des textes réalistes pour évaluer la qualité avant de mettre l'automatisation en production.

## Prochaines étapes

- [Classifier des entrées (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Extraire des informations (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Action IA personnalisée (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
