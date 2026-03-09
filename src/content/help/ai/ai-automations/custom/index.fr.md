---
title: 'Action IA personnalisée (Custom)'
description: "Avec la fonction IA Custom, vous définissez votre propre prompt et laissez l'IA exécuter n'importe quelle tâche sur vos données."
weight: 7
url: '/fr/aide/automatisation-ia-action-personnalisee'
seo:
    title: 'Automatisation IA : Action IA personnalisée dans SeaTable'
    description: "Comment créer des automatisations IA personnalisées dans SeaTable : rédigez votre propre prompt et faites traduire, reformuler ou évaluer des textes."
---

La fonction IA **Custom** est la plus flexible des cinq actions IA. Vous rédigez votre propre prompt et déterminez librement ce que l'IA fait avec vos données. Tout ce qui ne rentre pas dans les quatre fonctions standard (Summarize, Classify, OCR, Extract) peut être réalisé avec Custom.

## Cas d'utilisation typiques

- **Traduire** : Traduire automatiquement des textes dans une autre langue.
- **Reformuler** : Réécrire des textes dans un autre ton ou style (par ex. formel, orienté client, simplifié).
- **Suggestions de réponse** : Générer un brouillon de réponse basé sur une demande client.
- **Évaluer** : Évaluer des textes selon vos propres critères sur une échelle (par ex. pertinence, qualité, urgence).
- **Générer** : Créer des descriptions de produits, des publications pour les réseaux sociaux ou des méta-textes à partir de points clés.
- **Corriger** : Corriger automatiquement les fautes d'orthographe et de grammaire dans les textes.

## Prérequis

- Un tableau avec au moins une colonne dont le contenu doit être traité par l'IA.
- Une **colonne Texte** ou **colonne Texte formaté** pour le résultat.

## Guide étape par étape

### 1. Créer une automatisation et choisir un déclencheur

Créez une nouvelle règle d'automatisation comme décrit dans l'article [Configurer l'automatisation IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Choisissez le déclencheur approprié pour votre cas d'utilisation.

### 2. Ajouter l'action « Appeler l'IA »

Cliquez sur **Ajouter une action** et sélectionnez **Appeler l'IA**.

### 3. Sélectionner la fonction « Custom »

Dans les paramètres de l'action, choisissez :

- **Tableau** : Le tableau dans lequel l'IA doit travailler.
- **Fonction** : **Custom**

![Paramètres de l'action avec la fonction Custom sélectionnée](images/ai-automation-custom.png)

### 4. Rédiger le prompt

Le prompt est le cœur de la fonction Custom. Vous y formulez l'instruction pour l'IA. Utilisez **{Nom de colonne}** entre accolades pour insérer la valeur d'une colonne de la ligne actuelle dans le prompt.

**Structure d'un bon prompt :**

```
Traduis le texte suivant en anglais.
Conserve le ton et le formatage.

Texte : {Description}
```

Dans cet exemple, `{Description}` est remplacé à chaque exécution par le contenu réel de la colonne « Description ».

![Champ de saisie du prompt avec référence de colonne](images/ai-automation-custom-reference-column-by-name.png)

### 5. Définir la colonne de résultat

Sélectionnez la colonne dans laquelle le résultat de l'IA doit être écrit. Celle-ci doit être de type **Texte** ou **Texte formaté**.

### 6. Enregistrer et tester

Cliquez sur **Enregistrer** et testez l'automatisation avec une entrée. Vérifiez si le résultat dans la colonne de résultat correspond à vos attentes et ajustez le prompt si nécessaire.

## Exemples de prompts pour les tâches courantes

### Traduire des textes

```
Traduis le texte suivant en anglais.
Conserve les termes techniques et ne les traduis pas.

Texte : {Description du produit}
```

### Générer une suggestion de réponse

```
Rédige une réponse amicale et professionnelle
à la demande client suivante. La réponse ne doit
pas dépasser cinq phrases.

Demande : {Demande client}
```

### Reformuler un texte

```
Reformule le texte suivant pour qu'il soit adapté
à un communiqué de presse. Utilise un ton factuel
et professionnel.

Texte original : {Notes}
```

### Évaluer un contenu

```
Évalue le texte suivant sur une échelle de 1 à 5
en ce qui concerne son urgence. Réponds uniquement
avec le chiffre et une courte justification en une phrase.

Texte : {Demande de support}
```

### Générer une description de produit

```
Crée une description de produit attrayante pour une
boutique en ligne à partir des points clés suivants.
La description doit contenir entre 50 et 80 mots.

Nom du produit : {Nom}
Caractéristiques : {Caractéristiques}
Public cible : {Public cible}
```

### Corriger l'orthographe et la grammaire

```
Corrige les fautes d'orthographe et de grammaire dans
le texte suivant. Ne modifie pas le contenu ni les
formulations. Renvoie uniquement le texte corrigé.

Texte : {Texte libre}
```

## Exemple d'application : Traduire des descriptions de produits

Votre tableau de produits contient des descriptions de produits en allemand. Pour la boutique en ligne internationale, vous avez besoin de traductions en anglais. Au lieu de traduire chaque description manuellement, l'IA doit le faire automatiquement.

**Configuration :**

- **Déclencheur** : Lorsqu'une ligne est ajoutée
- **Fonction** : Custom
- **Prompt** : *Traduis le texte allemand suivant en anglais. Utilise un ton attrayant adapté à une boutique en ligne. Conserve les noms de produits et les noms de marques tels quels. Texte : {Description DE}*
- **Colonne de résultat** : Description EN (colonne Texte)

Dès qu'un nouveau produit avec une description en allemand est saisi, la traduction anglaise apparaît automatiquement dans la colonne de résultat.

## Conseils pour de bons prompts

- **Soyez précis.** « Écris un bon texte » donne des résultats imprévisibles. « Écris une description de produit de 50 à 80 mots dans un ton amical » est nettement mieux.
- **Utilisez les références de colonnes.** Avec `{Nom de colonne}`, vous pouvez combiner les valeurs de plusieurs colonnes dans un prompt pour fournir du contexte.
- **Définissez le format de sortie.** Le résultat doit-il être une seule phrase ? Une liste ? Un chiffre avec justification ? Précisez-le dans le prompt.
- **Testez et itérez.** Essayez le prompt avec différentes entrées. Si les résultats ne conviennent pas, ajustez la formulation.
- **Rédigez le prompt dans la langue cible.** Si le résultat doit être en anglais, rédigez le prompt en anglais. Cela améliore la qualité des résultats.

## Prochaines étapes

- [Résumer des textes (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Classifier des entrées (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Extraire des informations (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Reconnaissance de texte à partir d'images (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
