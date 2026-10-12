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

Après avoir créé la structure nécessaire de votre gestion des dépenses à l'étape 1, vous pouvez maintenant saisir de nouvelles dépenses à tout moment à l'aide de votre navigateur. Vous vous en souvenez certainement : chaque ligne représente un nouvel enregistrement et, dans votre cas, une opération de paiement.

Mais bien sûr, ce serait bien si vous pouviez également saisir d'autres dépenses en déplacement via votre téléphone portable. Ou bien vous souhaitez également saisir les dépenses de vos collègues ou des membres de votre famille. Pour ces cas, un formulaire web s'impose, que vous pouvez créer très facilement avec SeaTable, puisque vous avez déjà défini les possibilités du formulaire de saisie par les types de colonnes. Mais pourquoi expliquer les choses de façon longue et compliquée ? Construisons simplement le formulaire et essayons-le.

## Création du formulaire web

Dans l'en-tête de votre base, vous trouverez de nombreuses fonctions supplémentaires. Derrière le bouton `Forms`, SeaTable vous offre la possibilité de créer de nouveaux formulaires web.

![Gestion des formulaires avec bouton « Forms » et nouveau formulaire web](images/level1-create-webform.png)

1. Créez un nouveau formulaire web nommé `Expense Tracking`. En fait, le nom n'a pas d'importance, mais pourquoi ne pas donner un joli nom au formulaire ?
2. Une nouvelle interface utilisateur s'ouvre, dans laquelle vous pouvez concevoir le formulaire web.
3. Faites glisser les quatre champs du tableau `Reason`, `Date`, `Amount` et `Category` par glisser-déposer dans le formulaire.

![Formulaire web « Expense Tracking » avec champs Reason, Date, Amount, Category](images/level1-webform.png)

## Autres paramètres du formulaire web

Votre formulaire web est presque prêt et peut déjà être utilisé. Cependant, il y a encore trois réglages que nous vous conseillons de faire. Pour adapter les paramètres d'un champ de saisie, vous devez cliquer sur le champ de saisie dans le formulaire. Les possibilités de réglage de ce champ de saisie s'affichent alors immédiatement sur le côté droit. Les possibilités de réglage varient en fonction du champ de saisie sur lequel vous cliquez.

- `Category` : les différentes options doivent être affichées sous forme de **liste**.
- `Date` : le jour actuel doit être prédéfini comme **valeur par défaut**.
- `Amount` : la saisie de ce champ est **obligatoire**.

La configuration du formulaire web est maintenant terminée et nous pouvons saisir les premiers enregistrements par ce biais.

## Essayer le formulaire web

Les boutons orange dans le coin supérieur droit permettent d'obtenir soit l'URL du formulaire web, soit un code QR.

Vous verrez qu'à chaque fois que vous enverrez le formulaire, un nouvel enregistrement sera immédiatement écrit dans votre base. Vous n'avez pas besoin de recharger la page dans votre navigateur.

N'hésitez pas à expérimenter le formulaire web pendant quelques minutes et à apprécier les progrès que vous venez de réaliser : **dès maintenant, vous et toute autre personne à qui vous communiquez le lien vers ce formulaire web pouvez créer de nouvelles entrées dans votre base.**

Il est important de noter que seules les nouvelles entrées peuvent être créées via le formulaire web et qu'il n'est pas possible de modifier ou de consulter les entrées existantes.

Prenez également quelques minutes pour explorer les possibilités supplémentaires offertes par le formulaire web.

## Article d'aide avec plus d'informations

- [Les formulaires web en général]({{< relref "help/base-editor/webformulare/webformulare" >}})
- [Créer un formulaire web]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}})
- [Possibilités de configuration d'un formulaire web]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}})
