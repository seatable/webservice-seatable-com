---
title: 'Classer des entrées (Classify)'
description: 'Avec la fonction IA Classify, vous attribuez automatiquement des catégories aux entrées de votre base SeaTable.'
weight: 4
url: '/fr/aide/automatisation-ia-classer-entrees'
seo:
    title: 'Automatisation IA : Classer automatiquement des entrées dans SeaTable'
    description: 'Comment classer automatiquement des entrées dans SeaTable : configurer une automatisation IA avec la fonction Classify — définir des catégories et attribuer automatiquement des textes.'
---

La fonction IA **Classify** analyse le contenu d'une ou de plusieurs colonnes et attribue chaque entrée à une catégorie. Le résultat est écrit dans une colonne de sélection simple ou de sélection multiple. Vous pouvez ainsi classer automatiquement les textes entrants sans avoir à lire chaque entrée manuellement.

## Cas d'utilisation typiques

- **Tickets de support** : Classer automatiquement les demandes comme "Technical", "Billing", "General" ou "Feature Request".
- **Retours et avis** : Catégoriser les retours clients par sentiment (positif, neutre, négatif).
- **Boîte de réception e-mail** : Trier les messages entrants par sujet ou urgence.
- **Candidatures** : Classer les lettres de motivation par domaine de spécialité ou niveau d'expérience.

## Prérequis

- Un tableau avec au moins une **colonne Texte** servant d'entrée.
- Une **colonne Sélection simple** ou **colonne Sélection multiple** pour le résultat.

{{< warning headline="Important" text="Les catégories dans lesquelles l'IA doit classer doivent déjà être créées en tant qu'**options de sélection** dans la colonne de sélection simple ou de sélection multiple. L'IA ne peut attribuer que des options existantes." />}}

## Guide étape par étape

### 1. Créer les catégories dans la colonne de sélection

Avant de configurer l'automatisation, créez toutes les **catégories** souhaitées en tant qu'options dans la colonne de sélection simple (ou de sélection multiple). Par exemple : "Technical", "Billing", "General", "Feature Request".

![Colonne sélection simple avec catégories configurées](images/ai-automation-classify-options.png)

### 2. Créer une automatisation et choisir un déclencheur

Créez une nouvelle règle d'automatisation comme décrit dans l'article [Configurer une automatisation IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Un déclencheur typique est **Lorsqu'une ligne est ajoutée**, afin que chaque nouvelle entrée soit immédiatement classée.

### 3. Ajouter l'action « Appeler l'IA »

Cliquez sur **Ajouter une action** et sélectionnez **Appeler l'IA**.

### 4. Sélectionner la fonction « Classify »

Dans les paramètres de l'action, choisissez :

- **Tableau** : Le tableau dans lequel l'IA doit travailler.
- **Fonction** : **Classify**

![Options d'action pour la fonction Classify](images/ai-automation-classify.png)

### 5. Définir les colonnes d'entrée

Sélectionnez une ou plusieurs colonnes dont le contenu doit être analysé par l'IA pour déterminer la catégorie. L'IA lit les textes de ces colonnes et décide en fonction du contenu quelle catégorie convient le mieux.

### 6. Personnaliser le prompt

Dans le champ du prompt, vous pouvez donner à l'IA des instructions supplémentaires sur la manière de classer. C'est particulièrement utile lorsque les noms des catégories seuls ne sont pas suffisamment explicites.

**Exemples de prompts :**

| Prompt | Effet |
|---|---|
| *Classe la demande en fonction du sujet principal.* | Attribution simple par sujet |
| *Choisis "Technical" s'il s'agit de messages d'erreur ou de dysfonctionnements. Choisis "Billing" s'il s'agit de paiements ou de factures. Tout le reste est "General".* | Règles claires pour chaque catégorie |
| *Évalue le sentiment du texte : positif, neutre ou négatif.* | Analyse de sentiment |

{{< warning headline="Astuce" text="Plus vous décrivez précisément dans le prompt ce que signifie chaque catégorie, plus l'IA classe de manière fiable. Surtout pour des catégories similaires, une délimitation claire est recommandée." />}}

### 7. Définir la colonne de résultat

Sélectionnez la [colonne Sélection simple]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou la [colonne Sélection multiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}) dans laquelle le résultat doit être écrit.

- **Sélection simple** : L'IA choisit exactement une catégorie.
- **Sélection multiple** : L'IA peut attribuer plusieurs catégories simultanément.

### 8. Enregistrer et tester

Cliquez sur **Enregistrer** et testez l'automatisation avec une entrée dont la catégorie est évidente. Vérifiez si l'IA attribue la catégorie attendue.

## Exemple d'application : Catégoriser les tickets de support

Dans votre helpdesk, des demandes de support arrivent quotidiennement via un formulaire web. Chaque demande contient une **description** du problème. Vous souhaitez que chaque ticket soit automatiquement attribué à une catégorie afin que vos collaborateurs puissent traiter les tickets de manière filtrée.

**Configuration :**

- **Déclencheur** : Lorsqu'une ligne est ajoutée
- **Fonction** : Classify
- **Colonne d'entrée** : Description
- **Prompt** : *Classe la demande de support. Choisis "Technical" pour les erreurs, plantages et dysfonctionnements. Choisis "Billing" pour les questions relatives aux paiements, factures ou abonnements. Choisis "Feature Request" pour les suggestions d'amélioration. Tout le reste est "General".*
- **Colonne de résultat** : Catégorie (sélection simple avec les options "Technical", "Billing", "Feature Request", "General")

Dès qu'un nouveau ticket arrive, l'IA l'attribue automatiquement à la catégorie appropriée. Vos collaborateurs peuvent ensuite filtrer par catégorie et prioriser leurs tickets.

## Conseils pour de bons résultats

- **Gardez le nombre de catégories raisonnable.** Cinq à dix catégories fonctionnent généralement bien. Avec trop de catégories similaires, la précision diminue.
- **Décrivez chaque catégorie dans le prompt.** Surtout pour les noms de catégories ambigus, une brève explication aide l'IA dans l'attribution.
- **Utilisez une sélection simple** lorsque chaque entrée doit être attribuée à exactement une catégorie. N'utilisez une sélection multiple que lorsqu'une entrée peut effectivement appartenir à plusieurs catégories.
- **Vérifiez les premiers résultats.** Ajustez le prompt si l'IA classe de manière répétée incorrectement.

## Prochaines étapes

- [Résumer des textes (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Extraire des informations (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Action IA personnalisée (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
