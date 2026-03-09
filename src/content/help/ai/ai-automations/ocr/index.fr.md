---
title: 'Reconnaissance de texte dans les images (OCR)'
description: "Avec la fonction IA OCR, vous reconnaissez automatiquement le texte dans les images et les documents numérisés dans votre base SeaTable."
weight: 5
url: '/fr/aide/automatisation-ia-reconnaissance-texte-ocr'
seo:
    title: 'Automatisation IA : Reconnaissance de texte (OCR) dans SeaTable'
    description: "Comment reconnaître automatiquement le texte dans les images avec SeaTable : configurer une automatisation IA avec la fonction OCR — lire les cartes de visite, factures et documents."
---

La fonction IA **OCR** (Optical Character Recognition) reconnaît le texte dans les images et écrit le contenu reconnu dans une colonne de texte. Cela vous permet de convertir automatiquement des documents numérisés, des photos de cartes de visite ou des images de factures en texte consultable.

## Cas d'utilisation typiques

- **Cartes de visite** : capturer automatiquement les photos de cartes de visite sous forme de texte.
- **Factures et reçus** : convertir les factures numérisées en texte lisible.
- **Bons de livraison** : extraire le texte des bons de livraison photographiés.
- **Notes manuscrites** : numériser les photos de notes manuscrites.
- **Documents** : rendre les contrats ou formulaires numérisés disponibles sous forme de texte.

## Prérequis

- Un tableau avec une [colonne image]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) ou une [colonne fichier]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) contenant les images ou documents à reconnaître.
- Une [colonne texte ou colonne texte formaté]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) pour le texte reconnu.

## Guide étape par étape

### 1. Créer une automatisation et choisir un déclencheur

Créez une nouvelle règle d'automatisation comme décrit dans l'article [Configurer une automatisation IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Un déclencheur typique est **Lorsqu'une ligne est ajoutée** — ainsi chaque image nouvellement téléchargée est automatiquement traitée.

Vous pouvez également utiliser **Lorsqu'une ligne est modifiée** et définir la colonne image comme colonne surveillée. Dans ce cas, la reconnaissance OCR est déclenchée chaque fois qu'une nouvelle image est insérée dans la colonne.

### 2. Ajouter l'action « Appeler l'IA »

Cliquez sur **Ajouter une action** et sélectionnez **Appeler l'IA**.

### 3. Sélectionner la fonction « OCR »

Dans les paramètres de l'action, choisissez :

- **Tableau** : le tableau dans lequel l'IA doit travailler.
- **Fonction** : **OCR**

![Paramètres de l'action avec la fonction OCR sélectionnée](images/ai-automation-ocr.png)

### 4. Définir la colonne d'entrée

Sélectionnez la colonne à partir de laquelle l'IA doit reconnaître le texte. Vous pouvez utiliser une **colonne image** ou une **colonne fichier** comme colonne d'entrée. Avec une colonne fichier, vous pouvez par exemple traiter des PDF ou des documents numérisés.

{{< warning headline="Remarque" text="Si une colonne image ou fichier contient plusieurs fichiers, seul le **premier fichier** est traité. Idéalement, ne téléchargez qu'une seule image ou un seul document par ligne dans la colonne d'entrée." />}}

### 5. Définir la colonne de résultat

Sélectionnez la colonne dans laquelle le texte reconnu doit être écrit. Celle-ci doit être de type **Texte** ou **Texte formaté**.

### 6. Enregistrer et tester

Cliquez sur **Enregistrer** et téléchargez une image de test avec un texte bien lisible dans la colonne image. Après quelques secondes, le texte reconnu devrait apparaître dans la colonne de résultat.

## Exemple d'application : numériser des cartes de visite

Votre équipe commerciale photographie des cartes de visite lors de salons et télécharge les photos dans un tableau SeaTable. L'IA doit reconnaître automatiquement le texte sur la carte de visite afin que vous puissiez rechercher les coordonnées.

**Configuration :**

- **Déclencheur** : Lorsqu'une ligne est ajoutée
- **Fonction** : OCR
- **Colonne d'entrée** : Image de carte de visite (colonne image)
- **Colonne de résultat** : Texte reconnu (colonne texte)

Dès qu'une nouvelle entrée avec une image de carte de visite est créée, l'IA lit le texte de l'image et l'écrit dans la colonne de résultat. À partir de là, vous pouvez traiter les données — par exemple avec une action **Extract** suivante pour extraire spécifiquement le nom, l'entreprise et le numéro de téléphone.

{{< warning headline="Astuce" text="Combinez l'OCR avec la fonction **Extract** dans une deuxième action au sein de la même automatisation. Ainsi, vous reconnaissez d'abord le texte, puis extrayez les informations pertinentes dans des colonnes séparées dans une deuxième étape." />}}

## Conseils pour de bons résultats

- **La qualité de l'image compte.** Plus l'image est nette et contrastée, meilleure est la reconnaissance de texte. Les photos floues ou un mauvais éclairage peuvent entraîner des erreurs.
- **Le texte imprimé fonctionne plus fiablement que l'écriture manuscrite.** Le texte dactylographié est reconnu presque sans erreur. Pour l'écriture manuscrite, la qualité dépend de la lisibilité.
- **Gardez l'image droite.** Les images fortement déformées ou pivotées peuvent rendre la reconnaissance plus difficile.
- **Utilisez des formats d'image courants.** JPG et PNG fonctionnent de manière fiable.

## Combiner l'OCR avec Extract

La fonction OCR fournit l'**intégralité du texte reconnu** sous forme de texte continu. Si vous souhaitez extraire des informations spécifiques (par ex. nom, adresse, numéro de facture), vous pouvez ajouter une deuxième action avec la fonction [Extract]({{< relref "help/ai/ai-automations/extract" >}}) dans la même automatisation. Ainsi, le texte reconnu est structuré en colonnes individuelles dans une deuxième étape.

## Prochaines étapes

- [Extraire des informations (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Résumer des textes (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Action IA personnalisée (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
