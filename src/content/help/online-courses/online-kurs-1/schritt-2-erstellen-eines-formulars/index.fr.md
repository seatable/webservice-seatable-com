---
title: 'Étape 2 : Créer un formulaire'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/fr/aide/etape-2-creer-formulaire-web'
aliases:
    - '/fr/aide/schritt-2-erstellen-eines-formulars'
seo:
    title: 'Étape 2 : Créer et utiliser un formulaire web SeaTable'
    description: 'Apprenez à créer et personnaliser un formulaire web dans SeaTable pour collecter vos dépenses lors du cours en ligne.'
---

La structure créée à l'étape 1 vous permet déjà de saisir de nouvelles dépenses à tout moment depuis votre navigateur. Pour rappel : chaque ligne est un enregistrement, ici une dépense.

Mais ce serait plus pratique de pouvoir aussi noter une dépense en déplacement, depuis votre téléphone. Ou de laisser vos collègues, ou votre famille, saisir les leurs. Pour cela, rien de tel qu'un formulaire web, et SeaTable le crée en un rien de temps : les types de colonnes que vous avez choisis définissent déjà les champs du formulaire. Plutôt qu'un long discours, construisons-le et essayons-le.

## Création du formulaire web

En haut de votre base se trouvent de nombreuses fonctions supplémentaires. Le bouton `Forms` vous permet de créer des formulaires web.

![Gestion des formulaires avec bouton « Forms » et nouveau formulaire web](images/level1-create-webform.png)

1. Créez un nouveau formulaire web nommé `Expense Tracking`. Le nom importe peu, mais autant lui en donner un parlant !
2. Un éditeur s'ouvre, dans lequel vous concevez le formulaire.
3. Faites glisser les quatre champs du tableau, `Reason`, `Date`, `Amount` et `Category`, dans le formulaire.

![Formulaire web « Expense Tracking » avec champs Reason, Date, Amount, Category](images/level1-webform.png)

## Autres réglages du formulaire web

Votre formulaire est presque prêt, et déjà utilisable. Nous vous conseillons toutefois trois réglages. Pour régler un champ, cliquez dessus dans le formulaire : ses options s'affichent à droite. Elles varient selon le champ choisi.

- `Category` : les différentes options doivent être affichées sous forme de **liste**.
- `Date` : le jour actuel doit être prédéfini comme **valeur par défaut**.
- `Amount` : la saisie de ce champ est **obligatoire**.

Le formulaire est configuré : vous pouvez maintenant l'utiliser pour saisir vos premières dépenses.

## Essayer le formulaire web

Les boutons orange, en haut à droite, vous donnent l'URL du formulaire ou un code QR.

Chaque envoi du formulaire crée aussitôt une nouvelle ligne dans votre base, sans même que vous ayez à recharger la page.

Prenez quelques minutes pour essayer le formulaire et mesurer le chemin parcouru : **désormais, vous-même et toute personne à qui vous donnez le lien du formulaire pouvez ajouter des dépenses dans votre base.**

Notez qu'un formulaire web ne sert qu'à créer de nouvelles lignes : il ne permet ni de consulter ni de modifier celles qui existent.

Prenez aussi le temps d'explorer les autres options du formulaire web.

## Article d'aide avec plus d'informations

- [Les formulaires web en général]({{< relref "help/base-editor/webformulare/webformulare" >}})
- [Créer un formulaire web]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}})
- [Possibilités de configuration d'un formulaire web]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}})
