---
title: 'Exécuter une opération de traitement de données par automatisation'
date: 2023-04-28
lastmod: '2023-05-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/fr/aide/automatiser-traitement-donnees-seatable'
aliases:
    - '/fr/aide/datenverarbeitungsoperation-per-automation-ausfuehren'
seo:
    title: 'Automatisez le traitement des données dans SeaTable'
    description: 'Exécutez des opérations de traitement des données via des automatisations et gagnez du temps : calculs, liaisons et plus encore, de façon sûre.'

---

Grâce à l'automatisation, vous ne devez plus effectuer une opération de traitement des données manuellement, mais vous pouvez la faire exécuter automatiquement. La diversité des [opérations de traitement des données]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) disponibles - des calculs mathématiques à l'établissement de liens entre les valeurs de différents tableaux - vous ouvre de nouvelles possibilités d'automatisation de vos processus de travail.

## Exécuter une opération de traitement de données par automatisation

![Exécuter une opération de traitement de données par automatisation](images/how-to-use-automations-for-locking-rows-3.png)

1. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de base, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. Donnez un **nom** à l'automation et définissez le **tableau** et la **vue** dans laquelle elle doit être déclenchée.
4. Définir un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Exécuter une opération de traitement des données** comme action automatisée.
6. Sélectionnez n'importe quelle **opération de traitement des données**.
7. Effectuez les **réglages** nécessaires (par exemple, tableau, colonne source, colonne résultat) sur l'**opération de traitement des données**.
8. Confirmez en cliquant sur **Envoyer**.

## Création de l'automation

Après avoir déterminé dans quel **tableau** et quelle **vue** l'automatisation doit être déclenchée, vous définissez l'[événement déclencheur]({{< relref "help/base-editor/automationen/automations-trigger" >}}). Actuellement, seul un **déclencheur périodique** peut entraîner une opération de traitement des données. C'est pourquoi vous devez définir un **moment** où l'automation doit être déclenchée quotidiennement, hebdomadairement ou mensuellement.

![Sélection du déclencheur d'automatisation pour l'action : Exécuter une opération de traitement des données](images/select-trigger-for-data-operation-per-automation.png)

{{< warning  headline="Remarque importante"  text="L'action automatisée **Exécuter une opération de traitement de données** est à votre disposition **exclusivement** est disponible lors de l'événement déclencheur suivant :" />}}

![Déclencheur périodique]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_periodischer_trigger)

Sélectionnez ensuite **Exécuter une opération de traitement des données** comme action automatisée et choisissez l'[opération de traitement des données]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) souhaitée.

![Ajout de l'action automatisée](images/add-an-action.png)

![Sélection de l'opération de traitement des données à exécuter comme action automatisée de l'automatisation](images/select-data-operation-for-automation.png)

Les **opérations de traitement des données** suivantes sont à votre disposition :

- [Calculer des valeurs cumulées]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calculer des variations]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calculer un pourcentage]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calculer un classement]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Transférer des noms d'utilisateur]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparer et copier]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

Dans l'étape suivante, effectuez des **réglages** spécifiques sur l'**opération de traitement des données** qui doit être déclenchée par l'automatisation. Selon l'opération sélectionnée, vous serez invité à définir les **tableaux** et/ou **colonnes** (par exemple colonne source et colonne résultat) que vous souhaitez utiliser pour les calculs mathématiques ou pour établir des relations entre les valeurs de différents tableaux.

![Réglages spécifiques à effectuer sur l'opération de traitement des données](images/specific-settings-for-data-processing-operation.png)

Confirmez enfin l'automatisation avec **Envoyer** pour l'enregistrer et la faire exécuter au moment défini du déclencheur, ou cliquez sur **Exécuter maintenant** pour faire exécuter l'automatisation **directement**.

![Enregistrer l'automatisation ou la faire exécuter directement](images/cancel-run-now-or-submit-automation.png)

## Exemple d'application

Un cas d'utilisation concret de ce type d'automatisation pourrait par exemple se présenter si vous souhaitez enregistrer dans votre tableau le nombre de visites quotidiennes à un site web. Pour cela, vous souhaitez **cumuler** ligne par ligne, dans une nouvelle colonne, les **chiffres de visites** de chaque jour, saisis dans une [colonne numérique]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}) existante.

Jusqu'à présent, [le calcul des chiffres de visites cumulés à l'aide d'une opération de traitement des données]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}}) n'était possible que **manuellement**. Grâce à une automatisation correspondante, il est désormais possible de faire calculer les chiffres de visites cumulés **automatiquement** **chaque jour** à une heure fixe.

Pour la mise en œuvre, vous avez d'abord besoin d'un tableau dans lequel les différents **jours** sont enregistrés dans une [colonne de date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) et les **chiffres de visites** du site web dans une [colonne numérique]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}).

![Tableau d'exemple pour le cas d'utilisation de l'automatisation : Calculer des valeurs cumulées](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen.png)

Ajoutez ensuite au tableau une **deuxième colonne numérique**, dans laquelle les valeurs cumulées seront calculées après chaque exécution de l'automatisation. La nouvelle colonne _Cumulated Visitors_, initialement vide, fait office de **colonne résultat** dans l'opération de traitement des données, tandis que la colonne _Unique Visitors_ constitue la **colonne source**.

![Ajout d'une deuxième colonne numérique](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen-2.png)

Pour créer l'automatisation, suivez les étapes décrites dans la section [Création de l'automatisation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}). Sélectionnez également la colonne _Unique Visitors_ comme **colonne source** et la colonne nouvellement ajoutée _Cumulated Visitors_ comme **colonne résultat**.

![Sélection de la colonne source et de la colonne résultat](images/auswahl-quell-und-ergebnisspalte-im-anwendungsfall.png)

Après confirmation de l'automatisation, SeaTable calcule quotidiennement, au moment sélectionné, le **nombre cumulé de visiteurs du site web** et l'inscrit automatiquement dans la colonne résultat. Le calcul automatique des valeurs cumulées suppose bien entendu que le **nombre de visiteurs du site web de la veille** soit inscrit chaque jour, **avant** l'exécution de l'automatisation, dans la colonne _Unique Visitors_.

Tableau **avant** le déclenchement de l'automatisation :

![Tableau d'exemple avant le déclenchement de l'automatisation](images/Beispiel-Tabelle-vor-Ausloesung-der-Auomation-Kumulierte-Werte-Berechnen.png)

Tableau **après** le déclenchement de l'automatisation :

![Tableau d'exemple après le déclenchement de l'automatisation](images/Beispiel-Tabelle-nach-Ausloesung-der-Automation-Kumulierte-Werte-berechnen.png)
