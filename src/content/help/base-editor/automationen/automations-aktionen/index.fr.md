---
title: "Actions d'automatisation"
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/fr/aide/actions-automatisation-seatable'
aliases:
    - '/fr/aide/automations-aktionen'
seo:
    title: 'Actions d’automatisation SeaTable : toutes les solutions'
    description: 'Liste détaillée : notifications, email, ajout/lien/édition de ligne, scripts, traitement de données dans SeaTable – toutes les actions en un coup d’œil.'
weight: 6
---

**Les actions automatisées** représentent l'une des deux composantes essentielles des automatisations. Les actions sont alors déclenchées par des **événements déclencheurs** définis. Selon le [déclencheur]({{< relref "help/base-editor/automationen/automations-trigger" >}}), SeaTable peut exécuter différentes actions d'automatisation. Cet article vous donne un **aperçu** des différents types d'actions automatisées.

## Actions d'automatisation disponibles

La dernière version de SeaTable propose un total de 15 actions d'automatisation différentes :

- Envoyer une notification
- Envoyer une notification à une app
- Envoyer un e-mail
- Ajouter un enregistrement
- Verrouiller l'enregistrement
- Modifier l'enregistrement
- Ajouter des liens
- Ajouter un enregistrement dans un autre tableau
- Exécuter un script Python
- Appeler l'IA
- Gérer les rendez-vous dans Google Agenda
- Exécuter un traitement de données
- Convertir une page en PDF
- Créer un PDF à partir d'un document et l'envoyer
- Archiver

## Ajouter, dupliquer, déplacer et supprimer des actions d'automatisation

Pour ajouter une action, cliquez sur **le gros bouton avec l'icône plus** et sélectionnez l'action correspondante dans la liste déroulante. Notez que les actions disponibles varient selon le déclencheur.

