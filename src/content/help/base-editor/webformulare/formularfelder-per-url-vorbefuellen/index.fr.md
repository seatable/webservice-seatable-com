---
title: 'Pré-remplir les champs de formulaire'
date: 2023-01-08
lastmod: '2024-03-18'
categories:
    - 'webformulare'
author: 'vge'
url: '/fr/aide/formulaires-pre-remplir-champs-url'
aliases:
    - '/fr/aide/formularfelder-per-url-vorbefuellen'
seo:
    title: 'Formulaires SeaTable : pré-remplir des champs par URL ou lien personnalisé'
    description: 'Formulaires web SeaTable : préremplir les champs par lien avec valeurs par défaut. Guide sur types de colonnes et modes de lecture.'
weight: 5
---

Pour **pré-remplir les formulaires web**, vous avez la possibilité de définir des valeurs par défaut dans les champs du formulaire. Vous pouvez le faire directement dans l'URL ou à l'aide d'une fonction conviviale dans SeaTable.

## Générer un lien de formulaire avec des valeurs par défaut dans SeaTable

SeaTable propose une fonction qui vous permet de générer facilement **des liens de formulaire** dans lesquels les valeurs par défaut sont déjà prédéfinies.

1. Créez un [formulaire web]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. Dans l'éditeur de formulaire web, cliquez sur le bouton {{< seatable-icon icon="dtable-icon-share" >}} **Partager** dans le coin supérieur droit.
3. Cliquez maintenant sur le bouton **Ajouter un lien de formulaire** et le masque de saisie suivant apparaît :
   ![Valeurs pré-remplies dans les liens de formulaire personnalisés](images/Vorbefuellte-Werte-in-benutzerdefinierten-Formularlinks.png)
4. Donnez un **nom** au nouveau lien. Sous **URL personnalisée**, vous pouvez définir vous-même une partie de l'URL.
5. Pour pré-remplir un champ de formulaire avec une valeur par défaut, cliquez sur **Ajouter un champ**. Sélectionnez le **champ de formulaire** dans le menu déroulant et saisissez la **valeur par défaut** souhaitée.
6. Enfin, vous pouvez encore décider si la valeur par défaut peut être modifiée lors du remplissage du formulaire. Pour cela, sélectionnez **Lecture et écriture**. Si vous choisissez **Lecture seule**, la valeur ne peut pas être modifiée dans le formulaire.
7. Cliquez sur **Créer** pour générer le lien.

![Lien de formulaire personnalisé avec valeur pré-remplie](images/Benutzerdefinierter-Formularlink-mit-vorausgefuelltem-Wert.png)

Le résultat, c'est-à-dire l'URL étendue, est le même que celui de la procédure manuelle décrite ci-dessous.

## Pré-remplir un formulaire web directement via l'URL

![Pré-remplir un formulaire web](images/prefill.png)

1. Créez un [formulaire web]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. Dans l'éditeur de formulaire web, cliquez sur le bouton {{< seatable-icon icon="dtable-icon-share" >}} **Partager** pour obtenir le lien vers le formulaire web.
3. **Copiez** le lien et collez-le dans un nouvel onglet dans **la barre d'adresse du navigateur**, où vous pourrez le modifier et le tester.
4. Pour pré-remplir un champ de formulaire avec une valeur par défaut, ajoutez la chaîne de caractères **/?prefill_COLUMNNAME=PREFILLVALUE** au lien du formulaire.

Au lieu de **COLUMNNAME**, insérez le nom du champ que vous souhaitez remplir ; pour **PREFILLVALUE**, insérez la valeur par défaut souhaitée. Les espaces doivent être écrits sous la forme **%20**. Veillez à respecter les majuscules et les minuscules.

**Exemple** : si vous souhaitez envoyer à Joe Smith un formulaire web personnalisé dans lequel son nom est déjà inscrit, ajoutez la chaîne **/?prefill_Name=Joe%20Smith** au lien du formulaire.

Pour utiliser **plusieurs valeurs par défaut**, enchaînez les entrées de pré-remplissage avec le caractère **&** : /?prefill_COLUMNNAME=PREFILLVALUE**&**prefill_COLUMNNAME=PREFILLVALUE

Une fois que vous avez terminé, vous pouvez tester le lien en appuyant sur la **touche Entrée** et en affichant le formulaire web. Si tout s'est bien passé, vous pouvez voir dans cet **aperçu** les valeurs par défaut pré-remplies.

## Champs de formulaire pré-remplissables

Selon le type de colonne sur lequel repose un champ de formulaire, le pré-remplissage n'est pas toujours possible. Dans l'aperçu suivant, vous pouvez voir quels types de colonnes permettent le pré-remplissage par URL et lesquels ne le permettent pas.

| Type de colonne          | Prend en charge le pré-remplissage                            |
| ------------------------ | ------------------------------------------------------------- |
| Numéro automatique       | {{< icon "circle-xmark" >}}                                   |
| Image                    | {{< icon "circle-xmark" >}}                                   |
| Case à cocher            | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Fichier                  | {{< icon "circle-xmark" >}}                                   |
| Date                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Durée                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Sélection unique         | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| E-mail                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Créateur                 | {{< icon "circle-xmark" >}}                                   |
| Créé                     | {{< icon "circle-xmark" >}}                                   |
| Texte formaté            | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Formule                  | {{< icon "circle-xmark" >}}                                   |
| Formule de lien          | {{< icon "circle-xmark" >}}                                   |
| Géoposition              | {{< icon "circle-xmark" >}}                                   |
| Dernier modificateur     | {{< icon "circle-xmark" >}}                                   |
| Sélection multiple       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Collaborateur            | {{< icon "circle-xmark" >}}                                   |
| Évaluation               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Bouton                   | {{< icon "circle-xmark" >}}                                   |
| Signature                | {{< icon "circle-xmark" >}}                                   |
| Numéro de téléphone      | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Texte                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                      | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Nombre                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Dernière modification    | {{< icon "circle-xmark" >}}                                   |
