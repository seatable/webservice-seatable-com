---
title: 'Configurer une automatisation IA'
description: 'Créez une automatisation IA dans SeaTable étape par étape — du déclencheur à l''action IA finalisée.'
weight: 2
url: '/fr/aide/configurer-automatisation-ia'
seo:
    title: 'Configurer une automatisation IA dans SeaTable — Guide étape par étape'
    description: 'Comment créer une automatisation IA dans SeaTable : choisir un déclencheur, configurer la fonction IA, définir les colonnes d''entrée et de résultat, et tester.'
---

Dans ce guide, vous allez créer une automatisation avec l'action **Exécuter l'IA**. Une fois configurée, SeaTable traitera automatiquement vos données à l'aide d'un modèle IA — par exemple pour résumer des textes, catégoriser des entrées ou extraire des informations.

## Prérequis

- SeaTable (Cloud ou Server) **version 6.0** ou supérieure
- Une base contenant une table avec des données textuelles

{{< warning headline="Note pour les clients auto-hébergés" >}}

Dans **SeaTable Cloud**, le serveur IA est déjà intégré. SeaTable exploite son propre modèle linguistique (Gemma 3) sur une infrastructure GPU en Allemagne — vous pouvez utiliser les automatisations IA immédiatement.

Si vous **auto-hébergez** SeaTable, vous devez soit exploiter votre propre serveur IA, soit configurer une connexion à un fournisseur d'IA cloud. Pour plus d'informations, consultez le [guide d'installation de SeaTable AI](https://admin.seatable.com/installation/components/seatable-ai/).

{{< /warning >}}

## Étape 1 : Créer une règle d'automatisation

1. Ouvrez votre base et cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de la base, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle ou un dossier** et sélectionnez **Ajouter une règle**.
3. Donnez à l'automatisation un **nom** explicite, par exemple « Résumer les demandes de support ».

![Page d'aperçu des règles d'automatisation](images/ai-automation-overview.png)

## Étape 2 : Choisir un déclencheur

Cliquez sur **Ajouter un déclencheur** et sélectionnez un déclencheur. Deux déclencheurs sont disponibles pour les automatisations IA :

- **Lorsqu'une ligne est modifiée** — l'IA traite immédiatement la ligne modifiée
- **Lorsqu'une ligne est ajoutée** — l'IA traite automatiquement chaque nouvelle entrée

Sélectionnez ensuite la **table** et la **vue** dans lesquelles l'automatisation doit fonctionner. Vous pouvez éventuellement définir des **conditions** pour déclencher l'automatisation uniquement pour certaines entrées.

![Sélection du déclencheur](images/automation-trigger-selection.png)

{{< warning headline="Remarque" text="Les déclencheurs temporels (**À une heure programmée** et **À une heure programmée pour les entrées répondant à certaines conditions**) ne prennent actuellement pas en charge les actions IA." />}}

## Étape 3 : Ajouter l'action IA

1. Cliquez sur **Ajouter une action**.
2. Sélectionnez **Exécuter l'IA** en bas de la liste des actions disponibles.

![Liste des actions avec l'option Exécuter l'IA](images/automation-action-run-ai.png)

## Étape 4 : Configurer la fonction IA

Après avoir sélectionné l'action **Exécuter l'IA**, les **paramètres de l'action** s'ouvrent à droite. Configurez les éléments suivants :

### Table
Sélectionnez la table dans laquelle l'IA doit travailler. En règle générale, il s'agit de la même table que celle du déclencheur.

### Fonction
Choisissez l'une des cinq fonctions IA disponibles :

| Fonction | Description | Utilisation typique |
|---|---|---|
| **Summarize** | Résume les textes | Condenser de longues descriptions |
| **Classify** | Attribue des catégories | Catégoriser les demandes de support |
| **OCR** | Reconnaît le texte dans les images | Lire des cartes de visite, factures |
| **Extract** | Extrait des informations ciblées | Extraire numéro de facture, date |
| **Custom** | Prompt personnalisé | Traduire, évaluer, reformuler |

![Menu déroulant avec les cinq fonctions IA](images/automation-select-ai-function.png)

### Colonnes d'entrée
Sélectionnez une ou plusieurs colonnes dont le contenu doit être traité par l'IA. Il s'agit du texte (ou de l'image/du fichier pour l'OCR) que l'IA reçoit en entrée.

### Prompt
Pour toutes les fonctions sauf OCR, vous pouvez saisir un **prompt** pour contrôler le résultat. Par exemple : « Le résumé ne doit pas dépasser deux phrases et être rédigé en français. » Pour l'OCR, aucun prompt n'est nécessaire — l'IA reconnaît automatiquement le texte dans l'image.

### Colonne(s) de résultat
Sélectionnez la colonne dans laquelle le résultat de l'IA doit être écrit. Le type de colonne doit correspondre à la fonction choisie — par exemple une colonne texte pour les résumés ou une colonne sélection simple pour les classifications.

## Étape 5 : Enregistrer et activer

1. Cliquez sur **Enregistrer** pour sauvegarder les paramètres de l'action.
2. L'automatisation est maintenant active et s'exécutera automatiquement lors du prochain événement déclencheur.

## Tester l'automatisation

Pour tester l'automatisation immédiatement, déclenchez l'événement manuellement :

- Pour **Lorsqu'une ligne est ajoutée** : créez une nouvelle ligne avec des données de test.
- Pour **Lorsqu'une ligne est modifiée** : modifiez une valeur dans une colonne surveillée.

Vérifiez ensuite si l'IA a écrit le résultat dans la colonne de résultat. Vous pouvez consulter le statut et les éventuelles erreurs dans le [journal d'exécution]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}).

![Journal d'exécution d'une automatisation IA](images/automation-open-log.png)

## Problèmes fréquents

| Problème | Solution |
|---|---|
| La colonne de résultat reste vide | Vérifiez que la colonne d'entrée contient effectivement une valeur. Les entrées vides ne produisent aucun résultat. |
| Mauvais type de colonne | La colonne de résultat doit correspondre au résultat. Les classifications nécessitent une colonne sélection simple, les résumés une colonne texte. |
| L'automatisation ne se déclenche pas | Vérifiez que l'automatisation est activée et que la modification a lieu dans la bonne table et vue. |

## Prochaines étapes

Des guides détaillés pour chaque fonction IA sont disponibles dans ces articles :

- [Résumer des textes (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Classer des entrées (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Reconnaissance de texte dans les images (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Extraire des informations (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Action IA personnalisée (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
