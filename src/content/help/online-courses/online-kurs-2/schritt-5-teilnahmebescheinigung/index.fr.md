---
title: 'Étape 5 : Attestation de participation'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/fr/aide/etape-5-attestation-de-participation'
aliases:
    - '/fr/aide/schritt-5-teilnahmebescheinigung'
seo:
    title: 'Étape 5 : Attestation de participation PDF par email'
    description: 'Apprenez à créer et envoyer automatiquement des attestations de participation PDF aux participants avec SeaTable.'
---

Une fois votre prestation terminée, vous souhaitez parachever le processus en envoyant un dernier e-mail aux participants. Cet e-mail peut avoir différents contenus, comme par exemple :

- Une confirmation de participation
- Un remerciement pour votre participation
- Une demande de feedback
- Un code de bon pour le prochain cours
- …

## Créer et envoyer une confirmation de participation

Dans cette section, nous utiliserons SeaTable pour générer une confirmation de participation au format PDF et l'envoyer par e-mail aux participants.

### Publipostage avec le plugin de conception de pages

SeaTable propose quelques plugins qui vous permettent d'ajouter des vues et des fonctionnalités supplémentaires à vos données. Le plugin de conception de pages permet de créer des documents PDF, comme un publipostage dans Microsoft Word.

Ce plugin vous permet de créer des modèles qui contiennent à la fois des contenus statiques (comme des textes ou des logos) et des données dynamiques issues de votre base. Chaque ligne du tableau peut générer un document individuel.

{{< warning  headline="De nombreuses possibilités d'utilisation"  text="Le plugin de conception de pages offre de nombreuses possibilités : outre les attestations de participation, vous pouvez également créer des factures, des certificats, des circulaires et bien plus encore." />}}

Pour ce cours, nous avons déjà préparé un modèle simple pour créer une attestation de participation. Le nom, le cours et la date du cours sont automatiquement insérés, tandis que le reste du texte reste inchangé.

Prenez quelques minutes pour explorer les possibilités du plugin. Essayez par exemple d'ajouter un logo ou un graphique à votre signature.

![](images/lvl2-page-design.png)

Si vous cliquez sur `{{< seatable-icon icon="dtable-icon-download" >}} PDF`, le PDF généré est enregistré sur votre PC.

{{< warning  headline="Les modèles se réfèrent toujours à un tableau"  text="Lors de la création d'un nouveau modèle, les données ne peuvent être utilisées qu'à partir d'un seul tableau. Si vous avez besoin de données provenant d'une colonne liée, vous devez les inclure via des colonnes de référence (lookup). C'est la raison pour laquelle, dans le tableau `Registrations`, il existe trois colonnes de référence masquées. Ces colonnes ne sont nécessaires que pour le plugin de conception de pages et peuvent donc rester masquées." />}}

### Envoi par e-mail

Bien entendu, vous ne souhaitez pas télécharger manuellement le PDF et le charger à nouveau pour l'envoyer par e-mail. Au lieu de cela, vous pouvez utiliser un bouton dans le tableau `Registrations` qui exécute deux actions à la suite :

- `{{< seatable-icon icon="dtable-icon-pdf" >}} Create PDF and save to column`
- `{{< seatable-icon icon="dtable-icon-email" >}} Send email`

La configuration de ces actions devrait maintenant vous être familière. Lors de la création du PDF, vous choisissez le modèle souhaité et la colonne dans laquelle le document doit être enregistré. Lors de l'envoi de l'e-mail, vous indiquez la colonne à partir de laquelle la pièce jointe doit être envoyée.

{{< warning  headline="Les actions sont exécutées les unes après les autres"  text="Il n'y a aucun problème à ce que le bouton crée d'abord le fichier PDF et l'envoie ensuite. SeaTable attend que le PDF soit créé avant d'envoyer l'e-mail." />}}

### Quelques mots sur la gestion des fichiers

Dans SeaTable, les fichiers et les images ne sont pas stockés directement dans les cellules, mais dans le magasin de données central de la base. Les cellules contiennent uniquement des références aux fichiers correspondants. Cette gestion centralisée présente plusieurs avantages :

- Les fichiers peuvent être utilisés plusieurs fois sans devoir les télécharger à nouveau.
- Même si vous supprimez un fichier d'une cellule, il reste disponible dans la gestion centrale jusqu'à ce que vous le supprimiez définitivement.

Prenez quelques minutes pour vous familiariser avec la gestion des fichiers dans SeaTable. Pour plus d'informations, consultez les articles d'aide en lien à la fin de cette section.

## Article d'aide avec plus d'informations

- [Instructions pour le plugin de conception de pages]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}})
- [Enregistrer un document PDF par un bouton dans une colonne]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}})
- [La colonne des fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})
- [La gestion des fichiers d'une base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
