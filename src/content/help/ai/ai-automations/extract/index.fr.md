---
title: 'Extraire des informations (Extract)'
description: 'Avec la fonction IA Extract, vous pouvez lire de manière ciblée des informations dans des textes et les écrire dans des colonnes séparées.'
weight: 6
url: '/fr/aide/automatisation-ia-extraire-des-informations'
seo:
    title: 'Automatisation IA : Extraire automatiquement des informations dans SeaTable'
    description: 'Découvrez comment extraire des données de textes dans SeaTable : Configurez une automatisation IA avec la fonction Extract — lisez automatiquement les numéros de facture, dates et montants.'
---

La fonction IA **Extract** lit de manière ciblée certaines informations à partir de texte non structuré et les écrit dans des colonnes individuelles. Vous transformez ainsi du texte courant en données structurées — par exemple le numéro de facture, la date et le montant d'un texte de facture.

## Cas d'utilisation typiques

- **Factures** : Lire le numéro de facture, la date, le montant et le destinataire à partir de textes de factures.
- **E-mails** : Extraire le nom de l'expéditeur, l'objet et la demande principale des messages entrants.
- **Contrats** : Saisir la durée du contrat, le délai de résiliation et les parties contractantes à partir de textes de contrats.
- **Commandes** : Lire le numéro d'article, la quantité et l'adresse de livraison à partir de textes de commandes.
- **Cartes de visite** (après OCR) : Lire le nom, l'entreprise, le numéro de téléphone et l'e-mail à partir du texte reconnu.

## Prérequis

- Une table avec au moins une **colonne de texte** contenant le texte à analyser.
- Une ou plusieurs **colonnes de résultats** dans lesquelles les informations extraites seront écrites.

## Guide étape par étape

### 1. Créer une automatisation et choisir un déclencheur

Créez une nouvelle règle d'automatisation comme décrit dans l'article [Configurer une automatisation IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Choisissez un déclencheur approprié — par exemple **Lorsqu'une ligne est ajoutée**, afin que les nouvelles entrées soient traitées immédiatement.

### 2. Ajouter l'action « Appeler l'IA »

Cliquez sur **Ajouter une action** et sélectionnez **Appeler l'IA**.

### 3. Sélectionner la fonction « Extract »

Dans les paramètres de l'action, choisissez :

- **Table** : La table dans laquelle l'IA doit travailler.
- **Fonction** : **Extract**

![Paramètres de l'action pour la fonction Extract sélectionnée](images/ai-automations-extract.png)

### 4. Définir la colonne d'entrée

Sélectionnez la colonne dont le contenu doit être analysé par l'IA. Il s'agit généralement d'une **colonne de texte** avec du texte non structuré — par exemple le texte intégral d'une facture ou d'un e-mail.

### 5. Définir le prompt

Le prompt est particulièrement important pour la fonction Extract. Décrivez exactement **quelles informations** l'IA doit extraire. Soyez aussi précis que possible.

**Exemples de prompts :**

| Prompt | Informations extraites |
|---|---|
| *Extrais le numéro de facture, la date de facture et le montant total.* | Trois valeurs individuelles |
| *Lis le nom, l'entreprise et l'adresse e-mail à partir du texte.* | Coordonnées |
| *Trouve la date de début, la date de fin et le délai de résiliation.* | Informations contractuelles |
| *Extrais la désignation de l'article et la quantité commandée.* | Détails de commande |

### 6. Définir les colonnes de résultats

Attribuez chaque information à extraire à sa propre **colonne de résultats**. Choisissez le type de colonne correspondant au contenu attendu — l'IA reconnaît le format et écrit les valeurs directement dans le bon type de colonne. Ainsi, les dates se retrouvent de manière fiable dans une colonne de dates et les textes dans une colonne de texte.

![Configurer plusieurs colonnes de résultat](images/ai-automation-extract-output-mapping.png)

### 7. Enregistrer et tester

Cliquez sur **Enregistrer** et testez l'automatisation avec une entrée contenant les informations à extraire. Vérifiez si les valeurs arrivent correctement dans les colonnes de résultats.

## Exemple d'application : Lecture de données de facturation

Dans votre table, vous stockez les factures entrantes sous forme de texte courant (ou après reconnaissance OCR). Vous souhaitez extraire automatiquement les données de facturation les plus importantes dans des colonnes individuelles.

**Configuration :**

- **Déclencheur** : Lorsqu'une ligne est ajoutée
- **Fonction** : Extract
- **Colonne d'entrée** : Texte de la facture
- **Prompt** : *Extrais les informations suivantes du texte de la facture : numéro de facture, date de facture (au format JJ/MM/AAAA), montant net, montant TVA et montant brut.*
- **Colonnes de résultats** : Numéro de facture, Date de facture, Montant net, TVA, Montant brut

Dès qu'une nouvelle entrée avec un texte de facture est créée, l'IA extrait les données pertinentes et les écrit dans les colonnes respectives.

## Conseils pour de bons résultats

- **Soyez spécifique dans le prompt.** Au lieu de « Extrais les informations importantes », écrivez exactement quels champs vous avez besoin. Plus le prompt est précis, plus le résultat est fiable.
- **Indiquez le format souhaité.** Si vous avez besoin d'une date au format JJ/MM/AAAA, écrivez-le dans le prompt. Il en va de même pour les montants avec ou sans symbole de devise.
- **Testez avec différents textes.** Les factures de différents expéditeurs ont des formats différents. Vérifiez si l'IA trouve également les bonnes informations avec des mises en page différentes.
- **Combinez Extract avec l'OCR.** Si vos données sources se présentent sous forme d'images (par ex. des factures numérisées), utilisez d'abord la [fonction OCR]({{< relref "help/ai/ai-automations/ocr" >}}) puis Extract dans une deuxième action.

## Prochaines étapes

- [Reconnaissance de texte à partir d'images (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Résumer des textes (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Action IA personnalisée (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
