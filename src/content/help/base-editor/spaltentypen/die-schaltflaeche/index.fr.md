---
title: 'Le bouton'
date: 2023-01-07
lastmod: '2023-08-23'
categories:
    - 'andere-spalten'
author: 'nsc2'
url: '/fr/aide/colonne-bouton'
aliases:
    - '/fr/aide/die-schaltflaeche'
seo:
    title: 'Colonne bouton SeaTable – automatisation rapide'
    description: 'Automatisez vos tâches dans SeaTable via la colonne bouton : lancer scripts, envoyer emails, créer PDF et modifier le statut d’une ligne.'
weight: 25
---

La colonne des boutons a une fonction similaire à celle [des automatisations]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}), mais vous devez toujours utiliser les boutons **manuellement**. Le **bouton** que vous pouvez ajouter à vos **lignes** dans cette colonne vous permet de déclencher **des actions** définies à l'avance. C'est pourquoi ce type de colonne convient particulièrement bien à l'automatisation d'étapes de processus.

## Création du bouton

Tout d'abord, nommez la **colonne** et définissez le **libellé** et **la couleur du bouton** que vous souhaitez ajouter à vos lignes.

![Créer un bouton](images/create-button-column.png)

Dans l'étape suivante, vous définissez un nombre quelconque d'**actions** qui doivent être déclenchées par l'activation du bouton. Vous avez la possibilité d'enchaîner **plusieurs** actions.

![Panneau avec neuf actions de boutons](images/New-button-action-modal.png)

Vous pouvez choisir au total entre **neuf** actions différentes :

- Verrouiller la ligne
- Modifier la ligne
- Copier une ligne dans un autre tableau
- Ouvrir l'URL
- Ouvrir un plugin (possible uniquement si vous avez activé au moins un [plugin]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}) )
- Enregistrer le fichier PDF dans la colonne (possible uniquement si le [plug-in de conception de page]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) est activé)
- Envoyer une notification
- Envoyer un e-mail
- Exécuter le script

## Exemple d'application

Dans cet exemple d'application, nous utilisons le bouton pour attribuer le statut "payé" aux factures payées par un simple clic de souris. Pour cela, nous utilisons l'action **Modifier la ligne**.

![Sélection de l'action déclenchée par l'activation du bouton](images/modify-row.png)

Dans les **paramètres de la colonne**, nous indiquons que les entrées de la colonne de sélection simple **"status"** doivent passer de **"pending"** à **"paid"** en activant le bouton.

![Définition du bouton dans l'exemple d'application](images/settings-of-the-button-column-in-the-example.png)

Après avoir cliqué sur le bouton, le **statut** de la facture sélectionnée passe à **paid**.

![Action déclenchée dans l'exemple d'application du bouton](images/example-button-column.gif)

### Possibilité supplémentaire

Pour étendre l'automatisation des étapes de processus, vous pouvez également utiliser des boutons en combinaison avec [des automatisations]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) le traitement des **lignes** contenant les factures respectives qui ont été définies comme payées.

![Exemple d'application pour l'utilisation du bouton en combinaison avec des automatisations](images/use-the-button-cplumn-with-automations.gif)