![Ajouter des actions d'automatisation](images/automated-actions.jpg)

Si vous avez déjà mis en place des actions plus élaborées, comme l'envoi d'e-mails, le traitement des données ou les fonctions d'intelligence artificielle, vous pouvez également les dupliquer. Il suffit de cliquer sur les **trois points** puis sur **Dupliquer**. Vous n'aurez ainsi que peu de modifications à apporter à ces actions et vous gagnerez beaucoup de temps.

![dupliquer les actions d'automatisation](images/duplicate-automated-actions.jpg)

L'ordre des actions peut être facilement modifié **par glisser-déposer**. Placez le curseur de la souris sur une case d'action, maintenez le bouton gauche de la souris enfoncé sur la **surface de préhension à six points** et déplacez l'action à l'endroit souhaité. Vous pouvez ainsi adapter le déroulement de l'automatisation de manière flexible.

![Déplacer les actions d'automatisation](images/move-automated-actions.gif)

Bien entendu, vous pouvez également supprimer les actions dont vous n'avez plus besoin. Pour ce faire, cliquez sur les **trois points** puis sur **Supprimer**. Notez que les actions automatisées sont **supprimées immédiatement et définitivement** et ne peuvent pas être restaurées.

![supprimer les actions automatisées](images/delete-automated-actions.gif)

## Action automatisée : Envoyer une notification

En définissant "Envoyer une notification" comme action automatisée, vous pouvez définir une notification à un ou plusieurs utilisateurs. Les utilisateurs sélectionnés recevront une **notification** à chaque fois que le déclencheur correspondant sera déclenché. Cette action d'automatisation est disponible **pour tous les déclencheurs d'automatisation**.

Vous pouvez modifier les **destinataires** et le **contenu** des notifications à tout moment dans les **paramètres** de l'action. Pour les destinataires, vous pouvez concrètement sélectionner **des utilisateurs individuels** ou des utilisateurs dans une colonne spécifique de type [Collaborateur]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Créateur]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) ou [Dernier éditeur]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}). Écrivez le message souhaité dans la zone de texte et travaillez avec des références de colonne entre accolades pour insérer des valeurs spécifiques.

![Envoyer une notification par automation](images/send-notification-action-settings.jpg)

Les utilisateurs peuvent recevoir leurs notifications via l'icône {{< seatable-icon="dtable-icon-notice" >}} **icône en forme de cloche** à côté de leur avatar dans le coin supérieur droit.

![Notification reçue](images/example-action-notification.png)

L'article [Envoyer des notifications par automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}}) joue sur cette automation à travers un cas d'utilisation concret.

## Action d'automatisation : Envoyer une notification à une app

En définissant "Envoyer une notification à une app" comme action automatisée, vous pouvez définir une notification à un ou plusieurs utilisateurs d'une app. Les utilisateurs sélectionnés recevront une **notification** dans l'app chaque fois que le déclencheur correspondant sera déclenché. Cette action d'automatisation est disponible **pour tous les déclencheurs d'automatisation**.

Dans les **paramètres** de l'action, vous pouvez définir à quelle **app** et à quels **destinataires** les notifications doivent être envoyées. Pour les destinataires, vous pouvez concrètement sélectionner **des utilisateurs d'apps individuels** ou notifier des utilisateurs dans une colonne spécifique de type **Collaborateur, Créateur ou Dernier éditeur**. Saisissez le **contenu** de la notification dans la zone de texte. Utilisez les références de colonne entre accolades pour insérer des valeurs spécifiques.

![envoyer une notification à une app par automatisation](images/send-app-notification-action-settings.jpg)

Les utilisateurs de l'app concernée peuvent recevoir leurs notifications via **l'icône en forme de cloche** {{< seatable-icon="dtable-icon-notice" >}} à côté de leur avatar dans le coin supérieur droit.

![Consulter les notifications dans l'application](images/check-app-notifications.jpg)

## Action d'automatisation : Envoyer un e-mail

En définissant "Envoyer un e-mail" comme action automatisée, vous pouvez envoyer des e-mails prédéfinis à un ou plusieurs utilisateurs. SeaTable envoie un **e-mail** à chaque utilisateur sélectionné lorsque le déclencheur correspondant est activé. Cette action d'automatisation est disponible **pour tous les déclencheurs d'automatisation**.

Vous pouvez modifier à tout moment le **compte e-mail**, l'**objet**, le **destinataire**, le **message** et les **pièces jointes** de l'e-mail dans les **paramètres** de l'action. Pour ce faire, utilisez les références de colonne entre accolades pour insérer des valeurs spécifiques dans les champs de texte.

![définition de l'action d'automatisation : Envoyer un e-mail](images/send-email-action-settings.jpg)

L'article [Envoi d'e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) joue sur cette automatisation à travers un cas d'utilisation concret.

## Action d'automatisation : Ajouter un enregistrement

Si vous définissez "Ajouter un enregistrement" comme action automatisée, une **nouvelle ligne** sera ajoutée au tableau chaque fois que le déclencheur correspondant sera déclenché. Vous pouvez définir à l'avance les valeurs exactes pour chaque colonne individuellement.

![Action d'automatisation : ajouter un enregistrement](images/add-record-action-settings.jpg)

L'action d'automatisation "Ajouter un enregistrement" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- À une heure programmée

L'article [Ajouter des lignes par automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) passe en revue cette automation à travers un cas d'utilisation concret.

## Action d'automatisation : Verrouiller l'enregistrement

Si vous définissez "Verrouiller l'enregistrement" comme action automatisée, la **ligne** qui a déclenché l'automation sera verrouillée pour l'édition. Vous ne pouvez pas définir d'autres paramètres pour cette action – vous devez configurer les conditions de verrouillage de la ligne avec le **déclencheur**. Notez que vous ne pouvez pas **déverrouiller** les lignes verrouillées sans droits d'administrateur.

![définition de l'action d'automatisation : Verrouiller un enregistrement dans la table](images/lock-record-action.jpg)

![Verrouillage d'un enregistrement dans une table déclenché par une automatisation ](images/example-locked-records.jpg)

L'action d'automation "Verrouiller l'enregistrement" est actuellement disponible pour **les déclencheurs d'automation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- A une heure programmée pour les enregistrements qui correspondent aux conditions

L'article [Verrouiller des lignes par automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) passe en revue cette automation à travers un cas d'utilisation concret.

## Action d'automatisation : Modifier l'enregistrement

Si vous sélectionnez "Modifier l'enregistrement" comme action automatisée, les **lignes** du tableau seront modifiées après le déclenchement du trigger selon les **paramètres** définis au préalable. Vous pouvez définir pour chaque colonne une valeur que les lignes prendront automatiquement après la modification.

![Action d'automatisation : modifier l'enregistrement](images/modify-record-action-settings.jpg)

L'action d'automatisation "Modifier l'enregistrement" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- À une heure programmée pour les enregistrements qui correspondent aux conditions

## Action d'automatisation : Ajouter des liens

Si vous sélectionnez "Ajouter des liens" comme action automatisée, un [lien vers d'autres enregistrements]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) sera créé dans la colonne correspondante lors du déclenchement du trigger. Dans les **paramètres** de l'action, vous pouvez définir précisément les conditions d'ajout de tel ou tel lien dans le tableau.

![Action d'automatisation : ajout de liens](images/add-links-action-settings.jpg)

L'action d'automatisation "Ajouter des liens" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- À une heure programmée

L'article [Lier des enregistrements par automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) joue cette automation avec un cas d'utilisation concret.

## Action d'automatisation : Ajouter un enregistrement dans un autre tableau

Si vous sélectionnez "Ajouter un enregistrement dans un autre tableau" comme action automatisée, une **ligne sera créée dans un autre tableau** lorsque le déclencheur sera déclenché. Dans les **paramètres** de l'action, vous pouvez définir des valeurs individuelles pour chaque colonne, qui seront affectées aux lignes du tableau sélectionnée au cours de l'automatisation. De même, vous pouvez sélectionner des colonnes du même type dans la table source pour copier des enregistrements de ligne dans l'autre table.

![Action d'automatisation : Ajouter un enregistrement dans une autre table](images/add-record-to-other-table-action-settings.jpg)

L'action d'automatisation "Ajouter une nouvelle enregistrement dans un autre tableau" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée

L'article [Ajouter des enregistrements dans d'autres tables par automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) joue cette automation à travers un cas d'utilisation concret.

## Action d'automatisation : Exécuter un script Python

Si vous choisissez l'exécution d'un script Python comme action automatisée, le déclencheur met en route un **script Python** défini au préalable. Vous pouvez créer ou éditer le script à tout moment dans l'[éditeur de script]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}), puis le sélectionner dans les **paramètres** de l'action.

![Action d'automatisation : Exécuter un script Python](images/run-python-script-action-settings.jpg)

L'action d'automatisation "Exécuter un script Python" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- À une heure programmée

## Action d'automatisation : Appeler l'IA

Lorsque vous sélectionnez l'exécution d'une fonction d'IA comme action automatisée, le déclencheur appelle un **modèle d'IA** qui exécute une action définie au préalable dans la table. Vous pouvez configurer précisément l'action à exécuter dans les **paramètres**. Selon le type de fonction d'IA, vous pouvez avoir besoin de **colonnes d'entrée**, de **colonnes de sortie** et d'une **invite**.

![définition d'une action d'automatisation : Exécuter l'IA](images/run-ai-action-settings.jpg)

Vous pouvez faire exécuter les **fonctions d'IA** suivantes par une automation :

- **Résumer** : Résume le texte d'une ou plusieurs colonnes. Vous pouvez contrôler la longueur, le ton, le format et la langue du résumé en ajustant l'invite.
- **Classer** : Classifie les enregistrements d'une ou plusieurs colonnes. Vous pouvez personnaliser les catégories et les règles en utilisant l'invite. Le résultat atterrit dans une [colonne de sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou [colonne de sélection multiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
- **OCR** : Extrait du texte d'une [colonne d'image]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}). Le contenu reconnu est écrit dans la colonne de résultat de type [Texte ou Texte formaté]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}).
- **Extraire** : Extrait des informations spécifiques d'une colonne de type texte ou nombre en fonction de votre demande. Les informations extraites sont écrites dans les colonnes de résultats.
- **Défini par l'utilisateur** : Génère du contenu basé sur votre invite. Utilisez {nom de la colonne} entre accolades pour insérer la valeur de la colonne d'une ligne.

![actions exécutables à l'aide d'un modèle d'IA](images/run-ai-functions.jpg)

L'action d'automatisation "Appeler l'IA" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- À une heure programmée

## Action d'automatisation : Gérer les rendez-vous dans Google Agenda

Si vous sélectionnez "Gérer les rendez-vous dans Google Agenda" comme action automatisée, un rendez-vous de SeaTable sera créé ou mis à jour dans un Google Agenda lorsque le déclencheur est déclenché. Il y a quelques conditions à remplir pour que cette action fonctionne correctement :
- Tout d'abord, vous devez [synchroniser votre compte Google Agenda avec SeaTable]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/google-calender-synchronisieren" >}}).
- Dans un tableau, il doit y avoir deux [colonnes de dates]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) qui définissent le **début** et la **fin** des dates.
- Vous avez également besoin d'une [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) dans laquelle Google peut enregistrer l'**ID de l'événement** afin de synchroniser les rendez-vous.

![conditions préalables pour la gestion des événements dans Google Calendar](images/manage-events-in-google-calendar-part-1.png)

En outre, vous pouvez définir d'autres paramètres. Ajoutez un **titre**, une **description**, un **lieu** et des **participants** au rendez-vous. Pour ce faire, écrivez les informations dans les **champs de texte** ou utilisez les **références de colonne entre accolades** pour insérer des valeurs spécifiques du tableau. En activant les **régulateurs**, vous pouvez décider si vous souhaitez envoyer des notifications, s'il s'agit d'une vidéoconférence et si les invités peuvent modifier le rendez-vous, voir la liste des invités et inviter d'autres invités.

![Autres paramètres pour les événements dans Google Calendar](images/manage-events-in-google-calendar-part-2.png)

L'action d'automatisation "Gérer les événements dans Google Agenda" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée

## Action d'automatisation : Exécuter un traitement des données

Si vous choisissez d'exécuter un traitement de données comme action automatisée, le déclencheur déclenchera une [opération de traitement de données]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) définie à l'avance dans la table. Vous pouvez configurer précisément l'opération à effectuer dans les **Paramètres de l'action**. Selon le type d'opération, **certaines colonnes d'entrée et de sortie** peuvent être nécessaires.

![Définition d'une action d'automatisation : Exécuter un traitement de données](images/run-data-processing-action-settings.jpg)

Les **opérations de traitement de données** suivantes peuvent être exécutées avec une automation :
- [Calculer la différence]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calculer le pourcentage]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calculer le classement]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Extraire le nom d'utilisateur]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparer et copier]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

![opérations de traitement de données exécutables par un automate](images/run-data-processing-available-operations.jpg)

L'action d'automatisation "Exécuter un traitement de données" est actuellement disponible sur le **déclencheur d'automatisation** suivant :
- À une heure programmée

## Action d'automatisation : Convertir une page en PDF

Si vous sélectionnez "Convertir la page en PDF" comme action automatisée, SeaTable créera **un document PDF à partir de l'enregistrement** et l'enregistrera dans une [colonne de fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) lorsque le déclencheur sera déclenché. Pour cela, choisissez un **modèle** que vous aurez préalablement créé dans le [plugin de conception de page]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}). Vous pouvez également définir le **nom de fichier** dans les paramètres de l'action.

![Créer un PDF par automation](images/convert-page-to-pdf-action-settings.jpg)

L'action d'automatisation "Convertir la page en PDF" est actuellement disponible pour le **déclencheur d'automatisation** suivant :
- À une heure programmée pour les enregistrements qui correspondent aux conditions

## Action d'automatisation : Créer un PDF à partir d'un document et l'envoyer

Si vous sélectionnez "Créer un PDF à partir d'un document et l'envoyer" comme action automatisée, SeaTable créera **un document PDF** et l'enregistrera dans le [Gestionnaire de fichiers]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) lorsque le déclencheur est déclenché. De plus, SeaTable peut l'envoyer directement par e-mail.

Pour cela, dans les **paramètres** de l'action, sélectionnez un **modèle** que vous avez préalablement créé dans le plugin **Design de rapport** et attribuez un **nom de fichier**. Activez ensuite le curseur pour sélectionner un **dossier personnel** dans lequel vous souhaitez enregistrer le fichier. Si vous souhaitez uniquement générer le document, vous pouvez quitter la configuration à ce stade.

![créer et envoyer un PDF par automatisation à partir d'un modèle de rapport](images/generate-pdf-from-document-action-settings.jpg)

Si vous souhaitez ensuite envoyer le document généré, activez le curseur "Envoyer par e-mail". Vous pouvez à tout moment modifier le **compte de messagerie**, le **destinataire**, l'**objet** et le **message** de l'e-mail dans les **paramètres** de l'action.

![créer et envoyer un PDF par automatisation à partir d'un modèle de rapport](images/generate-pdf-from-document-and-send-action-settings.jpg)

L'action d'automatisation "Créer un PDF à partir d'un document et l'envoyer" est actuellement disponible pour le **déclencheur d'automatisation** suivant :
- À une heure programmée

## Action d'automatisation : Archiver

L'action d'archivage vous permet de [déplacer automatiquement des lignes vers le stockage Big Data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). Pour cela, la fonction Big Data doit bien sûr être activée dans la base concernée. Comme vous définissez déjà la **vue** et les éventuelles conditions de filtrage pour les lignes à archiver dans les paramètres du déclencheur, vous ne pouvez effectuer aucun réglage pour l'action elle-même.

![archiver des lignes par automatisation](images/automated-action-archive.png)

L'action d'automatisation "Archiver" est actuellement disponible pour les **déclencheurs d'automatisation** suivants :
- À une heure programmée
- À une heure programmée pour les enregistrements qui correspondent aux conditions