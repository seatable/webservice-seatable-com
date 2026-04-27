---
title: 'Créer une automatisation'
date: 2022-12-06
lastmod: '2025-11-04'
categories:
    - 'automationen'
author: 'kgr'
url: '/fr/aide/creer-automatisation'
aliases:
    - '/fr/aide/anlegen-einer-automation'
seo:
    title: 'Créer une automatisation dans SeaTable – mode d’emploi'
    description: 'Découvrez comment configurer une automatisation SeaTable : déclencheurs, actions, conditions logiques pour des process optimisés.'
---

Les automatisations permettent d'**automatiser les processus**, ce qui permet non seulement de gagner du temps, mais aussi de réduire le nombre d'erreurs humaines. La première étape vers l'automatisation des flux de travail est la création d'une automatisation.

## Créer une automatisation

1. Ouvrez la **Base** dans laquelle vous souhaitez créer une automation.

![créer des automations](images/how-to-use-automations.jpg)

2. Dans l'en-tête de la base, cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} puis sur **Règles d'automatisation**.

3. Cliquez sur **Ajouter une règle ou un dossier**, puis sur **Règle**.

![Créer une automatisation](images/add-automation.jpg)

4. Donnez un **nom** à la règle d'automatisation.

5. Créez l'automation souhaitée en définissant un **déclencheur** et différentes **actions**.

{{< warning headline="Astuce" text="Si aucune règle n'existe dans la base, vous pouvez **sélectionner directement un déclencheur pour la toute première automation** – et SeaTable créera automatiquement une règle." />}}

![raccourci pour la première automatisation](images/shortcut-add-first-automation.gif)

### Créer une règle d'automatisation dans un dossier

Si vous avez déjà créé un dossier pour les règles d'automatisation, vous pouvez également créer une règle directement dans le dossier. Pour ce faire, placez le curseur de la souris sur le dossier, cliquez sur les **trois points** et sur **Ajouter une règle**.

![créer une règle d'automatisation dans un dossier](images/add-automation-in-folder.jpg)

## Autres étapes d'automatisation

### Administration

Tout d'abord, vous pouvez gérer la nouvelle règle d'automatisation, par exemple **renommer**, **supprimer** ou **déplacer vers un dossier**.

{{< button label="En savoir plus sur la gestion des règles d'automatisation" link="help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}

### Déclencheurs

L'étape suivante consiste à définir un événement qui servira de déclencheur et déclenchera l'automatisation. Vous définissez également ici dans quelle **table** et dans quelle **vue** l'automation doit agir. Le **déclencheur** peut être l'ajout d'une ligne ou le respect de certaines conditions après une modification. En outre, vous pouvez également définir que l'automatisation se déclenche quotidiennement, hebdomadairement ou mensuellement à un moment précis.

![paramètres de déclenchement](images/trigger-settings.jpg)

{{< button label="En savoir plus sur les déclencheurs d'automatisation" link="help/base-editor/automationen/automations-trigger" >}}

### Actions

Pour finir, définissez une ou plusieurs **actions** qui seront déclenchées par l'événement déclencheur défini précédemment. Les actions possibles peuvent être, par exemple, l'envoi de notifications et d'e-mails, l'ajout ou le verrouillage d'entrées ou l'exécution d'une fonction d'IA, selon le type de déclencheur.

![Autres étapes d'automatisation](images/steps-for-automation.jpg)

{{< button label="En savoir plus sur les actions d'automatisation" link="help/base-editor/automationen/automations-aktionen" >}}
