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

Une fois le cours terminé, vous voulez clore le processus en envoyant un dernier e-mail aux participants. Il peut contenir, par exemple :

- une attestation de participation ;
- des remerciements ;
- une demande d'avis ;
- un bon de réduction pour le prochain cours ;
- …

## Créer et envoyer une attestation de participation

Dans cette étape, vous allez générer avec SeaTable une attestation de participation au format PDF, puis l'envoyer par e-mail aux participants.

### Un publipostage avec le plugin de conception de pages

SeaTable propose plusieurs plugins, qui ajoutent des vues et des fonctionnalités à vos données. Le plugin de conception de pages crée des documents PDF, à la manière d'un publipostage dans Microsoft Word.

Vous y créez des modèles qui mêlent des contenus fixes (textes, logos…) et des données issues de votre base. Chaque ligne du tableau peut ainsi produire son propre document.

{{< warning  headline="De nombreux usages"  text="Le plugin de conception de pages se prête à bien des usages : outre les attestations de participation, il permet de créer des factures, des certificats, des courriers et bien d'autres documents." />}}

Pour ce cours, un modèle simple d'attestation de participation est déjà prêt : le nom du participant, le cours et sa date y sont insérés automatiquement, le reste du texte ne change pas.

Prenez quelques minutes pour explorer le plugin. Essayez par exemple d'ajouter un logo ou une image sous la signature.

![](images/lvl2-page-design.png)

Un clic sur `{{< seatable-icon icon="dtable-icon-download" >}} PDF` enregistre le PDF généré sur votre ordinateur.

{{< warning  headline="Un modèle porte toujours sur un seul tableau"  text="Un modèle ne peut utiliser que les données d'un seul tableau. Pour y faire figurer des données d'un tableau lié, il faut passer par des colonnes de référence (lookup) : c'est pourquoi le tableau `Registrations` contient trois colonnes de référence masquées. Elles ne servent qu'au plugin de conception de pages et peuvent donc rester masquées." />}}

### Envoi par e-mail

Pas question, bien sûr, de télécharger le PDF pour le joindre ensuite à la main à un e-mail. Un bouton du tableau `Registrations` peut enchaîner les deux actions :

- `{{< seatable-icon icon="dtable-icon-pdf" >}} Create PDF and save to column`
- `{{< seatable-icon icon="dtable-icon-email" >}} Send email`

Ces réglages devraient maintenant vous être familiers. Pour créer le PDF, vous choisissez le modèle et la colonne où enregistrer le document ; pour envoyer l'e-mail, vous indiquez la colonne qui contient la pièce jointe.

{{< warning  headline="Les actions s'exécutent l'une après l'autre"  text="Le bouton peut sans problème créer le PDF puis l'envoyer : SeaTable attend que le PDF soit prêt avant d'envoyer l'e-mail." />}}

### Quelques mots sur la gestion des fichiers

Dans SeaTable, les fichiers et les images ne sont pas stockés dans les cellules elles-mêmes, mais dans un espace de stockage central propre à la base ; les cellules ne contiennent que des références vers ces fichiers. Cette gestion centralisée a plusieurs avantages :

- un même fichier peut servir plusieurs fois, sans avoir à le téléverser de nouveau ;
- un fichier retiré d'une cellule reste disponible dans la gestion des fichiers, jusqu'à ce que vous le supprimiez définitivement.

Prenez quelques minutes pour découvrir la gestion des fichiers de SeaTable. Les articles d'aide ci-dessous vous en diront plus.

## Article d'aide avec plus d'informations

- [Instructions pour le plugin de conception de pages]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}})
- [Enregistrer un document PDF par un bouton dans une colonne]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}})
- [La colonne des fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})
- [La gestion des fichiers d'une base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
